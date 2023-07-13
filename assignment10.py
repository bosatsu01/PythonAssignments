import tkinter as tk
import webbrowser as wb
obj=tk.Tk()

#button
e=tk.Entry(obj,font=("Times New Roman",25),width=30)
e.grid(row=0,column=0)

def display():
    s=e.get()   
    wb.open(f"https://aniwatch.to/home?source=pwa") 
    print("Navigating to AniWatch the Search: ",(f"https://aniwatch.to/home?source=pwa"))

b1=tk.Button(obj,text="Search Anime",font=("Jokerman",25),command=display)
b1.grid(row=1,column=0)

b=tk.Button(obj,text="Close",font=("Jokerman",30),command=obj.destroy)
b.grid(row=2,column=0)
obj.mainloop()

