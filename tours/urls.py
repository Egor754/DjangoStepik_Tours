from django.urls import path

from .views import MainView, DepartureView, \
    TourView, pageNotFound, ServerError

urlpatterns = [
    path('', MainView, name='main'),
    path('departure/<str:departure>/', DepartureView, name='departure'),
    path('tour/<int:id>/', TourView, name='tour')
]

handler404 = pageNotFound
handler500 = ServerError
