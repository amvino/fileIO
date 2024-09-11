from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import pyperclip


# Функция загрузки файла в облако
def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file' : f}
                response = requests.post('https://file.io', files = files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
                pyperclip.copy(link)
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


window = Tk()
window.title("Сохранения файлов в облаке")
window.geometry("300x150")

label = ttk.Label(text="Выберите файл для загрузки")
label.pack(pady=10)

button = ttk.Button(text="Выбрать файл", command=upload)
button.pack(pady=10)

entry = ttk.Entry()
entry.pack()

window.mainloop()