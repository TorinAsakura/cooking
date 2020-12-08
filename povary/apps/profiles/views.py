# -*- coding: utf-8 -*-
import datetime
import os
import json
from uuid import uuid4

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count
from django.contrib.auth import login

from fileupload.views import JSONResponse, response_mimetype
from sorl.thumbnail import get_thumbnail
from filebrowser.base import FileObject
from profiles.forms import ProfileForm, ProfileSettingsForm, AvatarForm
from utils import ajax_required, crop_image
from recipes.models import Recipe, RecipesBox
from recipes.forms import RecipesBoxForm
from notifications.models import Notice
from search.forms import RecipeSearchForm

from profiles.models import Profile
from registration.views import RegistrationView
from profiles.forms import RegisterForm
from forum_integration.api import register_forum_user
from core.tasks import send_mail, async_func
from gallery.models import Gallery
from regions.models import City, Country
from utils.utils import get_complex_paginator, search


def list(request):

    lookup_params = {'cook': True}

    q = request.GET.get('query')
    srt = request.GET.get('sort')
    order = request.GET.get('order')

    print srt, order

    profile_list = Profile.objects.all()

    now = datetime.datetime.now()
    delta = now - datetime.timedelta(days=90)
    new_profiles = profile_list.filter(user__date_joined__gte=delta)

    if q:
        profile_list = search(q, 'user__username', profile_list)
    else:
        country = request.GET.get('country')
        city = request.GET.get('city')
        sex = request.GET.get('sex')
        age = request.GET.get('age')
        recipes_number = request.GET.get('recipes')
        is_online = request.GET.get('is_online')

        if country:
            lookup_params['country_id'] = country
        if city:
            lookup_params['city_id'] = city
        if sex and sex != 'any':
            lookup_params['sex'] = sex
        if age:
            year = now.year
            birthday_year = year - int(age)
            date = datetime.date(birthday_year, 1, 1)
            lookup_params['birthday__gte'] = date
        if recipes_number:
            lookup_params['num_recipes__lte'] = recipes_number

        profile_list = profile_list.annotate(
            num_recipes=Count('user__recipe')).filter(**lookup_params)

        new_profiles = new_profiles.annotate(
            num_recipes=Count('user__recipe')).filter(**lookup_params)

        if is_online:
            profile_list = filter(lambda x: x.online(), profile_list)
            new_profiles = filter(lambda x: x.online(), new_profiles)

    pages_per_part = 8
    profile_per_page = 5
    page = request.GET.get('page')
    part = request.GET.get('part', 1)
    new_page = request.GET.get('new_page')
    new_part = request.GET.get('new_part', 1)

    profile_list, part_list, prev_base_page, next_base_page = \
        get_complex_paginator(
            profile_list,
            page if page else 1,
            part,
            profile_per_page,
            pages_per_part
        )

    new_profiles, new_part_list, new_prev_base_page, new_next_base_page = \
        get_complex_paginator(
            new_profiles,
            new_page if new_page else 1,
            new_part,
            profile_per_page,
            pages_per_part
        )

    data = {
        "new_part_list": new_part_list,
        "new_profiles": new_profiles,
        "new_prev_base_page": new_prev_base_page,
        "new_next_base_page": new_next_base_page,

        "part_list": part_list,
        "profile_list": profile_list,
        "prev_base_page": prev_base_page,
        "next_base_page": next_base_page,
        "profile_per_page": profile_per_page,

        "new": True if new_page else False,

        "cities": City.objects.all()[:10], #todo: remove 10 and do autocomplete for cities
        "countries": Country.objects.all()
    }

    return render(request, 'profiles/list.html', data)


@login_required
def profile(request):
    user = request.user
    form = ProfileForm(request.POST or None,
                       instance=request.user.profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.info(request, "Профиль успешно изменен")
    if request.user.profile.avatar:
        avatar_img = request.user.profile.avatar.url
    elif request.user.profile.original_avatar:
        avatar_img = get_thumbnail(request.user.profile.original_avatar,
                                   '300x300').url
    else:
        avatar_img = None
    my_recipes = Recipe.objects.filter(author=user)[:3]
    my_recipes_all = Recipe.objects.filter(author=user).count()
    data = {
    "user": user,
    "form": form,
    "search_form": RecipeSearchForm,
    "avatar_img": "avatar_img",
    "original_avatar": request.user.profile.original_avatar,
    "csrf_token": get_token(request),
    "my_recipes": my_recipes,
    "my_recipes_all": my_recipes_all,
    }
    return render(request, 'profiles/profile.html', data)


@ajax_required
@login_required
def upload_avatar(request):
    profile = request.user.profile
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            thumbnail = get_thumbnail(profile.original_avatar, '600x600')
            f = request.FILES.get('original_avatar')
            data = [{
                    'name': f.name,
                    'url': profile.original_avatar.url,
                    'thumbnail_url': thumbnail.url,
                    # 'delete_url': reverse('upload-delete', args=[image.id]), 'delete_type': "DELETE"
                    }]
            response = JSONResponse(data, {}, response_mimetype(request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            raise Exception(form.errors)
    data = {
    "form": AvatarForm
    }
    return render(request, "profiles/upload_avatar.html", data)


@ajax_required
def crop_avatar(request):
    if request.GET:
        profile = request.user.profile
        src_img = get_thumbnail(profile.original_avatar, '600x600').url
        x = float(request.GET['x'])
        y = float(request.GET['y'])
        x2 = float(request.GET['x2'])
        y2 = float(request.GET['y2'])
        src_img = '/'.join(src_img.strip('/').split('/')[1:])
        original_path = os.path.join(settings.MEDIA_ROOT, src_img)
        filename, extension = os.path.splitext(str(profile.original_avatar))
        filepath = '/'.join(filename.split('/')[:-1])
        filename = filename.split('/')[-1]
        cropped_filename = filename + '.cropped' + extension
        base_dir = os.path.join(
            "profiles",
            "%s_images" % (profile.user.username)
        )
        cropped_avatar = os.path.join(
            base_dir,
            cropped_filename
        )
        abs_out_dir = os.path.join(
            settings.MEDIA_ROOT,
            base_dir,
        )
        abs_out_img = os.path.join(
            abs_out_dir,
            cropped_filename
        )
        if not os.path.exists(abs_out_dir):
            os.makedirs(abs_out_dir)
        crop_image(original_path, abs_out_img,
                   (int(x), int(y), int(x2), int(y2)))
        key = "?%s" % uuid4().hex[:10]
        profile.avatar = cropped_avatar
        profile.save()
        data = {"url": profile.avatar.url + key, "path": profile.avatar.path}
        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return HttpResponse("FALSE")


def change_avatar(request):
    fb_path = request.GET.get('fb_path', None)
    if fb_path:
        import ipdb

        ipdb.set_trace()
        profile = request.user.profile
        request.user.profile.original_avatar = FileObject(fb_path)
        src_img = profile.original_avatar.version_generate('large')
        original_path = os.path.join(settings.MEDIA_ROOT, src_img.path)
        fb_out_img = os.path.join('uploads', src_img.folder,
                                  src_img.filename_root + '.cropped' + src_img.extension)
        abs_out_img = os.path.join(settings.MEDIA_ROOT, fb_out_img)
        crop_image(original_path, abs_out_img, (100, 100, 500, 500))
        cropped_avatar = FileObject(fb_out_img)

        request.user.profile.avatar = cropped_avatar
        request.user.profile.save()
        key = "?%s" % uuid4().hex[:10]
        large_avatar_url = request.user.profile.original_avatar.version_generate(
            'large').url
        data = {"url": large_avatar_url + key,
                "path": request.user.profile.original_avatar.path}
        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return HttpResponse("FALSE")


@csrf_exempt
@ajax_required
def check_user_existence(request):
    if request.method == "POST":
        username = request.POST.get("username", "").lower()
        email = request.POST.get("email")
        if User.objects.filter(Q(username__iexact=username) | Q(email=email)):
            data = json.dumps({
            "status": "ok",
            "user_exist": True
            })
        else:
            data = json.dumps({
            "status": "ok",
            "user_exist": False
            })
    else:
        data = json.dumps({
        "status": "error",
        "message": "Only POST requests"
        })
    return HttpResponse(data, mimetype="application/json")


@login_required
def password_change_done(request):
    messages.info(request, 'Пароль был успешно изменен!')
    return HttpResponseRedirect(reverse("profile"))


@login_required
def profile_settings(request):
    profile_settings = request.user.profile.settings
    form = ProfileSettingsForm(request.POST or None, instance=profile_settings)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Настройки успешно изменены.')
            return HttpResponseRedirect(reverse('profile'))
    data = {
    "settings_form": form
    }
    return render(request, "profiles/profile_settings.html", data)


def public_userpage(request, username):
    user = get_object_or_404(User, username=username)
    user_recipes = Recipe.objects.filter(author=user, published=True,
                                         completed=True)[:8]
    recipe_boxes = user.profile.recipesboxes.all()
    user.profile.inc_visits()
    data = {
    "user": user,
    "user_recipes": user_recipes,
    "recipe_boxes": recipe_boxes
    }
    return render(request, "profiles/public_userpage.html", data)


@login_required
def recipebox_manage(request):
    recipebox_list = RecipesBox.objects.filter(author=request.user.profile,
                                               published=True).order_by(
        "-created")
    if request.method == "POST":
        create_recipebox_form = RecipesBoxForm(request.user, request.POST)
        if create_recipebox_form.is_valid():
            box = create_recipebox_form.save(commit=False)
            box.author = request.user.profile
            box.save()
            messages.info(request,
                          u"Коробка '%s' успешно добавлена" % (box.title))
    create_recipebox_form = RecipesBoxForm(request.user)
    data = {
    "recipebox_list": recipebox_list,
    "create_recipebox_form": create_recipebox_form,
    }
    return render(request, "profiles/recipebox_manage.html", data)


@login_required
def recipebox_edit(request, recipebox_id):
    box = get_object_or_404(RecipesBox, id=recipebox_id, published=True)
    if box.author != request.user.profile:
        messages.info(request, u"Изменять коробку может только автор")
        return HttpResponseRedirect(reverse("recipebox_manage"))
    if request.method == "POST":
        form = RecipesBoxForm(request.user, request.POST, instance=box)
        if form.is_valid():
            box = form.save()
            data = {
            "form": form
            }
            messages.info(request, u"Коробка изменена")
            return HttpResponseRedirect(reverse('recipebox_manage'))
    form = RecipesBoxForm(request.user, instance=box)
    data = {
    "form": form
    }
    return render(request, "profiles/edit_recipebox.html", data)


@login_required
def recipebox_details(request, recipebox_id):
    box = get_object_or_404(RecipesBox, id=recipebox_id, published=True)
    if not box.is_public and box.author != request.user.profile:
        return HttpResponseForbidden("У вас нет прав на просмотр этой коробки")
    recipe_list = box.recipe_list.filter(published=True)
    paginator = Paginator(recipe_list, 10)
    page = request.GET.get('page')
    try:
        recipe_list = paginator.page(page)
    except PageNotAnInteger:
        recipe_list = paginator.page(1)
    except EmptyPage:
        recipe_list = paginator.page(paginator.num_pages)

    data = {
    "box": box,
    "recipe_list": recipe_list
    }
    return render(request, "profiles/recipebox_details.html", data)


@login_required
def recipebox_remove(request, recipebox_id):
    recipebox = get_object_or_404(RecipesBox, id=recipebox_id)
    if recipebox.author == request.user.profile:
        recipebox.published = False
        recipebox.save()
        return HttpResponseRedirect(reverse("recipebox_manage"))
    else:
        return HttpResponseForbidden("У Вас нет прав на удаление этой коробки")


@login_required
def remove_recipe_from_box(request, recipe_slug, recipebox_id):
    refer = request.META.get('HTTP_REFERER')
    try:
        box = RecipesBox.objects.get(id=recipebox_id)
    except RecipesBox.DoesNotExist:
        box = None
        messages.info(request, "Коробка не найдена")
    if box.author == request.user.profile:
        try:
            recipe = Recipe.objects.get(slug=recipe_slug)
        except Recipe.DoesNotExist:
            messages.info(request, "Рецепт не найден")
            recipe = None
        if box and recipe:
            box.recipe_list.remove(recipe)
            messages.info(request, "Рецепт удален из коробки")
    else:
        messages.info(request, "Вы не можете редактировать эту коробку")
    if refer:
        return HttpResponseRedirect(refer)
    else:
        return HttpResponseRedirect(reverse("recipebox_manage"))


class RegisterView(RegistrationView):
    """
    Custom registration view that uses our custom form.

    """
    form_class = RegisterForm
    success_url = "/"

    def register(self, request, **cleaned_data):
        user = User.objects.create(username=request.POST['username'],
                                   email=request.POST['email'])
        user.set_password(request.POST['password1'])
        user.is_active = True
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        user_password = request.POST['password1']
        user_ip_addr = request.META['REMOTE_ADDR']
        # register_forum_user(user.username, user_password, user_ip_addr)
        async_func.delay(register_forum_user, user.username, user_password,
                         user_ip_addr)
        login(request, user)
        gallery_title = user.username + '_gallery'
        gallery, created = Gallery.objects.get_or_create(title=gallery_title)
        user.profile.gallery = gallery
        user.profile.save()
        return user
