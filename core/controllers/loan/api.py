from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes, api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from core.controllers.loan.serializer import CreateLoanSerializer, LoanSerializer
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
        loans = LoanService.list(user=request.user)
        return Response(LoanSerializer(loans, many=True).data, status=HTTP_200_OK)

    @staticmethod
    def create_loan(request):
        serializer = CreateLoanSerializer(data=request.data)
        if serializer.is_valid():
            loan = LoanService.create_loan(requesting_user=request.user, amount=serializer.validated_data['amount'],
                                           term=serializer.validated_data['term'])

            return Response(LoanSerializer(loan).data, status=HTTP_201_CREATED)
        return Response({"success": False, "error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
