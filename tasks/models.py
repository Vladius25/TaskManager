from django.db import models
from simple_history.models import HistoricalRecords


class Status(models.Model):
    name = models.CharField("Cтатус", unique=True, max_length=30)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField("Название", max_length=30)
    description = models.TextField("Описание", max_length=250)
    creation_date = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.ForeignKey(Status, verbose_name="Статус", to_field='name', on_delete=models.SET_NULL, null=True)
    end_date = models.DateTimeField("Планируемая дата завершения", blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return "%s) %s" % (self.id, self.name)


