from django.contrib.auth.hashers import make_password, check_password
import email
from django.shortcuts import redirect, render
from . models import Product
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def product(request):
    data = Product.objects.all()
    return render(request, "product.html", {'data':data})

def add(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        description = request.POST['description']
        selling_price = request.POST['selling_price']
        mrp = request.POST['mrp']
        productimage = request.FILES['file']

        details = Product(product_name=product_name,description=description,selling_price=selling_price,mrp=mrp,image=productimage)
        details.save()

        return redirect(product_list)

def product_list(request):
    data = Product.objects.all()
    print("data", data)
    return render(request, "product_list.html",{'data':data})
        
def delete(request, id):
    b = Product.objects.get(id=id)
    b.delete()
    return redirect(product_list)

def add_product(request):
    return render(request,"add.html")

def edit(request,id):
    data = Product.objects.get(id = id)
    return render(request,"add.html",{'data':data})

def update(request):
    id = request.POST['id']
    data = Product.objects.get(id = id)
    data.product_name = request.POST['product_name']
    data.description = request.POST['description']
    data.selling_price = request.POST['selling_price']
    data.mrp = request.POST['mrp']
    data.productimage = request.FILES['file']
    data.save()
    return redirect(product_list)