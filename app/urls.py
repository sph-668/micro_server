from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial, name='initial'),
    path('signup/', views.signup, name='signup'),
    path('presave/', views.presave, name='presave'),
    path('getusername/', views.getusername, name='getusername'),
    path('signin/', views.signin, name='signin'),
    path('createlab/', views.createlab, name='createlab'),
    path('load/', views.load, name='load'),
    #path('check_dict/', views.check_dict, name='check_dict'),
    path('getpresavedlabs/', views.getpresavedlabs, name='getpresavedlabs'),
    path('save/', views.save, name='save'),
    path('getsavedlabs/', views.getsavedlabs, name='getsavedlabs'),
    path('getnumberedlabtocheck/', views.getnumberedlabtocheck, name='getnumberedlabtocheck'),
    path('getcheckednumberedlab/', views.getcheckednumberedlab, name='getcheckednumberedlab'),
    path('getlabtocheck/', views.getlabtocheck, name='getlabtocheck'),
    path('getcheckedlab/', views.getcheckedlab, name='getcheckedlab'),
    path('setscore/', views.setscore, name='setscore'),


]