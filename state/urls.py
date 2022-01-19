from django.urls import path
from . import views

app_name='state'

urlpatterns = [
    path('load-state-data/<str:state_name>', views.load_state_data, name='load-state-data'),
]