import tkinter as tk

def convertir_divisas():
    monto = float(entrada_monto.get())
    tasa_cambio = float(entrada_tasa.get())
    resultado = monto * tasa_cambio
    resultado_label.config(text=f"{resultado:.2f} en la divisa destino")


ventana = tk.Tk()
ventana.title("Calculadora de Divisas")


entrada_monto = tk.Entry(ventana)
entrada_tasa = tk.Entry(ventana)
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_divisas)
resultado_label = tk.Label(ventana, text="Resultado en la divisa destino")

tk.Label(ventana, text="Monto en divisa origen").pack()
entrada_monto.pack()
tk.Label(ventana, text="Tasa de cambio").pack()
entrada_tasa.pack()
boton_convertir.pack()
resultado_label.pack()


ventana.mainloop()
