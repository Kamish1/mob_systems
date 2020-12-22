from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('add', add_movie, name='add_movie'),
    path('graph', display_graph, name='graph'),
    path('collage', collage, name='collage'),
    path('diagram', display_diagram, name='diagram'),
    path('clear_collage', clear_collage, name='clear_collage'),
    path('<str:slug>', MovieDetailView.as_view(), name='detail_movie'),
    path('delete/<str:pk>/', delete_movie, name='delete_movie'),
]
