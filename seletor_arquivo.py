from tkinter import filedialog, Tk

def selecionar_arquivo():
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    caminho_arquivo = filedialog.askopenfilename(
        title="Adicione o gráfico",
        filetypes=[("Imagens", "*.jpg *.png *.jpeg")]
    )
    root.destroy()
    return caminho_arquivo
