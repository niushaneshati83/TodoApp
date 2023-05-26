from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import task
from .serializers import TodoSerializer

# Create your views here.
class TaskListApiView(APIView):
    def get(self,request):
        tasks = task.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        pass
