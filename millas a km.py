import tkinter as tk
from tkinter import messagebox

def convertir_millas_a_km():
    try:
        millas = float(entrada_millas.get())
        km = millas * 1.60934
        resultado_label.config(text=f"{km:.2f} Km")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")


ventana = tk.Tk()
ventana.title("Calculadora de Millas a Km")


entrada_millas = tk.Entry(ventana)
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_millas_a_km)
resultado_label = tk.Label(ventana, text="Resultado en Km")


entrada_millas.pack()
boton_convertir.pack()
resultado_label.pack()


ventana.mainloop()
