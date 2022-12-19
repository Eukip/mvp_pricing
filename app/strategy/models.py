from django.db import models
from users.models import User


# Create your models here.
class Strategy(models.Model):
    title = models.CharField(max_length=300)
    priority = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    logic = models.JSONField(blank=True, default=dict)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategy_user')

    def __str__(self) -> str:
        return self.title + ' ' + str(self.product.full_title)

    def save(self) -> None:
        
        return super().save()


class JournalStrategy(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, blank=True, null=True)
    journals = models.JSONField(blank=True, default=dict)