from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
    (r'^auth/$', views.facebook_auth),
    # Define other pages you want to create here
)

