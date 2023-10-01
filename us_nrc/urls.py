from django.urls import path
from us_nrc.data import read_data
from us_nrc.views import reactor_state
from .views import reactor_name,outage_list,outage_date_range,outage_date

urlpatterns = [
    # path('',read_data.index,name="index"),
    path(r'outage_date_search/',outage_date.ReactorOutageDate.as_view()),
    path(r'date_range_search/',outage_date_range.ReactorOutageDetails.as_view()),
    path(r'reactor_outage_list/',outage_list.ReactorOutageView.as_view()),
    path(r'reactor_search/',reactor_name.reactorName.as_view()),
    path(r'state_search/',reactor_state.reactorState.as_view()),
]

