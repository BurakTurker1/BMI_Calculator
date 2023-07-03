import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300,)

height_label = tkinter.Label(text="Boyunuzu giriniz: (cm)")
height_label.pack(pady=0)

height_entry = tkinter.Entry(width=30)
height_entry.focus()
height_entry.pack(pady=15)

width_label = tkinter.Label(text="Kilonuzu giriniz: (kg)")
width_label.pack(pady=0)
width_entry = tkinter.Entry(width=30)
width_entry.pack(pady=15)

result_button = tkinter.Button(width=20, text="result")
result_button.pack(padx=20, pady=15)

result_label = tkinter.Label(text="deneme deneme deneme")
result_label.pack()
window.mainloop()