from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    url(r'^daguerre/', include('daguerre.urls')),
    url(r'^species$', views.about_animal, name='species'),
    url(r'^breeder$', views.about_breeder, name='breeder'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^animal$', views.entries, name='animal'),
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
