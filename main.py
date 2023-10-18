from tkinter import *
#Arayüz Uİ oluşturma

FONT=("Verdana",20,"normal")
window =Tk()
window.title("Gizli Not")
window.config(padx=30,pady=30)

#konu başlığı ekleme
title_info_label=Label(text="Başlığı Giriniz",font=FONT)
title_info_label.pack()

title_entry=Entry(width=30)
title_entry.pack()

input_info_label=Label(text="Gizli Mesajı Giriniz",font=FONT)
input_info_label.pack()

input_text= Text(width=50,height=25)
input_text.pack()

master_secret_label=Label(text="Şifreyi Giriniz",font=FONT)
master_secret_label.pack()

master_secret_input=Entry(width=30)
master_secret_input.pack()

save_button=Button(text="Kaydet ve Şifrele")
save_button.pack()

decrypt_button=Button(text="Çöz")
decrypt_button.pack()


window.mainloop()