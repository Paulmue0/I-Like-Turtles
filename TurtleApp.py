import turtle
from tkinter import  Canvas, Frame, Tk, ttk
import tkinter
from PIL import Image
from PIL import ImageGrab
import datetime

class TurtleApp:
    """
    The TurtleApp class provides an interactive GUI application allowing users to view and save turtle graphics exercises.
    It uses the tkinter library for GUI, turtle library for turtle graphics, and PIL library for saving images.
    """

    def __init__(self, exercises):
        """
        Initializes a new instance of the TurtleApp class.

        Args:
            exercises (list of functions): A list of turtle graphics exercises to display in the GUI.
        """
        self.exercises = exercises
        self.current_exercise = 0
        self.root = Tk()
        self.root.title("I like Turtles <3")
        self.frame = Frame(self.root)
        self.frame.pack(side="top")

        self.exercise_labels = []
        for i, exercise in enumerate(self.exercises):
            
            label = ttk.Label(self.frame, text=f"Exercise {i + 1}: {exercise.__name__}", borderwidth=1)
            label.pack(side="left")     
            label.bind("<Button-1>", lambda event, index=i: self.on_label_click(event, index))
            self.exercise_labels.append(label)

        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack(side="bottom")

        self.screen = turtle.TurtleScreen(self.canvas)
        self.t = turtle.RawTurtle(self.screen)
        self.t.shape("turtle")
        self.screen.tracer(1,20)

        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.save_button = ttk.Button(self.button_frame, text="Save", command=self.save_exercise)
        self.save_button.pack(side=tkinter.RIGHT)
        self.next_button = ttk.Button(self.button_frame, text="Next", command=self.next_exercise)
        self.next_button.pack(side=tkinter.TOP)

        self.exercise_labels[self.current_exercise].config(background="yellow")
        self.root.mainloop()

    def on_label_click(self, event, index):
        """
        Handles the click event for exercise labels.

        Args:
            event (tkinter event object): The event object that contains information about the event.
            index (int): The index of the label that was clicked.
        """
        previous_index = (index - 1) % len(self.exercises)
        self.current_exercise = previous_index
        self.next_exercise()

    def reset_highlighting(self):
        """
        sets all exercise label backgrounds to white.
        """
        for label in self.exercise_labels:
            label.config(background="white")

    def next_exercise(self):
        """
        updates the current exercise and displays the next one.
        """
        self.screen.reset()
        self.t.shape("turtle")
        self.t.penup()
        self.t.goto(0,0)
        self.t.setheading(0)
        self.t.pendown()
        self.reset_highlighting()
        self.current_exercise = (self.current_exercise + 1) % len(self.exercises)
        self.exercises[self.current_exercise](self.t)
        self.exercise_labels[self.current_exercise].config(background="yellow")
        self.screen.update()
    def save_exercise(self):
        """
        saves a screenshot of the current turtle graphics to a file.
        """
        x0 = self.canvas.winfo_rootx() + self.canvas.winfo_x()
        y0 = self.canvas.winfo_rooty() + self.canvas.winfo_y()
        x1 = x0 + self.canvas.winfo_width()
        y1 = y0 + self.canvas.winfo_height()

        name = self.exercises[self.current_exercise].__name__
        postfix = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        filename = f"{name}_{postfix}.png"
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(filename)
