import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(entry.get()))
        except Exception as e:
            result.set("Error")
    elif text == "C":
        result.set("")
    else:
        result.set(entry.get() + text)

root = tk.Tk()
root.title("Calculator")

result = tk.StringVar()
entry = tk.Entry(root, textvar=result, font="Arial 20 bold", bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

for i, button in enumerate(buttons):
    btn = tk.Button(root, text=button, font="Arial 18", padx=20, pady=20)
    btn.grid(row=i//4+1, column=i%4)
    btn.bind("<Button-1>", click)

root.mainloop()