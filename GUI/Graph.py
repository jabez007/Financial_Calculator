import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk


class Graph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Graph Page!")
        label.pack(pady=10, padx=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)

        button1 = ttk.Button(button_frame,
                             text="Back to Home",
                             command=lambda: controller.show_frame("StartPage"))
        button1.pack(side=tk.LEFT)

        button2 = ttk.Button(button_frame,
                             text="Table Page",
                             command=lambda: controller.show_frame("Table"))
        button2.pack(side=tk.LEFT)

        f = Figure(figsize=(10, 10), dpi=100)
        a = f.add_subplot(111)
        controller.schedule.plot(x='Month', y='End Balance', ax=a)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
