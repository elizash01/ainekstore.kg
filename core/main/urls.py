from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, ProductSizeViewSet, ProductColorViewSet, VacanciesViewSet, UserListView, UserDetailView

app_name ='main'

router = routers.DefaultRouter()

router.register(r'categoty', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'productsize', ProductSizeViewSet, basename='productsize')
router.register(r'productcolor', ProductColorViewSet, basename='productcolor')
router.register(r'vacancy', VacanciesViewSet, basename='vacancy')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]    