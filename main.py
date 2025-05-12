import customtkinter as ctk
from seletor_arquivo import selecionar_arquivo
from gpt import ler_audiograma


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Ouvisse?")
app.geometry("400x200")

def on_click():
    caminho = selecionar_arquivo()
    if caminho:
        entry_arquivo.configure(state="normal")
        entry_arquivo.delete(0, "end")
        entry_arquivo.insert(0, caminho)
        entry_arquivo.configure(state="readonly")
        ler_audiograma()

entry_arquivo = ctk.CTkEntry(app, width=300)
entry_arquivo.pack(pady=20)
entry_arquivo.configure(state="readonly")

botao_selecionar = ctk.CTkButton(app, text="Selecionar gráfico", command=on_click)
botao_selecionar.pack()


app.mainloop()
