from rest_framework.fields import FloatField, IntegerField
from rest_framework.serializers import Serializer, ModelSerializer

from core.controllers.auth.serializer import UserSerializer
from core.models import Loans, Repayments


class CreateLoanSerializer(Serializer):
    amount = FloatField()
    term = IntegerField()


class RepaymentSerializer(ModelSerializer):
    class Meta:
        model = Repayments
        fields = ['id', 'amount', 'repayment_date', 'status', 'created_at']


class LoanSerializer(ModelSerializer):
    re_payments = RepaymentSerializer(many=True, source='repayments_set')
    requested_by = UserSerializer()

    class Meta:
        model = Loans
        fields = ['id', 'amount', 'requested_by', 'status', 'requested_at', 're_payments']
