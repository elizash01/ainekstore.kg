from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории', max_length=100)
    category_description = models.TextField(max_length=200, verbose_name='Описание')
    category_slug = models.SlugField(max_length=100, unique=True)
    create_ad = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' 


class ProductSize(models.Model):
    width = models.DecimalField(max_digits=10, decimal_places=5, verbose_name='Ширина')
    length = models.DecimalField(max_digits=10, decimal_places=5, verbose_name='Длина')
    thickness = models.DecimalField(max_digits=10, decimal_places=5, verbose_name='Толщина')


    # def __str__(self):
    #     return  self.width

    # def __str__(self):
    #     return self.name

    # def __str__(self):
    #     return self.thickness

    class Meta:
        verbose_name = 'Размер товара'
        verbose_name_plural = 'Размеры товара' 

class ProductColor(models.Model):
    color_name = models.CharField(max_length=100, verbose_name='Название цвета')
    color_slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цвета товара'    


class Product(models.Model):
    name = models.CharField(max_length=147, verbose_name='Название товара')
    product_description = models.TextField()
    prod_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    prod_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    prod_slug = models.SlugField(max_length=120, unique=True)       

    def __str__(self):
        return self.name
    


class Vacancies(models.Model):
    vacancy_name = models.CharField(max_length=147, verbose_name='Должность')
    salary = models.IntegerField(default=0, verbose_name='Зарплата')
    description = models.TextField()
    vac_slug = models.SlugField(max_length=120, unique=True)

    def str(self) -> str:
        return f'{self.name_vacanc} , {self.salary}'
