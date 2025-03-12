from django.urls import path
from .views import display_choices, loan, get_loan

urlpatterns = [
    path("operations/", display_choices),
    path("operations/<str:loan_id>", loan),
    path("operations/<str:loan_id>/get-loan/<int:amount>", get_loan),
]