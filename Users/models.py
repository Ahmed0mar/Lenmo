from django.db import models


class Investor(models.Model):
    name = models.CharField(max_length=50)
    banck_account = models.IntegerField(max_length=8, unique=True, blank=False)
    currnet_balance = models.FloatField()
    borrowers_ids = models.ManyToManyField(Borrower)

    def get_current_balance(self):
        #get the current balane ocf the banck account and return its values in current
        current_balance=0
        return current_balance


class Borrower(models.Model):
    name=models.CharField(max_length=50)
    banck_account=models.IntegerField(max_length=8, unique=True, blank=False)
    borrow_date=models.DateField()
    is_currently_borrowed=models.BooleanField(default=False)
    amount_of_borrowed_money=models.IntegerField()
    monthly_share=models.FloatField()
    investors_ids=models.ManyToManyField(Investor)

