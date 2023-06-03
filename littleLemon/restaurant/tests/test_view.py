from django.test import TestCase, Client
from django.urls import reverse
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer


# menu view test
class MenuItemViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.list_url = reverse('menu')
        self.item = Menu.objects.create(title = 'IceCream', price=80, inventory=100)

    def test_getall(self):
        response =  self.client.get(self.list_url)

        item1 = MenuItemSerializer(self.item)
        self.assertEqual(response.status_code,200)

