from django.urls import path
from Home.views import Home, Login, Logout, Profile, Signup

urlpatterns = [
    path('', Home, name='Home'),
    path('login/', Login),
    path('logout/', Logout),
    path('signup/', Signup),
    path('profile/likes/', Profile),
]