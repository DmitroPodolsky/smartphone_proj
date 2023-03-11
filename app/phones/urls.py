from django.urls import path
from . import views
from . import views1
urlpatterns = [
    path('login/', views.ApiLogin.as_view()),
    path('user/', views.get_api),
    path('extra_create/', views.ApiCreate.as_view()),
    path('logout/', views.knox_views.LogoutView.as_view()),
    path('logoutAll/',views.knox_views.LogoutAllView.as_view()),
    path('setpassword/', views.ApiSetPassword.as_view()),
    path('deluser/', views.ApiDelUser.as_view()),
    path('setuser/', views.ApiSetUser.as_view()),
    #path('create/', views1.register, name="register"),
    path('fast_create/', views.ApiCreate_Fast.as_view()),
    path('create/', views1.ApiCreate2.as_view()),
    path('activate/<uidb64>/<token>', views1.activate, name='activate'),
    path('reset/', views1.ApiForgetPssword.as_view()),
    path('reset/<uidb64>/<token>', views1.reset, name='reset')
    ]