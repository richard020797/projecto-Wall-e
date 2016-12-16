from django.conf.urls import url
from .views import UserStudySession

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', UserStudySession.as_view()),
]