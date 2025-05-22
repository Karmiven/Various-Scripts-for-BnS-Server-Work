import tkinter as tk
from tkinter import ttk

# Алфавит для кодирования (тот же, что и в PHP)
encodechar = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def generate_game_item_key():
    itemid_str = entry_itemid.get()
    if not itemid_str.isdigit():
        entry_key.delete(0, tk.END)
        entry_key.insert(0, "Invalid ID")
        return

    itemid = int(itemid_str)
    itemno = itemid * 16
    encode_str = []

    while itemno >= 64:
        remainder = itemno % 64
        encode_str.append(encodechar[remainder])
        itemno //= 64
    encode_str.append(encodechar[itemno])

    key = "AA" + ''.join(reversed(encode_str)) + "=="
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)

# Интерфейс
root = tk.Tk()
root.title("GameItemKey Generator")
root.geometry("300x150")
root.resizable(False, False)

# Метки и поля
label_itemid = ttk.Label(root, text="Item ID:")
label_itemid.pack(pady=(10, 0))
entry_itemid = ttk.Entry(root)
entry_itemid.pack()

label_key = ttk.Label(root, text="GameItemKey:")
label_key.pack(pady=(10, 0))
entry_key = ttk.Entry(root)
entry_key.pack()

# Кнопка
btn_generate = ttk.Button(root, text="Generate", command=generate_game_item_key)
btn_generate.pack(pady=10)

root.mainloop()
