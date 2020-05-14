from tkinter import Tk, Label, StringVar, Entry, Button, Message, X
from zipfile import ZipFile
from os.path import basename

def pt():
    zip_file_name = zip_name_entry.get()
    new_directory_name = basename(zip_file_name).split('.')[0]
    new_path = "H:\\PYTHON\\Practice\\Special\\Zipping files\\"

    with ZipFile(zip_file_name, 'r') as myzip:
        myzip.extractall(path=new_path+new_directory_name)

    message_value.set('Process completed')


root = Tk()
root.title("Unzip Me")

label = Label(root, text='Enter only one zip file path', font='arial 11', fg='red', padx=5, pady=5)
label.pack(fill=X)

zip_name_label = Label(root, text='Enter zip file path', font='arial 9', padx=2, pady=2)
zip_name_label.pack()

zip_name_value = StringVar()
zip_name_entry = Entry(root, textvariable=zip_name_value)
zip_name_entry.pack()

button = Button(root, text='Unzip', command=pt)
button.pack(pady=5)

message_value = StringVar()
message_value.set('Status')
message_label = Message(root, textvariable=message_value)
message_label.pack()

root.geometry("200x150")
root.mainloop()

