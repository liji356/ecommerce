from django.urls import path,include
from.import views
app_name='cart'

urlpatterns = [
   path('',views.cart_detail,name='cart_detail'),
   
   path('add/<int:product_id>/',views.addcart,name='addcart'),
   path('remove/<int:product_id>/',views.cart_remove,name="cart_remove"),
   path('remove/<int:product_id>/',views.remove,name="remove"),
 

]