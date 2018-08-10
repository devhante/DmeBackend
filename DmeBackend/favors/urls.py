from django.urls import path
from DmeBackend.favors import views

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:pk>/', views.account_detail),
    path('menus/', views.menu_list),
    path('menus/<int:pk>/', views.menu_detail),
]