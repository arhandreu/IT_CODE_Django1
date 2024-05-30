import datetime

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from homew.models import Furniture, Client, Category, NavBar, Order


class OrderInlineFromSet(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('date_delivery', datetime.date(2000, 1, 1)) < datetime.datetime.now().date():
                raise ValidationError('Неверная дата доставки')

        return super().clean()


class ClientInline(admin.TabularInline):
    model = Order
    extra = 2
    formset = OrderInlineFromSet


class FurnitureInline(admin.StackedInline):
    model = Order
    extra = 2
    formset = OrderInlineFromSet


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'price', 'category',)
    list_display_links = ('name',)
    search_fields = ('name__startswith', 'category__name',)
    list_editable = ('price',)
    list_filter = ('category', 'price',)
    inlines = [
        ClientInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'privilege',)
    list_display_links = ('firstname', 'lastname',)
    list_editable = ('privilege',)
    list_filter = ('privilege',)
    inlines = [
        FurnitureInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):

    list_display = ('client', 'furniture', 'count', 'sum_order', 'date_delivery', 'status')
    ordering = ('date_delivery',)
    actions = ('set_status',)

    @admin.display(description="Сумма заказа", ordering='count')
    def sum_order(self, order: Order):
        return order.count*order.furniture.price

    @admin.action(description="Изменить статус на 'Доставлено'")
    def set_status(self, request, queryset):
        queryset.update(status=True)


admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NavBar)
admin.site.register(Order, OrderAdmin)

