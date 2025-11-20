import tkinter as tk 
ventana = tk.Tk()
ventana.title("ejemplo boton")
ventana.geometry("400x500")
ventana.configure(bg='lightblue')

etiqueta = tk.Label(ventana, text='hola soy un label')
etiqueta.pack()

boton = tk.Button(ventana, text='presiona aqui')
boton.pack()

def cambiar_testo():
	print("!boton presionado")


boton.config(command=cambiar_testo)




ventana.mainloop()
cambiar_testo()