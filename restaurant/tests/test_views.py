from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    # 1. 依照要求，使用 setUp() 在每次測試前建立測試資料
    # (注意：Python 內建規範為大寫 U 的 setUp)
    def setUp(self):
        Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        Menu.objects.create(title="Burger", price=8.50, inventory=30)
        Menu.objects.create(title="Pasta", price=14.00, inventory=20)

    # 2. 依照要求，建立 test_getall() 撈取所有資料並驗證
    def test_getall(self):
        # 透過 API 客端發送 GET 請求到你的菜單 API 網址
        response = self.client.get(reverse('menu-items'))

        # 從資料庫中撈出剛才建立的所有菜單
        menus = Menu.objects.all()
        # 使用我們之前寫好的 MenuSerializer 進行序列化
        serializer = MenuSerializer(menus, many=True)

        # 斷言：驗證 API 回傳的資料與序列化後的資料完全相同
        self.assertEqual(response.data, serializer.data)
        # 順便驗證 HTTP 狀態碼是否為 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
