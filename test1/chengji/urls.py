from django.conf.urls import url
from chengji import views

urlpatterns=[
    url(r'^deng$',views.sy),
    url(r'^login_check$',views.login_check)
]