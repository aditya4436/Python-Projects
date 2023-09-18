"""
URL configuration for link_the_pipeline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin    #existing 
from django.urls import path    #existing 
from . import views     #changes made in this file

urlpatterns = [
    path('admin/', admin.site.urls),    #existing 
    path('', views.index, name='index'),    #changes made in this file
    path('analyze', views.analyze, name='analyze'),     #changes made in this file
    #path('capfirst', views.capfirst, name='capitalizefirst'),   #changes made in this file
    #path('newlineremove', views.newlineremove, name='newlineremove'),   #changes made in this file
    #path('spaceremover', views.spaceremover, name='spaceremover'),  #changes made in this file
    #path('charcount', views.charcount, name='charcount'),   #changes made in this file
]
