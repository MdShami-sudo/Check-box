import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Checkbox Example")

def checkbox_changed():
    if chk_state.get() == 1:
        lbl_status.config(text="Checkbox is checked!")
    else:
        lbl_status.config(text="Checkbox is unchecked.")


chk_state = tk.IntVar()

chk = ttk.Checkbutton(root, text="please check me for the confirmation!", variable=chk_state, command=checkbox_changed)
chk.pack(padx=20, pady=20)

lbl_status = ttk.Label(root, text="")
lbl_status.pack(pady=10)

root.mainloop()
