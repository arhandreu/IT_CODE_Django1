
from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture


def date_now(request):
    list_furniture = Furniture.objects.all()
    for item in list_furniture:
        print(item.image)
    return render(request, "homew/index.html", {"furniture": list_furniture, "title": "Список мебели"})
