from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.home),
    path('viw/',views.view_data, name='v'),
    path('delete/<int:id>', views.delt),
]
