from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, 
										ListAPIView, RetrieveAPIView)

# Create your views here.

class SnippetList(ListCreateAPIView):

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	
	def perfom_create(self, serializer):
		serializer.save(owner=self.request.user)

	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SnippetDetail(RetrieveUpdateDestroyAPIView):

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(ListAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer