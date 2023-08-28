from botocore.exceptions import ValidationError
from rest_framework.exceptions import ValidationError

from core.services.auth import AuthService

from django.test import TestCase

from core.services.loan import LoanService


class LoanTestCases(TestCase):
    def setUp(self):
        self.admin_user = AuthService.sign_up("Test Admin", "admin@test.com", "Test123456", True)
        self.customer_user = AuthService.sign_up("Test Customer", "customer@test.com", "Test123456", False)
        self.loan = LoanService.create_loan(requesting_user=self.customer_user, amount=5000, term=5, frequency="weekly")

    def test_customer_approval_fails(self):
        with self.assertRaises(ValidationError):
            LoanService.approve_loan(self.customer_user, self.loan.id)

    def test_admin_approval_passes(self):
        loan = LoanService.approve_loan(self.admin_user, self.loan.id)
        self.assertEquals("approved", loan.status)

    def test_customer_pays_all_repayments(self):
        loan = self.loan
        for repayment in loan.repayments_set.all():
            LoanService.pay(self.customer_user, loan_id=loan.id, repayment_id=repayment.id)

        loan = LoanService.get_loan_by_id(self.loan.id)
        self.assertEquals("paid", loan.status)

        for repayment in loan.repayments_set.all():
            self.assertEquals("paid", repayment.status)
# def test_user_creation():
#     assert admin_user.id is not None
#     assert customer_user.id is not None
#     assert admin_user.is_staff
#     assert not customer_user.is_staff
#
#
# def test_loan_approval():
#     pass
