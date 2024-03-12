"""
URL configuration for finaldgp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('signin',views.SignInView.as_view(),name='login'),
    path('seasonalfruits',views.Seasonalfruits.as_view(),name='sfruits'),
    path('importedfruits',views.Importedfruits.as_view(),name='ifruits'),
    path('tropicalfruits',views.Tropicalfruits.as_view(),name='tfruits'),
    path('dryfruits',views.Dryfruits.as_view(),name='dfruits'),
    path('citrusfruits',views.Citrusfruits.as_view(),name='cfruits'),
    path('berries',views.Berries.as_view(),name='berries'),
    path('melons',views.Melons.as_view(),name='melons'),
    path('leafy',views.Leafy.as_view(),name='leafy'),
    path('root',views.Root.as_view(),name='root'),
    path('pod',views.Pod.as_view(),name='pod'),
    path('indoor',views.Indoor.as_view(),name='indoor'),
    path('cactus',views.Cactus.as_view(),name='cactus'),
    path('medicinal',views.Medicinal.as_view(),name='medicinal'),
    path('fruitplants',views.Fruitplants.as_view(),name='fruitplants'),
    path('ornamental',views.Ornamentalplants.as_view(),name='ornamental'),
    path('flower',views.Floweringplants.as_view(),name='flower'),
    path('fertiliser',views.Organicfertiliser.as_view(),name='fertiliser'),
    path('cocopeat',views.Cocopeat.as_view(),name='cocopeat'),
]

