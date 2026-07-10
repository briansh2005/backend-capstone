from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# 1. 建立專門給訂位（Booking/Tables）使用的路由器
booking_router = DefaultRouter()
booking_router.register(r'tables', views.BookingViewSet)

api_router = DefaultRouter()
api_router.register(r'users', views.UserViewSet)
api_router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # --- Generic Views 菜單 API ---
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    # --- Step 4 核心 要求追加的訂位 API 網址 ---
    path('booking/', include(booking_router.urls)),

    # --- 驗證與其他 API ---
    path('api/', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 受保護訊息網址
    path('message/', views.msg, name='message'),

    # 要求追加的「取得 Token」自動驗證網址
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]