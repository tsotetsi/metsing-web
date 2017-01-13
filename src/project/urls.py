from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('metsing.apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
