from django.urls import path
from . import views

app = 'dore'
urlpatterns = [
    path('', views.ProductView.as_view(), name='product_all'),
    path('<int:pk>/', views.ProductView.as_view(), name='product_detail '),
    path('about/', views.about, name='about'),
    path('cats/', views.CategoryView.as_view(), name='category_all'),
    # path('cats/<int:cat_id>/', views.CategoryView.as_view()),   # name='product_list_by_category'
 #   path('cats/<slug:cat_slug>/', views.CategoryView.as_view(), name='category_slag'),
#path('', views.CategoryView.as_view(), name='product_list'),  # Домашняя страница
    #path('<int:id>/<slug:slug>/', views.ProductView.as_view(), name='product_detail'),  # Страница продукта
]
