import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *


def amortize(principal, interest_rate, years,
             reg_payment=None, addl_payment=0, annual_payments=12, start_date=date.today()):

    if reg_payment is None:
        # if the monthly payment is not given, calculate what it probably is
        reg_payment = -round(np.pmt(interest_rate / annual_payments, years * annual_payments, principal), 2)

    # initialize the variables to keep track of the periods and running balances
    p = 1
    beg_balance = principal
    end_balance = principal

    while end_balance > 0:

        # Recalculate the interest based on the current balance
        interest = round(((interest_rate/annual_payments) * beg_balance), 2)

        # Determine payment based on whether or not this period will pay off the loan
        payment = min(reg_payment, beg_balance + interest)
        principal_payment = payment - interest

        # Ensure additional payment gets adjusted if the loan is being paid off
        addl_payment = min(addl_payment, beg_balance - principal_payment)
        end_balance = beg_balance - (principal_payment + addl_payment)

        yield OrderedDict([('Month', start_date),
                           ('Period', p),
                           ('Begin Balance', beg_balance),
                           ('Payment', payment),
                           ('Principal', principal_payment),
                           ('Interest', interest),
                           ('Additional_Payment', addl_payment),
                           ('End Balance', end_balance)])

        # Increment the counter, balance and date
        p += 1
        start_date += relativedelta(months=1)
        beg_balance = end_balance


def blended(loans):
    total = 0
    total_interest = 0
    for l in loans:
        total_interest += float(l['loan amount']) * float(l['interest rate'])
        total += float(l['loan amount'])
    return total, total_interest / total


def read_loans(file_name="loans"):
    with open(file_name, "r") as loans_file:
        loans_raw = [line.strip().split(",") for line in loans_file.readlines()]

    loans_headers = {"loan amount": loans_raw[0].index("loan amount"),
                     "interest rate": loans_raw[0].index("interest rate")}

    return [dict([("loan amount", loan[loans_headers['loan amount']]),
                 ("interest rate", loan[loans_headers['interest rate']])])
            for loan in loans_raw[1:]]

# # # #

if __name__ == "__main__":
    student_loans = read_loans()
    print student_loans

    loan_amount, loan_interest = blended(student_loans)
    print loan_amount, loan_interest

    schedule = pd.DataFrame(amortize(loan_amount, loan_interest, 20, reg_payment=300))
    print schedule.head()
    print schedule.tail()

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 1)
    schedule.plot(x='Month', y='End Balance', ax=ax)
    fig.show()

    raw_input()