from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template import RequestContext

from haystack.views import SearchView, FacetedSearchView
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet

from search.forms import FacetSearchForm, RecipeSearchForm
from search.views import FacetRequestContext
from search.models import faceted_searchqueryset

from filebrowser.sites import site

import autocomplete_light
# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'povary.views.home', name='home'),
                       # url(r'^povary/', include('povary.foo.urls')),

                       url(r'^$', 'core.views.home', name='home'),
                       url(r'^cake$', 'core.views.cake_home', name='cake_home'),
                       url(r'^admin/filebrowser/', include(site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('profiles.urls')),
                       url(r'^recipes/', include('recipes.urls')),
                       #url(r'^setman/', include('setman.urls')),
                       url(r'^ingredients/', include('ingredients.urls')),
                       url(r'^comments/', include('comments.urls')),
                       url(r'^competitions/', include('competitions.urls')),
                       url(r'^categories/', include('categories.urls')),
                       url(r'^messages/', include('notifications.urls')),
                       url(r'^gallery/', include('gallery.urls')),
                       url(r'^upload/', include('fileupload.urls')),
                       url(r'^events/', include('events.urls')),
                       url(r'^tags/', include('tags.urls')),
                       url(r'^articles/', include('articles.urls')),
                       url(r'^masterclass/', include('master_class.urls')),
                       url(r'^cakegallery/', include('cakegallery.urls')),
                       url(r'^ranking/', include('ranking.urls')),
                       url(r'^wiki/', include('wiki.urls')),
                       url(r'^pages/', include('pages.urls')),
                       url(r'^search/', FacetedSearchView(
                           form_class=RecipeSearchForm,
                           searchqueryset=faceted_searchqueryset,
                           context_class=FacetRequestContext
                       ),
                           name='haystack_search'
                       ),
                       url(r'^article.php$', 'articles.views.old_article', name='old_article'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset', name="password_reset"),
                       url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
                       url(r'^markitup/', include('markitup.urls')),
                       url(r"^contact/$", 'core.views.contact', name='core-contact'),
                       url(r'^autocomplete/', include('autocomplete_light.urls')),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
