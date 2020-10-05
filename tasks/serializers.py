from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = "__all__"


class HistoricalTaskSerializer(serializers.ModelSerializer):
    update_date = serializers.ReadOnlyField(source="history_date")

    class Meta:
        model = Task
        fields = ("name", "description", "status", "end_date", "update_date")
