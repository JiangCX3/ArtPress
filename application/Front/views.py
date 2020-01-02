from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'Front/index.html')


def post(request):
    return render(request, 'Front/post.html')


def search(request):
    return render(request, 'search.html')


def tags(request):
    return render(request, 'tags.html')


def artists(request):
    return render(request, 'artists.html')
