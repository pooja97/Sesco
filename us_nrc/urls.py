from django.urls import path
from .views import reactorList

urlpatterns = [
    path('', reactorList.as_view()),
]
