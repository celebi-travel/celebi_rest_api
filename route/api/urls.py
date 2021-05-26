from django.urls import path
from route.api import views

urlpatterns = [
    path('', views.PlaceListAPIView.as_view(), name='places'),
    path('<int:id>/', views.PlaceDetailAPIView.as_view(), name='place_detail'),
]
