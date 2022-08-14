from turtle import title
from django.shortcuts import render


posts = [
    {
        'name': 'Blog Post 1',
        'author': 'Aditya',
        'content': 'first post contents',
        'date': '01/01/2022',
    },
    {
        'name': 'Blog Post 2',
        'author': 'Tom',
        'content': 'second post contents',
        'date': '02/01/2022',
    },
    {
        'name': 'Blog Post 3',
        'author': 'Dick',
        'content': 'third post contents',
        'date': '01/02/2022',
    },
]

def home(request):
    title = 'Blog-Home'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
    