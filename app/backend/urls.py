"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from phones import views1
from phones.views import AirPods_APP, Get_Phone_slug_APP, Phones_APP, Phones_comments_APP, Get_AirPod_slug_APP
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()#создаёт две ссылки на себя с помощью домена и на SimpleRouter()
router1 = routers.DefaultRouter()
router1.register(r'func',AirPods_APP)
router.register(r'func',Phones_APP)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/phones/',include(router.urls)),
    path('api/accounts/',include('phones.urls')),
    path('api/phone/<slug:pk>/',Get_Phone_slug_APP.as_view()),
    path('api/airpod/<slug:pk>/',Get_AirPod_slug_APP.as_view()),
    path('api/comments/',include('phones.urls1')),
    path('api/airpods/',include(router1.urls)),
    path('login/', views1.login, name='login'),
    path('auth/', views1.auth),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", views1.home, name='home'),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )