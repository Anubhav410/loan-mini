from django.contrib import admin
from django.urls import path, include

from core.controllers.auth.api import AuthAPIView
from core.controllers.loan.api import LoanAPIView

urlpatterns = [

    # Auth APIs
    path('auth/signup', AuthAPIView.sign_up),
    path('auth/login', AuthAPIView.login),

    # Loan APIs
    path('loan', LoanAPIView.list_and_create_loan),  # list and create loans
]
