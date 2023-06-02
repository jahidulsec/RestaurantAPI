from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booking', views.BookingView)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name = 'menu'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view(), name='singleMenu'),
]