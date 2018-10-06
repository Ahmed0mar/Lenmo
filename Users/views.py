from django.shortcuts import render
from datetime import date
# Create your views here.
from .models import Investor, Borrower

def borrow_request(request, money_amount):
       all_investors = Investor.objects.get()
       for investor in all_investors:
           if investor.currnet_balance >= money_amount:
               lend_money(borrower, investor, money_amount)
               break;
        # the bellow else to check if the for loop have been breaked or not
       else:
            # if their is no investor in database has a current balance equal to
            # money amount that the borrower want to borrow then the system take the amount of money
            #  from different users
            sum_of_investors_that_can_lend=get_investors(all_investors, money_amount)
            for investor in sum_of_investors_that_can_lend:
                investor.currnet_balance=0
                investor.borrower_id = borrower.id

def get_investors(all_investors, money_amount):
    sum =0
    indexes_of_investors=[]
    for investor in all_investors:
        sum += investor.currnet_balance
        indexes_of_investors.append(investor.id)
        if sum == money_amount:
            return indexes_of_investors
        else:
            raise ValueError('The amount you asked to borrow is too huge')


def lend_money(borrower, investor, money_amount):
    borrower.is_currently_borrowed=True
    borrower.amount_of_borrowed_money=money_amount
    borrower.monthly_share=money_amount/6
    borrower.borrow_date = date.today()

