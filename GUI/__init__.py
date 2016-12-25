# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
import tkinter as tk
import pandas as pd

from Functions import *

from StartPage import StartPage
from Table import Table
from Graph import Graph


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Financial Calculator")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        self.schedule = self.get_schedule()

        for F in (StartPage, Table, Graph):
            frame = F(container, self)

            self.frames[F.__name__] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def get_schedule(self):
        student_loans = read_loans()
        loan_amount, loan_interest = blended(student_loans)
        schedule = pd.DataFrame(amortize(loan_amount, loan_interest, 20, reg_payment=300))
        return schedule

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# # # #
