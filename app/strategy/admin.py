from django.contrib import admin
from .models import Strategy, JournalStrategy


# Register your models here.
class StrategyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Strategy, StrategyAdmin)


class JournalStrategyAdmin(admin.ModelAdmin):
    pass
admin.site.register(JournalStrategy, JournalStrategyAdmin)