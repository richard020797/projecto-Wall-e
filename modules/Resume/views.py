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

class SessionResume(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return Resume.objects.get(pk=pk)
		except Resume.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		resume = self.get_object(pk)
		serializer = ResumeSerializer(resume)
		return Response(serializer.data)

class ListAllSessionResumes(APIView):
	#permission_classes = (ApiUserPermissions,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get(self,request):
		resume = Resume.objects.all()
		serializer = ResumeSerializer(resume, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = ResumeSerializer(data = request.data)
		serializer.resume_text = resumeFunction(serializer.original_text)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)