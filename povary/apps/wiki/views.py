# -*- coding: utf-8 -*-
import json

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType

from reversion_compare.helpers import html_diff, EFFICIENCY, unified_diff

from wiki.models import WikiPage, WikiPageVersion, WikiDiscussion
from wiki.forms import WikiPageForm, WikiDiscussionForm
from comments.models import Comment


def wikipage_details(request, wikipage_slug):
	try:
		page = WikiPage.objects.get(slug=wikipage_slug, published=True, verified=True)
	except WikiPage.DoesNotExist:
		page = None
	data = {
		"page": page,
		"page_slug": wikipage_slug,
		"item_obj": page,
	}
	return render(request, "wiki/details.html", data)


def wikipage_edit(request, wikipage_slug):
	try:
		page = WikiPage.objects.get(slug=wikipage_slug)
	except WikiPage.DoesNotExist:
		page = None
	form = WikiPageForm(request.POST or None, instance=page)
	if request.method == "POST":
		if form.is_valid():
			wikipage = form.save(commit=False)
			if request.user.is_authenticated():
				wikipage.author = request.user
			wikipage.ip_addr = request.META.get("REMOTE_ADDR", "")
			wikipage.slug = wikipage_slug
			if not page:
				wikipage.save()
				WikiPageVersion.init_version(wikipage)
			else:
				author = request.user if request.user.is_authenticated() else None
				version = WikiPageVersion.objects.create(
					page=page,
					old_title=page.title,
					old_slug=page.slug,
					old_image=page.image,
					old_body=page.body,
					old_warnings=page.warnings,
					old_prooflinks=page.prooflinks,
					new_title=wikipage.title,
					new_slug=wikipage.slug,
					new_image=wikipage.image,
					new_body=wikipage.body,
					new_warnings=wikipage.warnings,
					new_prooflinks=wikipage.prooflinks,
					author=author,
					reason = form.cleaned_data['reason'],
					ip_addr=request.META.get("REMOTE_ADDR", '')
				)
			messages.info(request, "Страница энциклопедии отправлена на рассмотрение администрации. Спасибо.")
			return HttpResponseRedirect(reverse("wikipage_details", args=(wikipage.slug, )))
	data = {
		"form": form
	}
	return render(request, "wiki/edit.html", data)


def wikipage_history(request, wikipage_slug):
	wikipage = get_object_or_404(WikiPage, slug=wikipage_slug, published=True, verified=True)
	version_list = wikipage.get_versions().order_by('-revision')
	data = {
		"version_list": version_list,
		"wikipage_slug": wikipage_slug,
		"compare_box": [int(i) for i in request.session.get("versions2cmp", ())],
		"compare_list": [WikiPageVersion.objects.get(id=int(i)) for i in request.session.get("versions2cmp", ())]
	}
	return render(request, "wiki/history.html", data)


@csrf_exempt
def markdown_preview(request):
	import markdown
	if request.method == "POST":
		data = request.POST.get('data', '')
		return HttpResponse(markdown.markdown(data))
	else:
		raise Http404


def add2compare(request, wikipage_slug):
	version_id = request.GET.get("version_id")
	if version_id:
		versions2compare = request.session.get('versions2cmp', [])
		if len(versions2compare) == 2:
			messages.info(request, "Невозможно сравнить больше двух элементов. Измените параметры сравнения.")
			return HttpResponseRedirect(reverse("wikipage_history", args=(wikipage_slug, )))
		versions2compare.append(version_id)
		request.session['versions2cmp'] = versions2compare
	return HttpResponseRedirect(reverse("wikipage_history", args=(wikipage_slug, )))


def rm_compare(request, wikipage_slug):
	version_id=request.GET.get("version_id")
	if version_id:
		versions2compare = request.session.get('versions2cmp', [])
		try:
			versions2compare.remove(str(version_id))
			request.session['versions2cmp'] = versions2compare
		except ValueError:
			pass
	return HttpResponseRedirect(reverse("wikipage_history", args=(wikipage_slug, )))


def versions_compare(request, wikipage_slug):
	items2compare = request.session.get('versions2cmp', ())
	if len(items2compare) != 2:
		return HttpResponse("Fucking shit. Less than 2 comparing items")
	item1 = WikiPageVersion.objects.get(id=int(items2compare[0]))
	item2 = WikiPageVersion.objects.get(id=int(items2compare[1]))
	field_list = {"Заголовок": "new_title", "URL":"new_slug", "Изображение":"new_image",
		"Текст":"new_body", "Предупреждения":"new_warnings",
		"Ссылки на первоисточники":"new_prooflinks"
	}
	title_diff = html_diff(item1.new_title, item2.new_title)
	slug_diff = html_diff(item1.new_slug, item2.new_slug)
	image_diff = html_diff(item1.new_image, item2.new_image)
	body_diff = html_diff(item1.new_body, item2.new_body)
	warnings_diff = html_diff(item1.new_warnings, item2.new_warnings)
	prooflinks_diff = html_diff(item1.new_prooflinks, item2.new_prooflinks)
	wikipage = WikiPage.objects.get(slug=wikipage_slug)
	data = {
		# "diff_list": global_diff,
		"item1": item1,
		"item2": item2,
		"wikipage_slug": wikipage_slug,
		"wikipage": wikipage,
		"discussion_form": WikiDiscussionForm,
		"title_diff": title_diff,
		"slug_diff": slug_diff,
		"image_diff": image_diff,
		"body_diff": body_diff,
		"warnings_diff": warnings_diff,
		"prooflinks_diff": prooflinks_diff
	}
	return render(request, "wiki/compare.html", data)


def comment_version(request, version_id):
	if request.method == "POST":
		form = WikiDiscussionForm(request.POST)
		if form.is_valid():
			version = WikiPageVersion.objects.get(id=version_id)
			discussion = form.save(commit=False)
			discussion.version = version
			discussion.author = request.user if request.user.is_authenticated() else None
			discussion.save()
			return HttpResponseRedirect(reverse('wikipage_history', args=(version.page.slug, )))
	data = {
		"discussion_form": WikiDiscussionForm,
		"version_id": version_id,
	}
	return render(request, "wiki/version_commentform.html", data)


def ajax_commentversion(request, version_id):
	if request.method == "POST":
		form = WikiDiscussionForm(request.POST)
		if form.is_valid():
			version = WikiPageVersion.objects.get(id=version_id)
			discussion = form.save(commit=False)
			discussion.version = version
			discussion.author = request.user if request.user.is_authenticated() else None
			discussion.save()
			data = {
				"status": "ok",
				"body": discussion.text,
				"author": discussion.author.username,
				"pub_date": discussion.pub_date.isoformat(),
			}
		else:
			data = {
				"status": "error",
				"error": "validation_error",
				"message": form.errors
			}
	else:
		data = {
			"status": "error",
			"error": "request_error",
			"message": "Must be POST request"
		}
	return HttpResponse(json.dumps(data), mimetype="application/json")


def version_discussion(request, version_id):
	version = WikiPageVersion.objects.get(id=version_id)
	if request.method == "POST":
		form = WikiDiscussionForm(request.POST)
		if form.is_valid():
			discussion = form.save(commit=False)
			discussion.version = version
			discussion.author = request.user if request.user.is_authenticated() else None
			discussion.save()
			return HttpResponseRedirect(reverse('wikipage_history', args=(version.page.slug, )))
	comment_list = WikiDiscussion.objects.filter(version=version)
	data = {
		"discussion_form": WikiDiscussionForm,
		"comment_list": comment_list,
		"version_id": version_id
	}
	return render(request, "wiki/version_discussion.html", data)
