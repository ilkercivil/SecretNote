import tkinter as tk

# Fonksiyonlar
def gizli_not_yarat():
    # Bu fonksiyon, Gizli Not yarat butonuna tıklandığında çağrılacak işlemleri gerçekleştirir.
    pass  # Fonksiyonun işlevini buraya ekleyin

def gizli_not_oku():
    # Bu fonksiyon, Gizli Not oku butonuna tıklandığında çağrılacak işlemleri gerçekleştirir.
    pass  # Fonksiyonun işlevini buraya ekleyin

# Ana uygulama penceresini oluşturma
root = tk.Tk()
root.title("Gizli Not")
root.geometry("500x500")

# Butonlar
gizli_not_yarat_button = tk.Button(root, text="Gizli Not Yarat", command=gizli_not_yarat)
gizli_not_yarat_button.pack(pady=20)

gizli_not_oku_button = tk.Button(root, text="Gizli Not Oku", command=gizli_not_oku)
gizli_not_oku_button.pack(pady=20)

# Uygulamayı başlatma
root.mainloop()
