from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from books import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'topbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name= 'login'),
    url(r'^login/$', auth_views.logout, name= 'logout'),
    url(r'^$', views.index, name='home')

]
