from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from .models import ModelFile


# Create your views here.

class ModelUrlView(View):
    def post(self, request: HttpRequest):
        project_slug = request.POST.get("project_slug")
        model_slug = request.POST.get("model_slug")
        version = request.POST.get("version")
        mf = ModelFile.objects.filter(
            model_file__project__slug=project_slug,
            model_file__slug=model_slug,
            version=version
        ).first()
        if mf:
            return JsonResponse({"url": mf.file.url}, status=200)
        else:
            return JsonResponse({"msg": "未找到该模型"}, status=404)
