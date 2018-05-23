from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail)
]
