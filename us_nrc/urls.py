from django.urls import path
from us_nrc.views import reactor_state
from us_nrc.views import reactor_name,read_data

urlpatterns = [
    # path('',read_data.index),
    path(r'search/',reactor_name.reactorName.as_view()),
    path(r'state/',reactor_state.reactorState.as_view()),
]

