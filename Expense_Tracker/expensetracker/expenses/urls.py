from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenseList, name='expenseList'),                      #To show all expenses
    path('add/', views.expenseCreate, name='expenseCreate'),              #To add new expense
    path('edit/<int:pk>/', views.expenseUpdate, name='expenseUpdate'),    #To edit expense
    path('delete/<int:pk>/', views.expenseDelete, name='expenseDelete'),  #To delete expense
]