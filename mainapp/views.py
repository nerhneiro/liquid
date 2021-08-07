from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')

def shoppers(request):
    return render(request, 'shoppers.html')

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')