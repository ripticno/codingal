from tkinter import*
from datetime import date
window=Tk()
window.title("demo window")
window.geometry("400x300")
lbl=Label(text="hello wlcome to window", fg="white", bg="blue", width=300)
lbl2=Label(text="write your full name", fg="black", bg="white", width=300)
Entryname=Entry()
def display():
    name=Entryname.get()
    global massage
    massage="welcome to this applisition\n todays date is "
    greet="hallo "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,massage)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="begin", fg="white", bg="blue",command=display)
lbl.pack()
lbl2.pack()
Entryname.pack()
btn.pack()
text_box.pack()
window.mainloop()
