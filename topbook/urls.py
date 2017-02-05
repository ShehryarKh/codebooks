from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from books import views

urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name= 'login'),
    url(r'^login/$', auth_views.logout, name= 'logout'),
    url(r'^$', views.index, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
