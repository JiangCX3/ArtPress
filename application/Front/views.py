from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')


def test1(request):
    return render(request, 'test1.html')
