import tkinter as tk

window = tk.Tk()
window.title = ("Bmı Calculate")
window.minsize(300,400)
label1 = tk.Label(
    text="Enter Your Weight(kg)"
)
label2 = tk.Label(
    text="Enter Your Height(cm)"
)

def calculate(weight,height):
    height = height / 100
    height = height ** 2
    result = weight / height

    return result



def click():
    result = calculate(int(entry1.get()),float(entry2.get()))
    if entry1.get() == "" or entry2.get() == "":
        print("Please enter a value")
    elif entry1.get().isalpha() or entry2.get().isalpha(): 
        print("Please enter a numeric value")
    else:
        if result <=18.5:
            label3.config(text=f"BMI:{int(result)}, You are weak") 
        elif result > 18.5 and result <= 24.9:
            label3.config(text=f"BMI:{int(result)}, You are fit") 
        elif result > 25 and result <=30:
            label3.config(text=f"BMI:{int(result)}, You are overweight") 
        else:
            label3.config(text=f"BMI:{int(result)}, You are obesity")

buton = tk.Button(text= "Calculate",command=click)
label1.pack()
entry1 = tk.Entry(width=30)
entry1.pack()
label2.pack()
entry2 = tk.Entry(width=30)
label3 = tk.Label(
    text=""
)


entry2.pack()
buton.pack()
label3.pack()
window.mainloop()  
