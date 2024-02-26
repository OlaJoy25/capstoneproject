from django.shortcuts import render

from django.http import HttpResponse

posts =[
    {
        'author': 'Sarah Kojo',
        'title': 'Content Post1',
        'content': 'This is my first post',
        'date_posted': '18th February,2024'

    },
    {
        'author': 'Binta Jallo',
        'title': 'Content Post2',
        'content': 'This is my second post',
        'date_posted': '20th February,2024',


    }
]
def home(request):
    context = {
        'posts': posts

    }
    return render(request, 'web/home.html', context)


def about(request):
    return render(request, 'web/about.html', {'title': "About Haven"})
