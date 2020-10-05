from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class HistoricalTaskSerializer(serializers.ModelSerializer):
    update_date = serializers.SerializerMethodField()

    def get_update_date(self, obj):
        return obj.history_date

    class Meta:
        model = Task
        fields = ("name", "description", "status", "end_date", "update_date")
