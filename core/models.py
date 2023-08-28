from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, DO_NOTHING, IntegerField, CharField, CASCADE, FloatField, DateTimeField


class Loans(Model):
    requested_by = ForeignKey(User, on_delete=DO_NOTHING, related_name="my_loans")
    staff = ForeignKey(User, on_delete=DO_NOTHING, related_name="assigned_loans", null=True)
    amount = FloatField(null=False)
    currency = CharField(max_length=5, default="INR")
    term = IntegerField(null=False)
    frequency = CharField(default="weekly")
    status = CharField(default="pending")
    requested_at = DateTimeField(null=False)
    approved_at = DateTimeField(null=True)
    denied_at = DateTimeField(null=True)
    paid_at = DateTimeField(null=True)


class Repayments(Model):
    loan = ForeignKey(Loans, on_delete=CASCADE)
    payer = ForeignKey(User, on_delete=DO_NOTHING)
    amount = FloatField(null=False)
    currency = CharField(max_length=5, default="INR")
    status = CharField(default="pending")
    repayment_date = DateTimeField(null=False)
    created_at = DateTimeField(null=True)
    paid_at = DateTimeField(null=True)
    failed_at = DateTimeField(null=True)
