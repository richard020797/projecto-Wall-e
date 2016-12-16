from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ResumeSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .summarization import resumeFunction
#from .permissions import ApiUserPermissions

class UserStudySession(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return Session.objects.get(pk=pk)
		except Session.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		session = self.get_object(pk)
		serializer = SessionSerializer(session)
		return Response(serializer.data)

class ListAllStudySessions(APIView):
	#permission_classes = (ApiUserPermissions,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get(self,request):
		sessions = Session.objects.all()
		serializer = SessionSerializer(sessions, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = SessionSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)