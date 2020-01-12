from plagiarism import *
from tkinter import filedialog
def o2m():
    file1 = filedialog.askopenfilename(initialdir="./",
                                       title="Select Document File",
                                       filetypes=(("Documents", "*.pdf"), ("all files", "*.*")))

    dir = os.path.abspath(filedialog.askdirectory(initialdir="./", title="Select File Directory"))
    fileCount = os.listdir(dir)
    n = len(fileCount)
    i = 0
    while i < n:
        OneToMany(file1, dir, i)
        i += 1


def singleFile():
    file1 = filedialog.askopenfilename(initialdir="./",
                                       title="Select Source File",
                                       filetypes=(("Documents", "*.pdf"), ("all files", "*.*")))
    file2 = filedialog.askopenfilename(initialdir="./",
                                       title="Select Target File",
                                       filetypes=(("Documents", "*.pdf"), ("all files", "*.*")))

    OneToOne(file1,file2)