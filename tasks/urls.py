from django.urls import path

from tasks.views import GetHistoryView, GetCreateTasksView, GetUpdateDeleteTaskView

urlpatterns = [
    path("", GetCreateTasksView.as_view()),
    path("<int:pk>", GetUpdateDeleteTaskView.as_view()),
    path("history/<int:pk>", GetHistoryView.as_view()),
]
