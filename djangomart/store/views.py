from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
#from cart.models import CartItem
from django.db.models import Q

#from cart.views import _cart_id
from django.core.paginator import Paginator # this for paginations


def store(request, category_slug=None):
    categories = Category.objects.all()
    products = None  # product initially nao thakte pare

    if category_slug != None: # jodi page ar specific category thake.
        category= get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        
        paginator = Paginator(products, 1) # (products, 1) = product golo k koita page a dakhate chai.
        page = request.GET.get('page') #currently koita page a ace.
        paged_products = paginator.get_page(page) 
        
        product_count = products.count() 
    else: # jodi page ar specific category na thake.
        products = Product.objects.all().filter(is_available=True)
        
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()

    context = {
        'products': paged_products,
        'p_count': product_count,
    }
    return render(request, 'store/store.html', {'products':products,'p_count':product_count, 'categories': categories})


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #category__slug= Product ar sathe category ar akta somporkho acc ,,many to one tai double(__) user kora hoyasa.
#         in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
         raise e

    context = {
         'single_product': single_product,
#         'in_cart'       : in_cart,
     }
    return render(request, 'store/product_details.html', context)


def search(request): # this is for searching.
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count() # Q= when use multiple logical filter in model we will ues Q. and icontains= case insensetive
    context = {
        'products': products,
        'p_count': product_count,
    }
    return render(request, 'store/store.html', context)

