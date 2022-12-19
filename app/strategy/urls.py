from django.urls import path

from .views import StrategyCreateView

urlpatterns = [
    path("", StrategyCreateView.as_view(), name="strategy")
]