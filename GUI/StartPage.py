import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Table Page",
                            command=lambda: controller.show_frame("Table"))
        button1.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame("Graph"))
        button3.pack()
