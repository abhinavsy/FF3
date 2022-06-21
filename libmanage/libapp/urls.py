from django.urls import path,include

from . import views
app_name='libapp'

urlpatterns = [

    path('',views.allbook,name='allbook'),

]