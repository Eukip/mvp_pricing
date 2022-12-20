from django.db import models
from users.models import User
from .utils import get_needed_strategy_logic
from config.tasks import strategy_result as task_result
from .utils import strategy_result


# Create your models here.
class Strategy(models.Model):
    title = models.CharField(max_length=300)
    priority = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    logic = models.JSONField(blank=True, default=dict)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategy_user')

    def __str__(self) -> str:
        return self.title

    def save(self) -> None:
        super().save()
        needed_strategy_product = get_needed_strategy_logic(self.pk)
        strategy_result(needed_strategy_product)
        super().save()


class JournalStrategy(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, blank=True, null=True)
    journals = models.JSONField(blank=True, default=dict)