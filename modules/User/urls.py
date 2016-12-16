from django.conf.urls import url
from .views import SignUp, LogIn

urlpatterns = [
	url(r'^login/sign$', SignUp.as_view()),
	url(r'^login/$', LogIn.as_view()),
]