#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from gallery.models import Gallery, GalleryImage
from gallery.forms import GalleryImageForm
from recipes.models import Recipe
from fileupload.views import response_mimetype, JSONResponse
from sorl.thumbnail import get_thumbnail


def recipe_gallery_upload(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = recipe.gallery
            image = form.save(commit=False)
            image.gallery = gallery
            image.save()
            thumbnail = get_thumbnail(image, '100x100', crop='center', quality=99)
            f = request.FILES.get('image')
            data = [{
                'name': f.name,
                'url': image.image.url,
                'thumbnail_url': thumbnail.url,
                'delete_url': reverse('upload-delete', args=[image.id]), 'delete_type': "DELETE"
            }]
            response = JSONResponse(data, {}, response_mimetype(request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            raise Exception(form.errors)
    data = {
        "form": GalleryImageForm,
        "recipe": recipe
    }
    return render(request, "gallery/add_image_to_recipe.html", data)