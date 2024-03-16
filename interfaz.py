from tkinter import scrolledtext
import tkinter as tk
from Gramatica import analizar_entrada  

def analizar():
    entrada = txt_entrada.get("1.0", tk.END).strip()
    resultado = analizar_entrada(entrada)
    txt_resultado.delete("1.0", tk.END)
    if "Error de sintaxis" in resultado:
        txt_resultado.config(fg="red")  
    else:
        txt_resultado.config(fg="black") 
    txt_resultado.insert(tk.INSERT, resultado)

#ventana principal
ventana = tk.Tk()
ventana.title("Analizador Sintáctico")
ventana.geometry("600x400")
ventana.configure(bg="#333333") 

# marco principal       
frame_principal = tk.Frame(ventana, bg="#87CEEB")  
frame_principal.pack(pady=20)

# widget de entrada
lbl_entrada = tk.Label(frame_principal, text="Texto a analizar:", font=("Arial", 12), bg="#87CEEB")  
lbl_entrada.grid(row=0, column=0, padx=10, pady=5, sticky="w")

txt_entrada = scrolledtext.ScrolledText(frame_principal, width=60, height=10, wrap=tk.WORD)
txt_entrada.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
txt_entrada.insert(tk.INSERT, 'alter table columna drop column')

# boton para analizar
btn_analizar = tk.Button(frame_principal, text="Analizar", command=analizar, bg="#007bff", fg="white", font=("Arial", 12))  
btn_analizar.grid(row=2, column=0, padx=10, pady=5)

# salida para resultados
lbl_resultado = tk.Label(frame_principal, text="Resultado del análisis:", font=("Arial", 12), bg="#87CEEB") 
lbl_resultado.grid(row=3, column=0, padx=10, pady=5, sticky="w")

txt_resultado = scrolledtext.ScrolledText(frame_principal, width=60, height=10, wrap=tk.WORD)
txt_resultado.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

ventana.mainloop()
