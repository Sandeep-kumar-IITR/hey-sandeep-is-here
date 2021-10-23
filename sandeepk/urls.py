from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('random_picker/', views.random_p),
    path('random_picker/picker/',views.random_done),
    path('stone-paper/',views.stone_paper),
    path('stone-paper/gamer-choice/',views.gamer_choice),
    path('love-calculator/', views.love_calculator)





]