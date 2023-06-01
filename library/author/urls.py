from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.author_list),
    path('authors/<int:author_id>/', views.author_item, name='author_item'),
    path('update/<int:author_id>/', views.create_author_new, name='author_update'),
    path('delete/<int:author_id>/', views.delete, name='author_delete'),

]
