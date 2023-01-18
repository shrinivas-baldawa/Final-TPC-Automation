from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('bulletin/', views.bulletin, name='dashboard-bulletin'),
    path('marksheet/', views.marksheet, name='dashboard-marksheet'),
    path('placements/', views.placement, name='dashboard-placements'),
    path('students/', views.student, name='dashboard-students'),
    path('companies/', views.company, name='dashboard-companies'),
    path('index/', views.HomeView.as_view(),name='dashboard-index'),
    path('bulletin/delete/<notice>', views.product_delete, name='dashboard-products_delete'),
    path('api', views.ChartData.as_view()),
    path("search/", views.SearchResultsView.as_view(), name="search"),
    path("search1/", views.SearchResultsView1.as_view(), name="search1"),
    path("students/sendMail/", views.sendMail, name="sendMail"),
    path("search/sendMail/", views.sendMail, name="sendMail"),
    path("search1/sendMail/", views.sendMail, name="sendMail"),
]