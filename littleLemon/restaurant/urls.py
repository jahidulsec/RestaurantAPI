from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name = 'menu'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view(), name='singleMenu'),
    path('api-token-auth/', obtain_auth_token),
]