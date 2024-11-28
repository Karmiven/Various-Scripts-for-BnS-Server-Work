import os
import tkinter as tk
from tkinter import filedialog, messagebox


class CompactDirectoryTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор дерева каталогов")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Переменные
        self.start_path = tk.StringVar()
        self.excluded_dirs = []

        # Интерфейс
        self.create_widgets()

    def create_widgets(self):
        # Установим стиль
        self.style = {
            "font": ("Segoe UI", 12),
            "bg_color": "#f5f5f5",  # светлый фон
            "btn_bg": "#4CAF50",  # зелёный фон для кнопок
            "btn_fg": "#fff",  # белый текст на кнопках
            "listbox_bg": "#e0e0e0",  # светло-серый фон для списка
            "listbox_fg": "#333",  # тёмный текст в списке
            "entry_bg": "#fff",  # белый фон для поля ввода
            "label_fg": "#333",  # тёмный цвет текста меток
            "padx": 12,  # отступы
            "pady": 10,  # отступы
            "button_width": 20,  # ширина кнопок
            "listbox_height": 10  # высота списка
        }

        # Основной контейнер
        self.root.config(bg=self.style["bg_color"])

        # Рамка для содержимого
        frame = tk.Frame(self.root, bg=self.style["bg_color"])
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Поле выбора каталога
        tk.Label(frame, text="Каталог:", font=self.style["font"], fg=self.style["label_fg"], bg=self.style["bg_color"]).grid(row=0, column=0, padx=self.style["padx"], pady=self.style["pady"], sticky=tk.W)
        tk.Entry(frame, textvariable=self.start_path, font=self.style["font"], state="readonly", width=35, bg=self.style["entry_bg"]).grid(row=0, column=1, padx=self.style["padx"])
        tk.Button(frame, text="Выбрать", font=self.style["font"], command=self.choose_directory, bg=self.style["btn_bg"], fg=self.style["btn_fg"], relief="flat").grid(row=0, column=2, padx=self.style["padx"])

        # Список исключаемых папок
        tk.Label(frame, text="Исключить:", font=self.style["font"], fg=self.style["label_fg"], bg=self.style["bg_color"]).grid(row=1, column=0, padx=self.style["padx"], pady=self.style["pady"], sticky=tk.W)
        self.excluded_listbox = tk.Listbox(frame, height=self.style["listbox_height"], font=self.style["font"], bg=self.style["listbox_bg"], fg=self.style["listbox_fg"], selectmode=tk.SINGLE, bd=0, highlightthickness=0)
        self.excluded_listbox.grid(row=1, column=1, rowspan=3, padx=self.style["padx"], pady=self.style["pady"], sticky=tk.W + tk.E)

        button_frame = tk.Frame(frame, bg=self.style["bg_color"])
        button_frame.grid(row=1, column=2, rowspan=3, padx=self.style["padx"], pady=self.style["pady"], sticky=tk.N)
        tk.Button(button_frame, text="+", font=("Segoe UI", 16), width=3, command=self.add_exclusion, bg=self.style["btn_bg"], fg=self.style["btn_fg"], relief="flat").pack(pady=5)
        tk.Button(button_frame, text="-", font=("Segoe UI", 16), width=3, command=self.remove_exclusion, bg=self.style["btn_bg"], fg=self.style["btn_fg"], relief="flat").pack(pady=5)

        # Кнопка генерации
        tk.Button(frame, text="Генерировать дерево", font=("Segoe UI", 14, "bold"), command=self.generate_tree, bg="#2196F3", fg="#fff", relief="flat").grid(row=4, column=0, columnspan=3, pady=20, sticky=tk.NSEW)

    def choose_directory(self):
        """Открыть диалог для выбора корневого каталога."""
        path = filedialog.askdirectory(title="Выберите каталог для анализа")
        if path:
            self.start_path.set(path)

    def add_exclusion(self):
        """Добавить папку в исключения."""
        path = filedialog.askdirectory(title="Выберите папку для исключения")
        if path:
            self.excluded_dirs.append(os.path.abspath(path))  # Преобразуем путь в абсолютный
            self.excluded_listbox.insert(tk.END, os.path.basename(path))

    def remove_exclusion(self):
        """Удалить выбранную папку из списка исключений."""
        selected = self.excluded_listbox.curselection()
        if selected:
            index = selected[0]
            self.excluded_listbox.delete(index)
            del self.excluded_dirs[index]

    def is_excluded(self, path):
        """
        Проверить, исключён ли данный путь или его родительская папка.
        """
        path = os.path.abspath(path)  # Преобразуем путь в абсолютный
        for excluded in self.excluded_dirs:
            common_path = os.path.commonpath([path, excluded])
            if common_path == excluded:
                return True
        return False

    def print_tree(self, start_path, indent="", is_last=True, output=[]):
        """Рекурсивная функция для генерации дерева каталогов."""
        if self.is_excluded(start_path):
            return output  # Пропустить исключённые папки

        base_name = os.path.basename(start_path)
        connector = "└── " if is_last else "├── "
        output.append(indent + connector + base_name)
        indent += "    " if is_last else "│   "

        items = os.listdir(start_path)
        items = [item for item in items if not self.is_excluded(os.path.join(start_path, item))]  # Фильтрация исключений
        item_count = len(items)

        for index, item in enumerate(sorted(items)):
            item_path = os.path.join(start_path, item)
            is_last_item = (index == item_count - 1)

            if os.path.isdir(item_path):
                self.print_tree(item_path, indent, is_last_item, output)
            else:
                connector = "└── " if is_last_item else "├── "
                output.append(indent + connector + item)
        return output

    def generate_tree(self):
        """Генерация дерева каталогов."""
        start_path = self.start_path.get()
        if not start_path:
            messagebox.showerror("Ошибка", "Выберите каталог для анализа.")
            return

        # Генерация дерева
        try:
            tree_output = self.print_tree(start_path)
            output_file = os.path.join(start_path, "directory_tree.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(tree_output))
            messagebox.showinfo("Готово", f"Дерево каталогов сохранено в файл:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CompactDirectoryTreeApp(root)
    root.mainloop()
