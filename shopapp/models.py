from django.db import models
from django.urls import reverse

##FRIST TABLE###
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta():
        ordering=('name'),
        verbose_name='category'
        verbose_name_plural='categories'
#get_url function3
    def get_url(self):
        return reverse('shopapp:product_by_category',args=[self.slug])

####product_by_category:name of urls ####

    ##second Table##
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product')
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    

    #get url for product 
    def get_url(self):
        return reverse('shopapp:productdetalis',args=[self.category.slug,self.slug])
    


    class Meta():
        ordering=('name'),
        verbose_name='product'
        verbose_name_plural='products'



   


    def __str__(self):
        return '{}'.format(self.name)


# Create your models here.
