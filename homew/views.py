from django.db.models import Count
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import (TemplateView, ListView, DetailView,
                                  RedirectView)
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import filters, forms
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


def page_not_found(request, exception):
    # return HttpResponseNotFound("<h1> Такой страницы не существует! </h1>")
    return redirect("home")


class HomePage(ListView):
    template_name = 'homew/index.html'
    model = Furniture
    context_object_name = 'furniture'

    def get_filters(self):
        return filters.Furniture(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs.select_related('category')

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

        list_furniture = Furniture.objects.filter(category=context['category']).select_related('category')
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

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request):
        qs = Client.objects.all()
        serializer = serializers.Client(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Client(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, pk):
        instance = self.get_object(pk)

        serializer = serializers.Client(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response({'put': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientModelViewPagination(PageNumberPagination):
    page_size = 2
    page_size_query_params = 'page_size'
    max_page_size = 5


class ClientModelView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.Client
    pagination_class = ClientModelViewPagination


def show_furniture(request, slug):
    furniture = get_object_or_404(Furniture, slug=slug)
    context = {'furniture': furniture,
               }

    return render(request, 'homew/furniture.html', context)


def add_client(request):
    if request.method == "POST":
        form = forms.AddClientForm(request.POST)
        if form.is_valid():
            try:
                Client.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка при добавлении поста")
    else:
        form = forms.AddClientForm()

    context = {'title': "Добавление клиента",
               'form': form,
               }
    return render(request, 'homew/addClient.html', context)
