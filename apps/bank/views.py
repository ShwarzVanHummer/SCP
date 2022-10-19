from django.db.models import QuerySet
from urllib.request import Request
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet

from abstracts.mixins import ValidationMixin, ResponseMixin

from .serializers import (
    AccountSerializer,
    CardSerializer,
    TransactionsSerializer
)

from .models import (
    Card,
    Account,
    Transactions
)

# class AccountViewSet(ValidationMixin, ResponseMixin, ViewSet):