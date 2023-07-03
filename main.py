import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=400)

height_entry = tkinter.Entry(width=30)
height_entry.pack()

width_entry = tkinter.Entry(width=30)
width_entry.pack()

result_button = tkinter.Button(width=20)
result_button.pack()

result_label = tkinter.Label(text="deneme deneme deneme")
result_label.pack()
window.mainloop()