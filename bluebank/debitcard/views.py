from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from datetime import datetime


def display_choices(request):
    return HttpResponse("this is operations page!")


def get_loan(request, amount):
    global INIT_AMOUNT 
    if amount > INIT_AMOUNT:
        return HttpResponse(f"Maximum allowed loan amount is: {INIT_AMOUNT}")
    else:
        INIT_AMOUNT -= amount
        id = randint(1000, 9999)
        loans.append({
            "date": datetime.now(),
            "amount": amount,
            "id": str(id)
        })
        return HttpResponse(f"You've got the loan. Loan ID: {id}")


init_amount = 1000000
loans = []
def loan(request, loan_id):
    loan_data = list(filter(lambda x: x["id"] == str(loan_id), loans))
    if loan_data:
        return HttpResponse(str(loan_data[0]))
    else:
        return HttpResponse("loan not found")



