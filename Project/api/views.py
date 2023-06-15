from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .tasks import process_csv

@api_view(['POST'])
@csrf_exempt
def schedule_file_processing(request):
    file = request.FILES['file']
    output_file = 'output_' + file.name
    task = process_csv.delay(file.temporary_file_path(), output_file)
    return JsonResponse({'task_id': str(task.id)})


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
