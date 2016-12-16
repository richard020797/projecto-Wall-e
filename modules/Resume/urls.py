from django.conf.urls import url
from .views import SessionResume, ListAllSessionResumes

urlpatterns = [

	url(r'^newResume/$', ListAllSessionResumes.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', SessionResume.as_view()),
]