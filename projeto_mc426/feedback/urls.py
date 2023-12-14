from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.index, name='feedback'),
    path('<int:feedback_id>/', views.detail, name='detail'),
    path('list/', views.list, name='list'),
    path('<int:feedback_id>/answer', views.answer, name='answer'),
]
