import tkinter as tk
from tkinter import ttk, colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")
        self.root.geometry("800x600")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.old_x = None
        self.old_y = None
        self.selected_color = "black"
        self.selected_thickness = 2

        color_label = ttk.Label(root, text="Select Color:")
        color_label.pack(pady=(10, 5))
        self.color_var = tk.StringVar(root)
        self.color_var.set("black")
        self.color_menu = ttk.Combobox(root, textvariable=self.color_var, values=["black", "red", "green", "blue", "Eraser", "Custom"])
        self.color_menu.pack(pady=(0, 10))
        self.color_menu.bind("<<ComboboxSelected>>", self.change_color)

        thickness_label = ttk.Label(root, text="Select Thickness:")
        thickness_label.pack(pady=(10, 5))
        self.thickness_var = tk.StringVar(root)
        self.thickness_var.set("2")
        self.thickness_menu = ttk.Combobox(root, textvariable=self.thickness_var, values=["1", "2", "5", "10"])
        self.thickness_menu.pack(pady=(0, 10))
        self.thickness_menu.bind("<<ComboboxSelected>>", self.change_thickness)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            if self.selected_color == "Eraser":
                self.canvas.create_line(self.old_x, self.old_y, x, y, width=self.selected_thickness*2, fill="white")
            else:
                self.canvas.create_line(self.old_x, self.old_y, x, y, width=self.selected_thickness, fill=self.selected_color)
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def change_color(self, event):
        selected_color = self.color_var.get()
        if selected_color == "Custom":
            color = colorchooser.askcolor()[1]
            if color:
                self.selected_color = color
        else:
            self.selected_color = selected_color

    def change_thickness(self, event):
        selected_thickness = self.thickness_var.get()
        self.selected_thickness = int(selected_thickness)

root = tk.Tk()
app = PaintApp(root)
root.mainloop()
