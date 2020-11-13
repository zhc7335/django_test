# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse("<h1>🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟</h1>")
    # context = {'title': '图书列表', 'list': range(10)}
    # return render(request, 'book_app/index.html', context)
    list = BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'book_app/index2.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'book_app/detail.html', context)
