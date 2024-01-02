from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt  # Disable CSRF for simplicity; use appropriate middleware in production
@require_POST
def file_upload_view(request):
    # Process the uploaded file

    # Assuming successful file upload
    success_message = 'File uploaded successfully.'
    return JsonResponse({'status': 'success', 'message': success_message})
