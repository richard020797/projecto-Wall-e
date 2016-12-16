from django.conf.urls import url
from .views import UserStudySession, ListAllStudySessions

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', UserStudySession.as_view()),
	url(r'^all/$', ListAllStudySessions.as_view()),
]