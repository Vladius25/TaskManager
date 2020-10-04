from rest_framework import generics
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer, HistoricalTaskSerializer


class GetHistoryView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        records = instance.history.all()
        history = HistoricalTaskSerializer(records, many=True)
        return Response(history.data)
