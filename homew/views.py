from django.db.models import Count
from django.views.generic import (TemplateView, ListView, DetailView,
                                  RedirectView)

from .models import Furniture, Category


# def index(request):
#     list_furniture = Furniture.objects.all()
#     list_categories = Category.objects.annotate(
#     num_furniture=Count('furniture'))
#     context = {"furniture": list_furniture,
#                "title": "Список мебели",
#                "categories": list_categories, }
#
#     return render(request, "homew/index.html", context)


class HomePage(ListView):
    template_name = 'homew/index.html'
    model = Furniture
    context_object_name = 'furniture'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        list_categories = Category.objects.annotate(
            num_furniture=Count('furniture'))

        context["categories"] = list_categories
        context["title"] = "Список мебели"

        return context


# def get_category(request, pk):
#     list_furniture = Furniture.objects.filter(category=pk)
#     list_categories = Category.objects.annotate(
#     num_furniture=Count('furniture'))
#     category = Category.objects.get(pk=pk)
#     context = {"furniture": list_furniture,
#                "title": "Список мебели",
#                "categories": list_categories,
#                "category": category, }
#
#     return render(request, "homew/category.html", context)


class DetailCategory(DetailView):
    template_name = 'homew/category.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        list_furniture = Furniture.objects.filter(category=context['category'])
        list_categories = Category.objects.annotate(num_furniture=Count('furniture'))

        context["furniture"] = list_furniture
        context["title"] = "Список мебели"
        context["categories"] = list_categories

        return context


class SearchMagazine(RedirectView):
    query_string = True
    url = 'https://yandex.ru/maps/172/ufa/category/furniture_store/184107871/'


class About(TemplateView):
    template_name = 'homew/about.html'
