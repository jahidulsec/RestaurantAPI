from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# menu item view
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


# single menu item view
class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


# Booking view

class BookingView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer