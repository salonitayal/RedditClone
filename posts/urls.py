from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/upvote', views.upvote, name='upvote'),    
    path('<int:pk>/downvote', views.downvote, name='downvote'), 
]
