from django.urls import path

from .views import StrategyListCreateView

urlpatterns = [
    path("", StrategyListCreateView.as_view(), name="strategy")
]