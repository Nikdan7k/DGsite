from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('alltext/', views.alltext, name='alltext'),
    path('post_new/one', views.form_one, name='post_new_one'),
    path('post_new/two', views.form_two, name='post_new_two')
]