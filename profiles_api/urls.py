from django.urls import path
from .views import HelloAPIView 


urlpatterns = [
    path('HelloAPIView/', HelloAPIView.as_view()),
]
