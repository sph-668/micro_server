from django.urls import path
from . import views

urlpatterns = [
    path('lk_student_sent/', views.lk_student_sent, name='lk_student_sent'),
    path('', views.lk_student_active, name='lk_student_active'),
    path("signup/", views.signup, name="signup"),
    path('presave/', views.presave, name='presave'),
    path('getusername/', views.getusername, name='getusername'),
    path('save_1/', views.save_1, name='save_1'),
    path('save_2/', views.save_2, name='save_2'),
    path('save_3/', views.save_3, name='save_3'),
    path('save_4/', views.save_4, name='save_4'),
    path('save_5/', views.save_5, name='save_5'),
    path("signup_/", views.signup, name="signup"),
    path('signin/', views.signin, name='signin'),
    path('create_lab/', views.create_lab, name='create_lab'),
    path('load/', views.load, name='load'),

]