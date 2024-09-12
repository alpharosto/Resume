from django.urls import path
from .views import ResumeExtractView

urlpatterns = [
    path('', ResumeExtractView.as_view(), name='home'),  # Handle the root URL
    # Other URL patterns
]
