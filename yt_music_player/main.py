import pyautogui as pg 
import tkinter as tk 
import webbrowser as wb


app = tk.Tk()
app.title('YOUTUBE MUSIC PLAYER')
app.geometry('600x600')
app.resizable(False, False)

prompt = tk.Entry(width=35, font="Helvetica 16")
prompt.place(x=30, y=50)

def start_search():
    global prompt
    wb.open('https://www.youtube.com/results?search_query='+prompt.get())

start = tk.Button(width=5, height=5, font='Helvetica 16', text='START', command=start_search)
start.place(x=270, y=200)


app.mainloop()