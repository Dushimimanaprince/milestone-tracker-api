from django.urls import path
from .views import milestone_collection_view

urlpatterns = [
    path('api/milestones/', milestone_collection_view, name='milestone-collection'),
]