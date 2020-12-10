from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import timedelta


class Posts(models.Model):
    class Meta(object):
        db_table = 'posts'

    task = models.CharField(verbose_name='タスク名', max_length=255)
    task_text = models.CharField(verbose_name='タスク詳細', max_length=255)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now())
    deadline = models.DateTimeField(verbose_name='締切', default=timezone.now() + timedelta(days=3))
    importance = models.BooleanField(verbose_name='重要度', default=True)
    Urgency = models.BooleanField(verbose_name='緊急度', default=True)

    def __str__(self):
        return self.task, self.deadline
