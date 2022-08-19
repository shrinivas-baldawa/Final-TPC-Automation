from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('placements/', views.placement, name='dashboard-products'),
    path('students/', views.student, name='dashboard-customers'),
    path('companies/', views.company, name='dashboard-order'),
]







#     path('customers/detial/<int:pk>/', views.customer_detail,
#          name='dashboard-customer-detail'),
#     path('products/delete/<int:pk>/', views.product_delete,
#          name='dashboard-products-delete'),
#     path('products/detail/<int:pk>/', views.product_detail,
#          name='dashboard-products-detail'),
#     path('products/edit/<int:pk>/', views.product_edit,
#          name='dashboard-products-edit'),