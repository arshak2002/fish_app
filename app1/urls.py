from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name = "home" ),
    path('order/<id>', views.order, name = "order"),
    path('signup/',views.signup, name = "signup" ),
    path('login/',views.login, name = "login" ),
    path('logout/',views.logout, name = "logout" ),
    path('myorder/',views.myorder, name = "myorder" ),
    path('feedback/',views.feedback, name = "feedback" ),
    path('account/',views.account, name = "account" ),
]