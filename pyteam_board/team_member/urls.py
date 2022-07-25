from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /team_member/5/
    path('<int:person_id>/', views.detail, name='detail'),
    # ex: /team_member/5/experience/
    path('<int:person_id>/results/', views.experience, name='experience'),
   
]