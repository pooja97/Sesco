from django.urls import path
from us_nrc.data import read_data
from us_nrc.views import reactor_state
from .views import reactor_name,outage_list,outage_date_range,outage_date

urlpatterns = [
    # path('',read_data.index,name="index"),
    path(r'date_range/',outage_date_range.ReactorOutageDetails.as_view()),
    path(r'reactor_outage/',outage_list.ReactorOutageView.as_view()),
    path(r'search/',reactor_name.reactorName.as_view()),
    path(r'state/',reactor_state.reactorState.as_view()),
    path(r'outage_date/',outage_date.ReactorOutageDate.as_view()),
]

