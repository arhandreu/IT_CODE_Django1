from django.contrib import admin
from homew.models import Furniture, Client, Category


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'price', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category',)
    list_editable = ('price',)
    list_filter = ('category', 'price',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'privilege')
    list_display_links = ('firstname', 'lastname',)
    list_editable = ('privilege',)
    list_filter = ('privilege',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)


