from tkinter import Tk, Label, StringVar, Entry, Button, Message, X
from tkinter import messagebox
from os import walk, path
from zipfile import ZipFile, ZIP_DEFLATED


def pt():
    folder_path = folder_path_entry.get()
    zip_file_name = zip_name_entry.get()
    files_to_zip = list()

    for root, _, files in walk(folder_path):
        for file in files:
            files_to_zip.append(path.join(root, file))

    with ZipFile(zip_file_name + '.zip', 'w') as myzip:
        for file in files_to_zip:
            myzip.write(file, arcname=path.basename(file), compress_type=ZIP_DEFLATED)

    message_value.set('Process completed')


root = Tk()
root.title("Zip Me")

messagebox.showinfo("Important Note", "Please! give only one folder without subfolders inside it.")

label = Label(root, text='Enter only one folder path', font='arial 11', fg='red', padx=5, pady=5)
label.pack(fill=X)

folder_path_label = Label(root, text='Enter folder path', font='arial 9', padx=2, pady=2)
folder_path_label.pack()

folder_path_value = StringVar()
folder_path_entry = Entry(root, textvariable=folder_path_value)
folder_path_entry.pack()

zip_name_label = Label(root, text='Enter zip file name without ".zip"', font='arial 9', padx=2, pady=2)
zip_name_label.pack()

zip_name_value = StringVar()
zip_name_entry = Entry(root, textvariable=zip_name_value)
zip_name_entry.pack()

button = Button(root, text='compress & zip', command=pt)
button.pack(pady=5)

message_value = StringVar()
message_value.set('Zipping status')
message_label = Message(root, textvariable=message_value)
message_label.pack()

root.geometry("220x200")
root.mainloop()
