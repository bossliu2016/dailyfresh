from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$',views.logout),
    url(r'^info/$', views.info),
    url(r'^order(\d*)/$', views.order),
    url(r'^site/$', views.site),

]
