from rest_framework import generics
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import HistoricalTaskSerializer, TaskSerializer


class GetCreateTasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        query_params = self.request.query_params.dict()
        conditions = {"status": "status", "from_date": "end_date__gte", "to_date": "end_date__lte"}
        for param_name in conditions.keys():
            if param_name in query_params:
                queryset = queryset.filter(**{conditions[param_name]: query_params[param_name]})
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class GetHistoryView(generics.RetrieveAPIView):
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        records = instance.history.all()
        history = HistoricalTaskSerializer(records, many=True)
        return Response(history.data)
