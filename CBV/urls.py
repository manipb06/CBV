"""CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.myview, name='func'),
    path('class/',views.MyView.as_view(), name='class'),
    path('class/',views.MyView.as_view(name= 'Mandeep'), name='class'),
    path('cc/',views.MyChildView.as_view(), name='childclass'),
    
    path('home/',views.homefunc, name='home'),
    path('homecl/',views.HomeClassView.as_view(), name='homeclass'),
    path('aboutfun/',views.aboutfunc, name= 'aboutfunc'),
    path('aboutcl/', views.AboutClass.as_view(), name='aboutcl' ),
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.ContactClassView.as_view(), name='contactcl'),
    path('newsfun/', views.newsfun, {'template_name':'news.html'}, name='newsfun'),
    path('newsfun2/', views.newsfun, {'template_name':'news2.html'}, name='newsfun2'),
    path('newscl/', views.NewsClassView.as_view(), name='newscl' ),
]
