from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from .models import *

class CategoryAdmin(TranslationAdmin):
    #list_display = ('name',)
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Picture)
admin.site.register(Article)
admin.site.register(ArticlePicture)
admin.site.register(Page)
admin.site.register(Oders)
admin.site.register(OrderProducts)


# Register your models here.
