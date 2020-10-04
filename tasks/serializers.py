from rest_framework import serializers

from tasks.models import Task, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("name", )


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj: Task):
        return obj.status.name

    class Meta:
        model = Task
        fields = "__all__"


class HistoricalTaskSerializer(TaskSerializer):
    update_date = serializers.SerializerMethodField()

    def get_update_date(self, obj: Task):
        return obj.history_date

    class Meta:
        model = Task
        fields = ("name", "description", "status", "end_date", "update_date")
