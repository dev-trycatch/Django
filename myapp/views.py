from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def receipe(request):
    if request.method == "POST":
        data = request.POST
        # print(data['rec_name'])
        # print(data.get('rec_name'))
        # rec_name = data['rec_name']
        # rec_desc = data['rec_desc']
        rec_name = data.get('rec_name')
        rec_desc =  data.get('rec_desc')
        rec_images = request.FILES.get('rec_images')
        # print(rec_name)
        # print(rec_desc)
        # print(rec_images)
        Receipe.objects.create(
            rec_name = rec_name,
            rec_desc = rec_desc,
            rec_images = rec_images,
        )
        return redirect('/receipe/')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(rec_name__icontains = request.GET.get('search'))

    context = {'recipes':queryset}
    return render(request , 'receipes.html' ,context)

def update_recipe(request , id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        rec_name = data.get('rec_name')
        rec_desc = data.get('rec_desc')
        rec_images = request.FILES.get('rec_images')

        queryset.rec_name = rec_name
        queryset.rec_desc = rec_desc

        if rec_images:
            queryset.rec_images = rec_images

        queryset.save()
        return redirect('/receipe/')

    context = {'recipes':queryset}
    return render(request , 'update_recipe.html', context)

def delete_recipe(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login/')

        user  = authenticate(username = username,password = password)
        if user is None:
            messages.info(request, "Invalid password.")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipe/')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created Successfully!!!")
        return redirect('/register/')
    return render(request,'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')