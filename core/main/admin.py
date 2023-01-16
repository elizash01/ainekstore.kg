from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductColor, ProductSize, Vacancies


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_slug', 'category_description')
    list_display_links = ('id', 'category_name')
    prepopulated_fields = {'category_slug': ('category_name',)}
    search_fields = ('category_name', 'category_description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_description', 'prod_color', 'prod_size', 'image', 'prod_slug' )
    list_display_links = ('id', 'name')
    prepopulated_fields = {'prod_slug': ('name')}
    ordering = ('name', 'prod_color', 'prod_size', )
    
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'width', 'length', 'thickness', )
    list_display_links = ('id', 'width', 'length', 'thickness')


class ProducrColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color_name','color_slug', )   
    list_display_links =  ('id', 'color_name')
    prepopulated_fields = {'color_slug': ('color_name')} 
      

class VacanciesAdmin(admin.ModelAdmin):
    list_display =  ('id', 'vacancy_name', 'salary', 'description', 'vac_slug')  
    list_display_links = ('vacancy_name', 'salary')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSize), ProductSizeAdmin
admin.site.register(ProductColor, ProductColor)
admin.site.register(Vacancies, VacanciesAdmin)