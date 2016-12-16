from django.conf.urls import url, include
from django.contrib import admin
#from rest_framework_jwt.views import obtain_jwt_token
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^resumes/', include('modules.Resume.urls', namespace="resumes")),
    url(r'^sessions/', include('modules.Session.urls', namespace="sessions")),
    url(r'^users/', include('modules.Session.urls', namespace="users")),
]