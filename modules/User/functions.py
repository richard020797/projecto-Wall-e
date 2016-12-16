from django.contrib.auth import authenticate, login


def LogIn(request, username, id_facebook):
	user = authenticate(
		username = username,
		password = id_facebook)

	if user is not None:
		login(request, user)