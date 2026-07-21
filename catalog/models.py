from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
    Абстрактная модель с полями создания и изменения.
    Удобно наследовать для большинства моделей приложения.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True