from tkinter import Tk, Label, Entry, Button, StringVar, ttk, messagebox, CENTER

def convertir():
    try:
        valor = float(input_temp.get())  # Obtener el valor ingresado
        unidad_origen = combobox_origen.get()  # Obtener la unidad de origen
        unidad_destino = combobox_destino.get()  # Obtener la unidad de destino

        if unidad_origen == unidad_destino:
            resultado.set(f"{valor:.2f} {unidad_destino}")
        elif unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
            resultado.set(f"{(valor * 9/5) + 32:.2f} °F")
        elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
            resultado.set(f"{valor + 273.15:.2f} K")
        elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
            resultado.set(f"{(valor - 32) * 5/9:.2f} °C")
        elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
            resultado.set(f"{((valor - 32) * 5/9) + 273.15:.2f} K")
        elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
            resultado.set(f"{valor - 273.15:.2f} °C")
        elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
            resultado.set(f"{((valor - 273.15) * 9/5) + 32:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar solo números.")

# Configuración de la ventana principal
ventana = Tk()
ventana.title("Convertidor de Temperatura V0.1")
ventana.geometry("400x300")
ventana.configure(bg="#87CEEB")  # Color azul vintage
ventana.resizable(False, False)

# Estilo del título
titulo = Label(ventana, text="Convertidor Temperatura", bg="#87CEEB", fg="white", font=("Courier", 16, "bold"))
titulo.pack(pady=10)

# Entrada de temperatura
input_temp = StringVar()
entrada = Entry(ventana, textvariable=input_temp, font=("Courier", 12), justify=CENTER)
entrada.pack(pady=5)

# Combobox de origen
combobox_origen = ttk.Combobox(ventana, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Courier", 10))
combobox_origen.set("Celsius")
combobox_origen.pack(pady=5)

# Combobox de destino
combobox_destino = ttk.Combobox(ventana, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Courier", 10))
combobox_destino.set("Fahrenheit")
combobox_destino.pack(pady=5)

# Botón para convertir
boton_convertir = Button(ventana, text="Convertir", command=convertir, bg="#4682B4", fg="white", font=("Courier", 12, "bold"))
boton_convertir.pack(pady=10)

# Resultado
resultado = StringVar()
etiqueta_resultado = Label(ventana, textvariable=resultado, bg="#87CEEB", fg="black", font=("Courier", 14))
etiqueta_resultado.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()