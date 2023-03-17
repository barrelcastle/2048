import tkinter as tk
from subroutines2048 import *

root = tk.Tk()
root.title('Home screen')

startBtn = tk.Button(root,text='Start Game',command=lambda:runGame(root))
startBtn.pack()

root.mainloop()