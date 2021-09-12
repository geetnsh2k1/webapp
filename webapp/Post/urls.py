from django.urls import path
from Post.views import Like, Unlike, Add

urlpatterns = [
    path('like/<str:id>/', Like),
    path('unlike/<str:id>/', Unlike),
    path('add/', Add),
]