from trackerApp.models import Expenses
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
class ExpenseModel(ModelSerializer):
    class Meta:
        model=Expenses
        fields="__all__"
        read_only_fields=['owner','created_at']