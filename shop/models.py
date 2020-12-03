from django.db import models

# Product Sections
class Color(models.Model):
    color_name=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.color_name

class SuperCategory(models.Model):
    superCategory_name=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.superCategory_name

class Category(models.Model):
    category_name=models.CharField(max_length=30,default="")
    superCategory_name=models.ForeignKey(
        'SuperCategory',
        on_delete=models.SET_DEFAULT,
        default=""
        )


    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    product_category=models.ForeignKey(
        'Category',
        on_delete=models.SET_DEFAULT,
        default=""
        )
    product_description=models.TextField(max_length=2000,default="")
    product_price=models.IntegerField(default=0)
    product_quantity=models.IntegerField(default=0)
    product_color=models.ForeignKey(
        'Color',
        on_delete=models.SET_DEFAULT,
        default=""
    )
    product_image=models.ImageField(upload_to='shop/images',default="")
    product_date=models.DateField(default="")

    def __str__(self):
        return self.product_name
