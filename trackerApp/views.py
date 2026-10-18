from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.response import Response
from trackerApp.models import Expenses
from trackerApp.serializers import ExpenseModel
from rest_framework import authentication,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class CreateListApiView(CreateAPIView,ListAPIView):
    serializer_class=ExpenseModel
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
         DjangoFilterBackend,
         SearchFilter,
         OrderingFilter
    ]
    filterset_fields=['category','payment']
    search_fields=['title']
    ordering_fields=['amount','created_at']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        return Expenses.objects.filter(owner=self.request.user)

class RetrieveUpdateDeleteApiView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ExpenseModel
    lookup_url_kwarg="id"
    def get_queryset(self):
        return Expenses.objects.filter(owner=self.request.user)
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
    def perform_destroy(self, instance):
        return instance.delete()
    def retrieve(self, request, *args, **kwargs):
       instance=self.get_object()
       serializer=self.get_serializer(instance)
       return Response(serializer.data)
