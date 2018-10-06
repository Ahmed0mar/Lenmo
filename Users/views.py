from django.shortcuts import render

# Create your views here.
from .models import Investor, Borrower

def borrow_request(request, money_amount):
       all_investors = Investor.objects.get()
       for investor in all_investors:
           if investor.currnet_balance >= money_amount:
               lend_money()
               break;
        # the bellow else to check if the for loop have been breaked or not
       else:
            # if their is no investor in database has a current balance equal to
            # money amount that the borrower want to borrow then the system take the amount of money
            #  from different users
            get_investors_ids(all_investors, money_amount)


def get_investors_ids(all_investors, money_amount):
    sum =0
    indexes_of_investors=[]
    for investor in all_investors:
        sum += investor.currnet_balance
        indexes_of_investors.append(investor.id)
        if sum == money_amount:
            return indexes_of_investors
        else:
            raise ValueError('The amount you asked to borrow is too huge')
