from rest_framework import generics, permissions
from rest_framework.response import Response

from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.serializers import HistoricalTaskSerializer, TaskSerializer


class GetCreateTasksView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permissions = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Task.objects.all()
        query_params = self.request.query_params.dict()
        conditions = {
            "status": "status",
            "from_date": "end_date__gte",
            "to_date": "end_date__lte",
        }
        for param_name in conditions.keys():
            if param_name in query_params:
                queryset = queryset.filter(
                    **{conditions[param_name]: query_params[param_name]}
                )
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class GetHistoryView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        records = instance.history.all()
        history = HistoricalTaskSerializer(records, many=True)
        return Response(history.data)
