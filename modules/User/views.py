from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .functions import LogIn
from .serializers import UserSerializer

class SignUp(APIView):

	def post(self,request):

		serializer = UserSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)




class LogIn(APIView):
	def get_object(self,request):
		try:
			facebook = request.data["id_facebook"]
			return User.objects.get(facebook=id_facebook)
		except User.DoesNotExist:
			raise Http404

	def post(self,request):
		current_user = self.get_object(request)
		serializer = UserSerializer(current_user)
		return Response(serializer.data,status=status.HTTP_200_OK)