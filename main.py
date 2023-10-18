import tkinter as tk
from cryptography.fernet import Fernet

class SecretNoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Secret Notes")

        # Anahtar ve Fernet şifreleme nesnesini oluştur
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # Pencere boyutunu ayarla
        window_width = 500
        window_height = 400
        master.geometry(f"{window_width}x{window_height}")

        # Başlık etiketi
        self.title_label = tk.Label(master, text="Enter Your Title:")
        self.title_label.pack()

        # Başlık metin giriş kutusu
        self.title_entry = tk.Entry(master)
        self.title_entry.pack()

        # Secret etiketi
        self.secret_label = tk.Label(master, text="Enter Your Secret:")
        self.secret_label.pack()

        # Secret metin giriş kutusu (10 satırlık)
        self.secret_entry = tk.Text(master, height=10)
        self.secret_entry.pack()

        # Master Key etiketi
        self.master_key_label = tk.Label(master, text="Enter Master Key:")
        self.master_key_label.pack()

        # Master Key metin giriş kutusu
        self.master_key_entry = tk.Entry(master, show="*")
        self.master_key_entry.pack(pady=10)  # Master Key giriş kutusunu aşağı doğru biraz ittik

        # Save&Encrypt butonu
        self.save_button = tk.Button(master, text="Save & Encrypt", command=self.save_and_encrypt)
        self.save_button.pack()

        # Decrypt butonu
        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_note)
        self.decrypt_button.pack()

    def save_and_encrypt(self):
        title = self.title_entry.get()
        secret = self.secret_entry.get("1.0", tk.END).strip()  # 10 satırlık metni al

        # Metni şifrele
        encrypted_note = self.cipher_suite.encrypt(secret.encode())

        # Dosyaya kaydet
        with open(f"{title}.txt", "wb") as file:
            file.write(encrypted_note)

        print("Note saved and encrypted successfully.")

    def decrypt_note(self):
        title = self.title_entry.get()
        master_key = self.master_key_entry.get()

        try:
            # Dosyayı oku ve şifreyi çöz
            with open(f"{title}.txt", "rb") as file:
                encrypted_note = file.read()
                decrypted_note = self.cipher_suite.decrypt(encrypted_note)
                print("Decrypted Note:", decrypted_note.decode())
        except FileNotFoundError:
            print("Note not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecretNoteApp(root)
    root.mainloop()
