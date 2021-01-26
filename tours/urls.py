from django.urls import path

from .views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView, name='main'),
    path('departure/<str:departure>/', DepartureView, name='departure'),
    path('tour/<int:id>/', TourView, name='tour')
]
