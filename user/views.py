from django.http.response import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import User, UserDetails
from django.contrib import messages


def index(request,username):
    user = get_object_or_404(User,username=username)
    return render(request,"index.html",{"user": user})


def validate_user_api(request):
    if request.method == "POST":
        username = None
        email = None
        if username:
            if User.objects.filter(username=username).exists():
                return JsonResponse({"message":"username alreday taken"},status=400)
        if email:
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"email alreday taken"},status=400)
        if not any([username,email]):
            return JsonResponse({"message":f"invalid body"},status=400)
        else:
            return JsonResponse({"message":f"{(username or email)} available"},status=200)
    else:
        return JsonResponse({"message":"method not allowed"},status=405)


def add_user(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            short_name = request.POST.get('short_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password != confirm_password:
                messages.error("password and confirm password should be match")
                return redirect(reverse("add-user"))

            user = User.objects.create_user(username=username,full_name=full_name,email=email,password=password,is_staff=True)
            return redirect(reverse("index",args=username))
        else:
            return render(request,"add-user.html")
    except Exception as e:
        messages.error(request,f"{e}")
        return render(request,"add-user.html")
        