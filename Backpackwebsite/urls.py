"""
URL configuration for Backpackwebsite project.

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
# website link: https://gbackpack.oceanwp.org/?_gl=1%2A14xe22a%2A_ga%2AMTQ3NTg4MDIyOS4xNzE3OTE1NDMy%2A_ga_LCTYVQKHNC%2AMTcxNzkxNTQzMS4xLjAuMTcxNzkxNTQzMS42MC4wLjA.

from django.contrib import admin
from django.urls import path
from Backpackwebsite import settings
from webApp import views
from django.conf.urls.static import static  


admin.site.site_header = 'Backpack website'                    # default: "Django Administration"
admin.site.index_title = 'Madhav"s Website'                 # default: "Site administration"
admin.site.site_title = 'Madhav"s Website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop', views.shop),
    path('blog', views.blog),
    path('account', views.account),
    path('contact', views.contact),
    path('cart', views.cart),
    path('signup', views.signup),
    path('data', views.data),
    path('register', views.register),
    path('logincheck', views.logincheck),
    path('cartitem', views.cartitem),
    path('deletecart', views.deletecart),
    path('increment', views.increment),
    path('decriment', views.decriment),
    path('logout', views.logout),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  