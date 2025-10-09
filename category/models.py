from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.TextField(unique=True) # slug is URL
    description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(upload_to="photos/categories",blank=True)

 

    def __str__(self):
        return self.category_name

    class Meta: 
        verbose_name = "category"
        verbose_name_plural = "categories"