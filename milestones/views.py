import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Milestone


@csrf_exempt
def milestone_collection_view(request):
    """
    Handles:
    - POST /api/milestones/ -> US-01: Create Milestone
    - GET  /api/milestones/ -> US-02: List all Milestones
    """
    if request.method == 'GET':
        milestones = Milestone.objects.all().order_by('-created_at')
        data = [
            {
                "id": m.id,
                "title": m.title,
                "description": m.description,
                "student_id": m.student_id,
                "status": m.status,
                "created_at": m.created_at.isoformat(),
            }
            for m in milestones
        ]
        return JsonResponse({"milestones": data, "count": len(data)}, status=200)

    elif request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (ValueError, TypeError):
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)

        title = payload.get('title')
        description = payload.get('description', '')
        student_id = payload.get('student_id')

        # Validation per Acceptance Criteria
        if not title or not student_id:
            return JsonResponse(
                {"error": "Both 'title' and 'student_id' are required fields."},
                status=400,
            )

        milestone = Milestone.objects.create(
            title=title.strip(),
            description=description.strip(),
            student_id=student_id.strip(),
            status='PENDING'
        )

        return JsonResponse(
            {
                "message": "Milestone created successfully",
                "id": milestone.id,
                "title": milestone.title,
                "description": milestone.description,
                "student_id": milestone.student_id,
                "status": milestone.status,
                "created_at": milestone.created_at.isoformat(),
            },
            status=201
        )

    return JsonResponse({"error": f"Method {request.method} not allowed"}, status=405)