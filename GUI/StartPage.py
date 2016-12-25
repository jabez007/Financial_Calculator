import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)

        button1 = ttk.Button(button_frame,
                             text="Table Page",
                            command=lambda: controller.show_frame("Table"))
        button1.pack(side=tk.LEFT)

        button3 = ttk.Button(button_frame,
                             text="Graph Page",
                             command=lambda: controller.show_frame("Graph"))
        button3.pack(side=tk.LEFT)
