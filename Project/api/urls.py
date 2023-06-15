from django.urls import path
from .views import schedule_file_processing, download_result

urlpatterns = [
    path('upload/', schedule_file_processing, name='upload'),
    path('download/<str:task_id>/', download_result, name='download'),
]
