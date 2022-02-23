from django.contrib import admin
from .models import *


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class PoetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id_id', 'info_id_id')
    list_display_links = ('id', 'name')


class PoemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'poet_id_id')
    list_display_links = ('id', 'name')


class InformationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'info_id', 'info')
    list_display_links = ('id', 'info')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Poets, PoetsAdmin)
admin.site.register(Poems, PoemsAdmin)
admin.site.register(Informations, InformationsAdmin)
