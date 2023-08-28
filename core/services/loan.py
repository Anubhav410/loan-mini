import logging
from datetime import timezone, timedelta

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from core.models import Loans, Repayments

log = logging.getLogger(__name__)


class LoanService:
    @staticmethod
    def get_loan_by_id(loan_id) -> Loans:
        return Loans.objects.get(id=loan_id)

    @staticmethod
    def approve_loan(approving_user, loan_id):
        if not approving_user.is_staff:
            raise ValidationError("You do not have permission for this operation")

        log.info(f"Approving Loan: {loan_id}")
        loan = LoanService.get_loan_by_id(loan_id)
        if loan.status != "pending":
            raise ValidationError("Not in a Valid State")

        loan.approved_at = timezone.now()
        loan.staff = approving_user
        loan.status = "approved"
        loan.save()
        return loan

    @staticmethod
    def pay(user, loan_id, repayment_id):
        log.info(f"Paying Loan: {loan_id} : RePaymentId: {repayment_id}")
        loan = LoanService.get_loan_by_id(loan_id)
        repayment = loan.repayments_set.get(id=repayment_id)
        repayment.status = "paid"
        repayment.paid_at = timezone.now()
        repayment.save()

        all_paid = True
        for repayments in loan.repayments_set.all():
            if repayments.status != "paid":
                all_paid = False
                break

        if all_paid:
            loan.status = "paid"
            loan.save()

        loan.refresh_from_db()
        return loan

    @staticmethod
    def deny_loan(acting_user, loan_id):
        log.info(f"Denying Loan: {loan_id}")
        loan = LoanService.get_loan_by_id(loan_id)
        if loan.status != "pending":
            raise ValidationError("Not in a Valid State")

        loan.denied_at = timezone.now()
        loan.staff = acting_user
        loan.status = "denied"
        loan.save()
        return loan

    @staticmethod
    def list(user):
        if user.is_staff:
            return Loans.objects.all()
        else:
            return Loans.objects.filter(requested_by=user)

    @staticmethod
    def create_loan(requesting_user, amount, term, frequency="weekly"):
        log.info(f"creating loan: {requesting_user}, {amount}, {term}, {frequency}")
        loan = Loans.objects.create(requested_by=requesting_user, amount=amount, term=term, frequency=frequency,
                                    requested_at=timezone.now())

        # create the repayment schedule too
        now = timezone.now()
        repayment_date = now
        installment_amount = amount / term
        for n in range(term):
            repayment_date = repayment_date + timedelta(weeks=1)
            Repayments.objects.create(loan=loan, amount=installment_amount, payer=requesting_user,
                                      repayment_date=repayment_date,
                                      created_at=now)

        log.info(f"loan created : {loan}")
        return loan
