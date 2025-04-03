from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'web/index.html')


def portfolio_view(request):
    return render(request, 'web/portfolio.html')


def services_view(request):
    return render(request, 'web/services.html')
