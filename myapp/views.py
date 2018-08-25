from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings

def email_send(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ti1230221@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'mail.html')
@login_required(login_url='/myapp/login')
def mail2(request):
    return render(request,'mail.html')

def home(request):
    return render(request,'index.html')
def home_login(request):
    return render(request,'sample.html')

def register(request):
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            emailid=form.cleaned_data['email']
            first=form.cleaned_data['first_name']
            last=form.cleaned_data['last_name']
            passw=form.cleaned_data['password']

            User.objects.create_user(username=name,email=emailid,first_name=first,last_name=last,password=passw)
            messages.success(request,"user registration successfully")
            return HttpResponseRedirect('/myapp/index21/')
    else:
        form=user_form()
    return render(request,'registration.html',{"form":form})

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        passw = request.POST['password']

        try:
            username = auth.authenticate(username=user_name, password=passw)
            if username is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/myapp/loggedin/')
            else:
                messages.error(request, "invalid")
        except:
            messages.error(request, "welcome")

    return render(request, 'index21.html')


def logout(request):
   return render(request, 'index.html')

def product(request,id):
    product=Product.objects.get(id=id)
    if(request.method=='POST'):
        form=Cart_form(request.POST)
        q=request.POST['quantity']
        if(form.is_valid()):
            f=form.save(commit=False)
            f.user=request.user
            f.product=product
            f.quantity=q
            f.total_price=float(product.price)*float(q)
            f.save()
            return HttpResponseRedirect('/myapp/cart/')
    else:
        form=Cart_form()
    return render(request,'products.html',{
        "detail":product,
        "form":form
    })



@login_required(login_url='/myapp/login')
def cart(request):
    all=Cart.objects.filter(user=request.user)
    total=[]
    for i in all:
        total.append(i.total_price)
    return render(request,'cart.html',{
        "all":all,
        "total": sum(total)
    })
@login_required(login_url='/myapp/login/')
def checkout(request):
    all = Cart.objects.filter(user=request.user)
    total = []
    for i in all:
        total.append(i.total_price)
    if(request.method=='POST'):
        form=Checkout_form(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            messages.success(request,"User Details Inserted Sucessfully")
            return HttpResponseRedirect('/')
        else:
            messages.error(request,"Invalid form")
    else:
        form=Checkout_form()
    return render(request,'checkout.html',{"form":form,
                                           "all": all,
                                           "total": sum(total)
                                           })



def single(request):
    return render(request,'furniture.html')


def shop(request):
    cat=Categories.objects.all()
    default='Mobile'
    all_items=Product.objects.filter(category__name=default)
    return render(request,'furniture.html',{
        "cat":cat,
        "all_items":all_items,
    })

def shop2(request,cat_name):
    cat=Categories.objects.all()
    default='Mobile'
    all_items=Product.objects.filter(category__name=cat_name)
    return render(request,'furniture.html',{
        "cat":cat,
        "all_items":all_items,
    })

def home(request):
    data1=newarrival.objects.all()
    context = {
            'Data1':data1
        }

    return render(request,'index.html',context)

def home3(request):
    data2=newarrival.objects.all()
    context = {
            'Data1':data2
        }

    return render(request,'sample.html',context)


@login_required(login_url='/myapp/login/')
def delete_cart_item(request,item_id):
    match=Cart.objects.get(id=item_id)
    match.delete()
    return HttpResponseRedirect('/myapp/cart/')

def home2(request):
    data=Product.objects.all()
    context = {
        'Data':data
    }
    return render(request,'single.html',context)

def Newarrival(request,id):
    newproduct=newarrival.objects.get(id=id)
    if(request.method=='POST'):
        f=Cart2_form(request.POST)
        q=request.POST['quantity']
        if(f.is_valid()):
            f=f.save(commit=False)
            f.user=request.user
            f.newproduct=newproduct
            f.quantity=q
            f.total_price=float(newproduct.price)*float(q)
            f.save()
            return HttpResponseRedirect('/myapp/cart2/')
    else:
        f=Cart2_form()
    return render(request,'furniture.html',{
        "detail":newproduct,
        "form":f
    })

@login_required(login_url='/myapp/login/')
def cart2(request):
    all=Cart2.objects.filter(user=request.user)
    total=[]
    for i in all:
        total.append(i.total_price)
    return render(request,'cart2.html',{
        "all":all,
        "total": sum(total)
    })

def hacks(request):
    return render(request,'short-codes.html')

def search(request):
    if request.method=='POST':
        s=request.POST['sr']
        if(s):
            match=Product.objects.filter(Q(title__icontains=s)|
                                         Q(description__icontains=s))
            if match:
                return render(request,'search.html',{"sr":match})
            else:
                messages.error(request,"No Result Found")

        else:
            return HttpResponseRedirect('/myapp/search/')
    return render(request,'search.html')