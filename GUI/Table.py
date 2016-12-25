import tkinter as tk
from tkinter import ttk


class Table(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Table Page!!!")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame("Graph"))
        button2.pack()
