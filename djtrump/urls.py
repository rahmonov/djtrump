from django.conf.urls import url
from django.contrib import admin

from djtrump import views

# dumb comment assaasdas
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^personalize$', views.personalize, name='personalize')
]
