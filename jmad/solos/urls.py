from django.urls import path
from solos.views import index

urlpatterns = [
    path('', index.as_view()),
]
