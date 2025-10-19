import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

# --- 1. CONFIGURACIÓN INICIAL Y LECTURA DE PALABRAS ---
try:
    with open('oficina.txt', 'r', encoding='utf-8') as archivo:
        palabras = [p for p in archivo.read().splitlines() if p]
    palabra_secreta = random.choice(palabras).upper()
except (FileNotFoundError, IndexError):
    palabra_secreta = "PYTHON"
    print("ADVERTENCIA: No se encontró 'oficina.txt' o está vacío. Usando palabra de respaldo.")

intentos_restantes = 7
palabra_mostrada = list("_" * len(palabra_secreta))

# --- 2. LÓGICA PRINCIPAL DEL JUEGO ---
def verificar_letra():
    global intentos_restantes
    letra = entry_letra.get().upper()
    entry_letra.delete(0, tk.END)

    if not letra or not letra.isalpha() or len(letra) != 1:
        messagebox.showwarning("Entrada Inválida", "Por favor, introduce una sola letra.")
        return

    if letra in palabra_secreta:
        for i, caracter in enumerate(palabra_secreta):
            if caracter == letra:
                palabra_mostrada[i] = letra
    else:
        intentos_restantes -= 1

    actualizar_interfaz()
    verificar_fin_del_juego()

def actualizar_interfaz():
    """Esta función actualiza todos los elementos de la ventana."""
    label_palabra.config(text=" ".join(palabra_mostrada))
    
    errores = 7 - intentos_restantes
    if 0 <= errores < len(imagenes):
        label_imagen.config(image=imagenes[errores])
    
    label_intentos.config(text=f"Quedan {intentos_restantes} intentos")

def verificar_fin_del_juego():
    if "_" not in palabra_mostrada:
        messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
        ventana.destroy()
    elif intentos_restantes == 0:
        messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {palabra_secreta}")
        ventana.destroy()

# --- 3. CREACIÓN DE LA VENTANA Y SUS COMPONENTES ---
ventana = tk.Tk()
ventana.title("Ahorcado con Imágenes")
ventana.geometry("400x500")

# Cargar las imágenes
imagenes = []
try:
    for i in range(8): # Cargamos 8 imágenes, de 0 a 7 errores
        img = Image.open(f"imagenes_ahorcado/ahorcado_{i}.png").resize((200, 200))
        imagenes.append(ImageTk.PhotoImage(img))
except FileNotFoundError:
    messagebox.showerror("Error de Archivos", "No se encontraron las imágenes en la carpeta 'imagenes_ahorcado'. Asegúrate de que existan de 'ahorcado_0.png' a 'ahorcado_7.png'.")
    ventana.destroy()

# Si las imágenes se cargaron correctamente, creamos el resto de la interfaz
if imagenes:
    label_imagen = tk.Label(ventana, image=imagenes[0])
    label_imagen.pack(pady=10)

    label_palabra = tk.Label(ventana, text=" ".join(palabra_mostrada), font=("Helvetica", 24, "bold"))
    label_palabra.pack(pady=20)

    label_intentos = tk.Label(ventana, text=f"Quedan {intentos_restantes} intentos", font=("Helvetica", 14))
    label_intentos.pack(pady=10)

    entry_letra = tk.Entry(ventana, width=3, font=("Helvetica", 18), justify='center')
    entry_letra.pack(pady=5)
    entry_letra.bind("<Return>", lambda event: verificar_letra())

    boton_adivinar = tk.Button(ventana, text="Adivinar", command=verificar_letra, font=("Helvetica", 12))
    boton_adivinar.pack(pady=10)

    ventana.mainloop()