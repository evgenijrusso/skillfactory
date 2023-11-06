from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models.products import Product
from .models.categories import Category
from django.shortcuts import render, get_object_or_404

menu = ["О сайте", "Добавить категорию", "Добавить продукт", "Обратная связь", "Войти"]


class CategoryView(View):

    def get(self, request, cat_slug):
        """" Страница списка товаров"""
        categories = Category.objects.all()
        # products = Product.objects.filter(available=True)
        # context = {'categories': categories, 'products': products, 'menu': menu, 'title': 'Главная страница'}
        return render(request, "dore/about.html")
        # if request.GET:
        #     print('request.GET:', request.GET)
        # return HttpResponse(f'<h2>Страница CategoryView</h2><p>slug= {cat_slug}</p>')


class ProductView(View):

    def get(self, request):
        """ Страница продукта"""
        products = Product.objects.all()
    #    product = get_object_or_404(Product, id=pk, slug=slug, available=True)
        context = {'products': products}
        return render(request,  'dore/products.html', context)   # "dore/products.html


def about(request):
    return render(request, "dore/about.html")



def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена<h2/>')