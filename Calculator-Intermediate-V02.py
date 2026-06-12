import tkinter as tk

history = []

def on_click(value):
    current = entry.get()

    if value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)

            history.append(current + " = " + result)
            update_history()

        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    elif value == "C":
        entry.delete(0, tk.END)

    elif value == "⌫":
        entry.delete(len(current)-1, tk.END)

    elif value == "√":
        try:
            num = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, num ** 0.5)
        except:
            entry.insert(0, "Error")

    elif value == "x²":
        try:
            num = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, num ** 2)
        except:
            entry.insert(0, "Error")

    elif value == "%":
        try:
            num = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, num / 100)
        except:
            entry.insert(0, "Error")

    elif value == "±":
        try:
            num = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, -num)
        except:
            entry.insert(0, "Error")

    else:
        entry.insert(tk.END, value)


def update_history():
    history_box.delete(0, tk.END)
    for item in history[-10:]:
        history_box.insert(tk.END, item)


root = tk.Tk()
root.title("Intermediate Python Calculator")
root.geometry("383x630")
root.configure(bg="#222")

entry = tk.Entry(
    root,
    font=("Arial", 24),
    bg="#333",
    fg="white",
    insertbackground="white",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    "C", "⌫", "%", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "±", "0", ".", "=",
    "√", "x²"
]

row = 1
col = 0

for b in buttons:
    cmd = lambda x=b: on_click(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        width=5,
        height=2,
        font=("Arial", 14),
        bg="#444",
        fg="white",
        activebackground="#666"
    ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

history_label = tk.Label(root, text="History", bg="#222", fg="white")
history_label.grid(row=row+1, column=0, columnspan=4)

history_box = tk.Listbox(root, height=6, bg="#333", fg="white")
history_box.grid(row=row+2, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

root.mainloop()
