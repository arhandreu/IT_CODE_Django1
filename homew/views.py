from django.db.models import Count
from django.views.generic import (TemplateView, ListView, DetailView,
                                  RedirectView)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import filters
from .models import Furniture, Category, Client
from . import serializers

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

    def get_filters(self):
        return filters.Furniture(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        list_categories = Category.objects.annotate(
            num_furniture=Count('furniture'))

        context["categories"] = list_categories
        context["title"] = "Список мебели"
        context['filters'] = self.get_filters()

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
        list_categories = Category.objects.annotate(
            num_furniture=Count('furniture'))

        context["furniture"] = list_furniture
        context["title"] = "Список мебели"
        context["categories"] = list_categories

        return context


class SearchMagazine(RedirectView):
    query_string = True
    url = 'https://yandex.ru/maps/172/ufa/category/furniture_store/184107871/'


class About(TemplateView):
    template_name = 'homew/about.html'


class ClientAPIView(APIView):
    def get(self, request):
        qs = Client.objects.all()
        serializer = serializers.Client(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Client(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Yea'})


class ClientModelView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.Client

