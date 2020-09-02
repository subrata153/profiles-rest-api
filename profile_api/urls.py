from django.urls import path, include

from rest_framework.routers import DefaultRouter 

from profile_api import views

router = DefaultRouter()
"""Regiater viewset url using rest default router"""
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #dynamically creates the api url using rest routers function
    path('', include(router.urls))
]