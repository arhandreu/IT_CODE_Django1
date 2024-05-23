import django_filters
from homew import models


class Furniture(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название мебели',
                                     lookup_expr='icontains')
    created_at = django_filters.DateFilter(label='Создана после',
                                           lookup_expr='gt')
    price = django_filters.RangeFilter(label='Цена от и до')

    class Meta:
        model = models.Furniture
        exclude = ('image', )
