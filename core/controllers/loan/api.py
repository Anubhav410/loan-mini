from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes, api_view

from core.controllers.loan.serializer import CreateLoanSerializer
from core.services.loan import LoanService


class LoanAPIView:
    @staticmethod
    @api_view(['POST', 'GET'])
    @authentication_classes([BasicAuthentication])
    def list_and_create_loan(request):
        if request.method == 'POST':
            return LoanAPIView.create_loan(request)
        elif request.method == 'GET':
            return LoanAPIView.list_loan(request)

    @staticmethod
    def list_loan(request):
        pass

    @staticmethod
    def create_loan(request):
        serializer = CreateLoanSerializer(data=request.data)
        if serializer.is_valid():
            loan = LoanService.create_loan(requesting_user=request.user, amount=serializer.validated_data['amount'],
                                           term=serializer.validated_data['term'])
