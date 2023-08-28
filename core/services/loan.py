import logging
from datetime import timezone, timedelta

from django.utils import timezone

from core.models import Loans, Repayments

log = logging.getLogger(__name__)


class LoanService:
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
