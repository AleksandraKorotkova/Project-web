from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('skaters', views.SkatersListView.as_view(), name='skaters'),
    path('skaters/<int:pk>', views.SkatersDetailView.as_view(), name='skaters-detail'),
    path('trainers', views.TrainersListView.as_view(), name='trainers'),
    path('trainers/<int:pk>', views.TrainersDetailView.as_view(), name='trainers-detail'),
    path('elements', views.ElementsListView.as_view(), name='elements'),
    path('elements/<int:pk>', views.ElementsDetailView.as_view(), name='elements-detail'),
]