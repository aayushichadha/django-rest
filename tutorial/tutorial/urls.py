from django.conf.urls import url,include
from snippets import views as snippets_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    url(r'^max/', snippets_views.max),
    url(r'^check/', snippets_views.check),
    url(r'^admin/', admin.site.urls),
)


