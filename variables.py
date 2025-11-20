import time
import tkinter as tk 
ventana = tk.Tk()
ventana.title("ejemplo reloj")
ventana.geometry("400x500")
ventana.configure(bg='lightblue')



etiqueta = tk.Label(ventana, text='hola soy un label')
etiqueta.pack()

def actualizar_hora():
	etiqueta.config (text=time.strftime("14:14:15"))
	etiqueta.after(1000,actualizar_hora)
	etiqueta.config(fg='blue',bg='lightgreen', font=("Arial",16, 'bold'))
actualizar_hora()






