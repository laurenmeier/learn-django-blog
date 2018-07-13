from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^teaching/$', views.teaching_list, name='teaching_list'),
    url(r'^projects/$', views.projects_list, name='projects_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]