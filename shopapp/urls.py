from.import views
from django.urls import path
app_name='shopapp'
#app_name='searchapp'

urlpatterns = [
    path('',views.productcategory,name='productcategory'),
    path('<slug:slug_c>/',views.productcategory,name='product_by_category'),
    path('<slug:slug_c>/<slug:product_slug>/',views.productdetalis,name='productdetalis'),
    #SEARCH PATH #
    #path('serach/' ,views.SearchRes,name='SearchRes'),
 
]