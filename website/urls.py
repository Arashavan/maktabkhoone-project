from django.urls import path
from .views import index_view, portfolio_view, services_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('home/', index_view, name='index'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('services/', services_view, name='services')
]
