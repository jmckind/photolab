from django.shortcuts import render

def index(request):
    context = {'message': 'OK'}
    return render(request, 'index.html', context)
