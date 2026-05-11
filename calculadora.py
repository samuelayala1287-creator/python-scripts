import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons frame
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        # First row
        clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#fff", cursor="hand2", command=self.clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

        # Second row
        seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
        multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

        # Third row
        four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
        minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

        # Fourth row
        one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
        plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

        # Fifth row
        zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
        equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.equalpress).grid(row=4, column=3, padx=1, pady=1)

        # Sixth row for additional functions
        sqrt = tk.Button(btns_frame, text="√", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.sqrt).grid(row=5, column=0, padx=1, pady=1)
        power = tk.Button(btns_frame, text="^", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("**")).grid(row=5, column=1, padx=1, pady=1)
        pi = tk.Button(btns_frame, text="π", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click(math.pi)).grid(row=5, column=2, padx=1, pady=1)
        e = tk.Button(btns_frame, text="e", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click(math.e)).grid(row=5, column=3, padx=1, pady=1)

    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equalpress(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            messagebox.showerror("Erro", "Expressão inválida")
            self.expression = ""

    def sqrt(self):
        try:
            result = str(math.sqrt(float(self.expression)))
            self.input_text.set(result)
            self.expression = result
        except:
            messagebox.showerror("Erro", "Expressão inválida para raiz quadrada")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()