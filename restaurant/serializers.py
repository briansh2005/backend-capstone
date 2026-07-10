from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu

# 1. Coursera 要求的 User 序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# 2. 餐廳訂位（Booking）序列化器
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # 包含 id, name, no_of_guests, booking_date

# 3. 餐廳菜單（Menu）序列化器
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # 包含 id, title, price, inventory
