from django.urls import path
from .views import (
    RecipieList, RecipieDetail
)

urlpatterns = [
    path('', RecipieList.as_view()),
    path('<int:pk>/', RecipieDetail.as_view()),
]
