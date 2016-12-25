from Functions import *
from GUI import GUI


if __name__ == "__main__":
    """
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
    """
    app = GUI()
    app.mainloop()
