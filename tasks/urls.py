from django.urls import path

from tasks.views import GetHistoryView

urlpatterns = [
    path("history/<int:pk>", GetHistoryView.as_view(), name="get-history"),
]