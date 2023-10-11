from django.db import models
from django.urls import reverse
from shopapp.models import Product

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)

        
    def get_url(self):
        return reverse('shopapp:productdetalis',args=[self.category.slug,self.slug])


    class Meta():
        db_table='Cart'
        ordering=['date']

    def __str__(self):
        return '{}'.format(self.cart_id) 

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    Active=models.BooleanField(default=True)

    

   

    class Meta():
        db_table='CartItem'
        
    def sub_total(self):
        return self.product.price * self.quantity
    


    def __str__(self):
        return '{}'.format(self.product) 




    
       




# Create your models here.
