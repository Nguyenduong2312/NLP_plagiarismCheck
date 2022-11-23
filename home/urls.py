from django.urls import path
from . import views

urlpatterns = [
   path('', views.get_input, name="home"),
   path('chooseWeb/', views.chooseWeb, name="choose web"),
   path('cmp1/',views.cmp1,name ="cmp"),
   path('cmp2/',views.cmp2,name ="cmp"),
   path('cmp3/',views.cmp3,name ="cmp"),
   path('cmp4/',views.cmp4,name ="cmp"),
   path('cmp5/',views.cmp5,name ="cmp"),


]