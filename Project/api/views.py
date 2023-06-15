from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .tasks import process_csv
from django.conf import settings
import os

@api_view(['POST'])
@csrf_exempt
def schedule_file_processing(request):
    if request.method == "POST":
        file = request.FILES["file"]
        output_file = os.path.join(settings.MEDIA_ROOT, f'output_{file.name}')
        # Write uploaded file to disk
        input_file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(input_file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        # Pass the path of the saved file to the task
        task = process_csv.delay(input_file_path, output_file)
        return JsonResponse({"task_id": str(task.id)}, status=202)
    return JsonResponse({"detail": "Invalid method"}, status=400)


@api_view(['GET'])
def download_result(request, task_id):
    task = process_csv.AsyncResult(task_id)
    if task.ready():
        filename = task.get()
        with open(filename, 'r') as file:
            response = HttpResponse(file.read(), content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    else:
        return JsonResponse({'error': 'File is still being processed. Please wait.'})
