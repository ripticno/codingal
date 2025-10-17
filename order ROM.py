import tkinter as tk
from tkinter import ttk, messagebox
class ROM:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Managment App")
        self.menu_item={"FRIES":2,"LUNCH":2,"BURGER":3,"PIZZA":4,"CHEESE BURGER":2.5,"DRINKS":1}
        self.exchange_rate=125
        self.setup_backbround(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.label(frame,text="Restaurant Managment App",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_lables={}
        self.menu_quantities={}
        for i, (item,price) in enuerate(self.manu.items(),start=1):
            label=ttk.Label(frame,text="f{item} (${price})",font=("Aial",12))
        label.grid(row=i,pabx=10,pady=5)
        self.menu_label[item]=label
        quantity_entry=ttk.Entry(frame,width=5)
        quantity_entry.grid(row=i,colum=1,padx=10,pady=5)
        self.menu_quantites[item]=quantity_entry
    self.currency_var=tk.StringVar()
    ttk.Label(frame,text="Currency",font=("Arial",12)).grid(row=len(self.menu_item)+1,colum=0,padx=10,pady=5)
    currency_dropdown=ttk.combobox()
