from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from csweb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("csweb.urls")),
    path('accounts/', include('django.contrib.auth.urls'))
]