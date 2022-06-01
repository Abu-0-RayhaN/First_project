

from django.urls import path
from.import views
urlpatterns = [
    path('',views.authlogin,name='login'),
    path('registration',views.authregistration,name='registration'),
    path('forgot-password',views.forgotpassword,name='forgotpassword'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.userlogout,name='logout'),

]