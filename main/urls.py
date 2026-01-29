from django.urls import path, include
from main.views import landing_page


urlpatterns = [
    path('', landing_page, name='landing_page'),
]