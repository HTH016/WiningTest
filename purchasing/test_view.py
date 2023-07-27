from django.test import TestCase
from django.test.client import Client
from store.models import WinSell


# Create your tests here.
class TestView(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        wine_id = 8
        user_i = "test1111"
        sell_id = 74

    def test_store_list_view(self):
        page = self.client.get("/purchase/store-list")
        self.assertEquals(page.status_code, 200)
        page.content

    def test_detail_product_list_view(self):
        pass

    def test_buy_list_view(self):
        pass

    def test_add_pick_list_view(self):
        pass
