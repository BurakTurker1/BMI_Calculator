import tkinter
BMI_result=0
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

def clickButton():
    user_width = float(width_entry.get())
    user_height = float(height_entry.get()) / 100
    BMI_result = user_width / (user_height * user_height)
    result_label.config(text=f"Bmı değeriniz: {BMI_result:.2f}")
    if BMI_result<18.5:
        result_label.config(text=f"Bmı değeriniz: {BMI_result:.2f} zayıf")
    elif BMI_result>19 and BMI_result<24.9:
        result_label.config(text=f"Bmı değeriniz: {BMI_result:.2f} sağlıklı kilo")
    elif BMI_result>25 and BMI_result<29.9:
        result_label.config(text=f"Bmı değeriniz: {BMI_result:.2f} kilolu")
    elif BMI_result>30:
        result_label.config(text=f"Bmı değeriniz: {BMI_result:.2f} obez")


result_button = tkinter.Button(width=20, text="result", command=clickButton)
result_button.pack(padx=20, pady=15)

result_label = tkinter.Label()
result_label.pack()
window.mainloop()