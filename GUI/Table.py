import tkinter as tk
from tkinter import ttk


class Table(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Table Page!!!")
        label.pack(pady=10, padx=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)

        button1 = ttk.Button(button_frame,
                             text="Back to Home",
                             command=lambda: controller.show_frame("StartPage"))
        button1.pack(side=tk.LEFT)

        button2 = ttk.Button(button_frame,
                             text="Graph Page",
                             command=lambda: controller.show_frame("Graph"))
        button2.pack(side=tk.LEFT)
