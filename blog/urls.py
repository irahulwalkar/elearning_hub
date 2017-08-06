from django.conf.urls import url
from blog import views

urlpatterns = [
	url('^$', views.topic_list, name='topic_list'),
	url('^topic/(?P<pk>\d+)/$', views.post_list, name='post_list'),
	url('^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^blog/login/$', views.user_login, name='login'),    
    url(r'^blog/logout/$', views.user_logout, name='logout'),
]