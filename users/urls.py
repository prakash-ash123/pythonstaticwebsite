
from django.urls import path
from . import views


urlpatterns = [
   path('signin_user',views.signin_user, name="signin"),
   path('signup_user',views.signup_user, name="signup"),
   path('signout_user',views.signout_user, name="signout")

]