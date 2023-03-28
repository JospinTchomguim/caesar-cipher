import tkinter as tk

def caesar_cipher(message, key, mode):
    result = ""

    if mode == "decrypt":
        key = -key

    for char in message:
        if char.isalpha():
            ascii_val = ord(char)
            shifted_ascii_val = ascii_val + key

            if char.islower():
                if shifted_ascii_val < ord("a"):
                    shifted_ascii_val += 26
                elif shifted_ascii_val > ord("z"):
                    shifted_ascii_val -= 26
            elif char.isupper():
                if shifted_ascii_val < ord("A"):
                    shifted_ascii_val += 26
                elif shifted_ascii_val > ord("Z"):
                    shifted_ascii_val -= 26

            result += chr(shifted_ascii_val)
        else:
            result += char

    return result


def encrypt_message():
    message = entry.get()
    key = int(key_entry.get())
    encrypted_message = caesar_cipher(message, key, "encrypt")
    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, encrypted_message)
    output.config(state="disabled")


def decrypt_message():
    message = entry.get()
    key = int(key_entry.get())
    decrypted_message = caesar_cipher(message, key, "decrypt")
    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, decrypted_message)
    output.config(state="disabled")


# Créer l'interface graphique
window = tk.Tk()
window.title("Chiffrement de César")

# Entrée pour le message
label = tk.Label(window, text="Message à chiffrer/déchiffrer :")
label.grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

# Entrée pour la clé
key_label = tk.Label(window, text="Clé de chiffrement/déchiffrement :")
key_label.grid(row=1, column=0)
key_entry = tk.Entry(window)
key_entry.grid(row=1, column=1)

# Boutons de chiffrement et de déchiffrement
encrypt_button = tk.Button(window, text="Chiffrer", command=encrypt_message)
encrypt_button.grid(row=2, column=0)
decrypt_button = tk.Button(window, text="Déchiffrer", command=decrypt_message)
decrypt_button.grid(row=2, column=1)

# Sortie pour le résultat
output_label = tk.Label(window, text="Résultat :")
output_label.grid(row=3, column=0)
output = tk.Text(window, height=5, width=50, state="disabled")
output.grid(row=4, column=0, columnspan=2)

window.mainloop()


