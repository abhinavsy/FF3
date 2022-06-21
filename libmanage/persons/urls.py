from django.urls import path

from . import views
app_name='persons'

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.ajax_load_cities, name='ajax_load_cities'),
    path('ajax/load-books/', views.ajax_load_books, name='ajax_load_books'), # AJAX
]