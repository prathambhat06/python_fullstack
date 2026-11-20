from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
    path('student-form/', views.student_form, name='student_form'),
    path('student-list/', views.student_list, name='student_list'),
]