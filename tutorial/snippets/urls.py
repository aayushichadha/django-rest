from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^max/', views.max),
    url(r'^check/', views.check),
)