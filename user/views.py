from django.shortcuts import render, get_object_or_404
from .models import User


def index(request,username):
    user = get_object_or_404(User,username=username)
    return render(request,"index.html",{"user": user})