from xml.etree.ElementInclude import include

from django.urls import path
from . import views
urlpatterns = [
    path('createPho/', views.Phones_comments_APP.as_view()),
    path('operatePho/<int:pk>/', views.Phones_comments_APP.as_view()),
    path('createAir/', views.AirPods_comments_APP.as_view()),
    path('operateAir/<int:pk>/', views.AirPods_comments_APP.as_view()),
    path('add_product/',views.Bascet_products_APP.as_view()),
    path('operate_product/<int:pk>/',views.Bascet_products_APP.as_view()),
    path('not_aut_add_product/',views.Bascet_products_not_aut_APP.as_view()),
    path('not_aut_get_product/<int:pk>/',views.Bascet_products_not_aut_APP.as_view()),
    path('not_aut_del_product/<int:pk>/<int:pk1>/',views.Bascet_products_not_aut_APP.as_view())
    ]