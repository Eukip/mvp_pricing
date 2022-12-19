from django.urls import path
from .views import StrategyToProductView

urlpatterns = [
    path("<int:product_id>", StrategyToProductView.as_view(), name="strategy_product")
]