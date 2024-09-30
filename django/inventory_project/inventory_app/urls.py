from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet
from . import views

router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),  
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
