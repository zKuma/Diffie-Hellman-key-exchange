import tkinter
import customtkinter
from PIL import Image
from module import *
import random

def er(text):
    textboxe.configure(state="normal")
    textboxe.insert("0.0", text)
    textboxe.configure(state="disabled")


def c1():
    textboxa.configure(state="normal")
    textboxb.configure(state="normal")
    textboxc.configure(state="normal")
    textboxd.configure(state="normal")
    textboxe.configure(state="normal")

    textboxa.delete("1.0", tkinter.END)
    textboxb.delete("1.0", tkinter.END)
    textboxc.delete("1.0", tkinter.END)
    textboxd.delete("1.0", tkinter.END)
    textboxe.delete("1.0", tkinter.END)

    textboxa.configure(state="disabled")
    textboxb.configure(state="disabled")
    textboxc.configure(state="disabled")
    textboxd.configure(state="disabled")
    textboxe.configure(state="disabled")

    try:
        Q = int(entry1.get())
        alpha = entry2.get()
        if alpha == '':
            alpha = random.choice(find_primitive_root(Q))
        else:
            alpha = int(alpha)

        global check
        check = 1
        if Q < 2:
            check = 0
        elif Q == 2:
            check = 1
        elif Q % 2 == 0:
            check = 0
        else:
            for i in range(3, Q, 2):
                if Q % i == 0:
                    check = 0
        if check == 0:
            er("Q phải là số nguyên tố!")
        elif alpha not in find_primitive_root(Q):
            er("Căn nguyên tố của Q sai!")
        else:
            Xa = int(entry3.get())
            Xb = int(entry4.get())
            ares = 1
            bres = 1
            asha = 1
            bsha = 1

            textboxa.configure(state="normal")
            textboxb.configure(state="normal")
            textboxc.configure(state="normal")
            textboxd.configure(state="normal")
            textboxe.configure(state="normal")

            for i in range(Xa):
                ares *= alpha
                ares %= Q
                textboxa.insert("10000000.end", str(alpha) + get_super(str(i+1)) + " mod " + str(Q) + " = " + str(ares) + "\n")

            for i in range(Xb):
                bres *= alpha
                bres %= Q
                textboxb.insert("10000000.end", str(alpha) + get_super(str(i+1)) + " mod " + str(Q) + " = " + str(bres) + "\n")

            for i in range(Xa):
                asha *= bres
                asha %= Q
                textboxc.insert("10000000.end", str(bres) + get_super(str(i + 1)) + " mod " + str(Q) + " = " + str(asha) + "\n")

            for i in range(Xb):
                bsha *= ares
                bsha %= Q
                textboxd.insert("10000000.end", str(ares) + get_super(str(i + 1)) + " mod " + str(Q) + " = " + str(bsha) + "\n")

            textboxe.insert("0.0", "Phiên khóa chung: "+str(asha)+"\n")
            textboxe.insert("0.0", "Khóa công khai của B: " + str(bres) + "\n")
            textboxe.insert("0.0", "Khóa công khai của A: " + str(ares) + "\n")

            textboxa.configure(state="disabled")
            textboxb.configure(state="disabled")
            textboxc.configure(state="disabled")
            textboxd.configure(state="disabled")
            textboxe.configure(state="disabled")
    except:
        er("Tham số lỗi!")


app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Trao đổi khóa Diffie–Hellman")

img1 = customtkinter.CTkImage(light_image=Image.open("pattern.png"), size=(1000, 1000))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=400, corner_radius=15)
frame.place(x=30,y=100)

l2 = customtkinter.CTkLabel(master=frame, text="THAM SỐ", font=('Times', 20))
l2.place(x=110, y=25)

l3 = customtkinter.CTkLabel(master=frame, text="Số nguyên tố Q", font=('Times', 15))
l3.place(x=50, y=70)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='_'*100)
entry1.place(x=50, y=100)

l4 = customtkinter.CTkLabel(master=frame, text="Căn nguyên tố của Q", font=('Times', 15))
l4.place(x=50, y=130)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Có thể bỏ trống')
entry2.place(x=50, y=160)

l5 = customtkinter.CTkLabel(master=frame, text="Khóa mật của A", font=('Times', 15))
l5.place(x=50, y=190)

entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='_'*100)
entry3.place(x=50, y=220)

l6 = customtkinter.CTkLabel(master=frame, text="Khóa mật của B", font=('Times', 15))
l6.place(x=50, y=250)

entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='_'*100)
entry4.place(x=50, y=280)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Bắt đầu", corner_radius=6, command=c1)
button1.place(x=50, y=350)

#Result
detail = customtkinter.CTkFrame(master=l1, width=1200, height=500, corner_radius=15)
detail.place(x=375,y=30)
detail.grid_rowconfigure(0, weight=1)
detail.grid_columnconfigure(0, weight=1)

l7 = customtkinter.CTkLabel(master=detail, text="Khóa công khai của A", font=('Times', 15))
l7.grid(row=0,column=0)

l8 = customtkinter.CTkLabel(master=detail, text="Khóa công khai của B", font=('Times', 15))
l8.grid(row=0,column=1)

textboxa = customtkinter.CTkTextbox(master=detail, width=300, height=150, font=('Times', 15), corner_radius=1, border_width=1, state="disabled", fg_color="transparent")
textboxa.grid(row=1, column=0, sticky="nsew")

textboxb = customtkinter.CTkTextbox(master=detail, width=300, height=150, font=('Times', 15), corner_radius=1, border_width=1, state="disabled", fg_color="transparent")
textboxb.grid(row=1, column=1, sticky="nsew")

l9 = customtkinter.CTkLabel(master=detail, text="A tính phiên khóa chung", font=('Times', 15))
l9.grid(row=2,column=0)

l10 = customtkinter.CTkLabel(master=detail, text="B tính phiên khóa chung", font=('Times', 15))
l10.grid(row=2,column=1)

textboxc = customtkinter.CTkTextbox(master=detail, width=300, height=150, font=('Times', 15), corner_radius=1, border_width=1, state="disabled", fg_color="transparent")
textboxc.grid(row=3, column=0, sticky="nsew")

textboxd = customtkinter.CTkTextbox(master=detail, width=300, height=150, font=('Times', 15), corner_radius=1, border_width=1, state="disabled", fg_color="transparent")
textboxd.grid(row=3, column=1, sticky="nsew")

l11 = customtkinter.CTkLabel(master=detail, text="Kết quả trao đổi khóa", font=('Times', 15))
l11.grid(row=4,column=0, columnspan=2)

textboxe = customtkinter.CTkTextbox(master=detail, width=300, height=150, font=('Times', 30), corner_radius=1, border_width=1, state="disabled", fg_color="transparent")
textboxe.grid(row=5, column=0, columnspan=2, sticky="nsew")

app.mainloop()
