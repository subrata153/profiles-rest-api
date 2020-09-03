from django.urls import path, include

from rest_framework.routers import DefaultRouter 

from profile_api import views

router = DefaultRouter()
"""Regiater viewset url using rest default router"""
"""we only need to specify the basename if we are not creating a view set that doesn't have queryset or if we want to ovveride the name of the queryset"""
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #dynamically creates the api url using rest routers function
    path('', include(router.urls))
]