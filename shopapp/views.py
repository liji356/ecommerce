from django.shortcuts import render,get_object_or_404
from.models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


##To SHOW  All product ##
#CATEGORY PART #
def productcategory(request,slug_c=None):
    c_page=None
    products_list=None
    if slug_c!=None:
        c_page=get_object_or_404(Category,slug=slug_c)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
##PAGENATOR CODE##
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        Products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'products':products})
##show product detalis one bye one:####
#c_slug,product_slug##:Two varibale for category and product
def productdetalis(request,slug_c,product_slug):
    try:
        product=Product.objects.get(category__slug=slug_c,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})        

# Create your views here.
##SEARCH ITEM###


