from tkinter import *
from tkinter import ttk

class SessionInicio:

    def __init__(self, raiz):

        raiz.title("Inicio de Sesión")
        
        raiz.rowconfigure(0, weight=3)
        raiz.columnconfigure(0, weight=1)
        #Configura el tamaño de la form
        #raiz.configure(width=300, height=200)
        self.usuario = StringVar()
        self.contrasena = StringVar()

        mainframe = ttk.Frame(raiz, padding= "3 3 12 12")
        mainframe.grid(column=0, row=0, rowspan=6, padx=5, pady=5)#sticky=(N , W, E, S))
        #Componente vacío para dar apariecncia de separación
        ttk.Label(mainframe, text=" ").grid(column=3,row=2)
        
        usuario_entrada = ttk.Entry(mainframe, width=20, textvariable=self.usuario)
        usuario_entrada.grid(column=4, row=3, sticky=(W, E))
        #Etiqueta Usuario
        ttk.Label(mainframe, text="Usuario: ").grid(column=3,row=3)
        #Componente vacío para dar apariecncia de separación
        ttk.Label(mainframe, text=" ").grid(column=3,row=4)
        #Configuración del Entry donde se escribe la contraseña tiene como parámetro contrasena
        #que corresponde a la variable donde guardará el valor escrito 
        contrasena = ttk.Entry(mainframe, width=20, textvariable=self.contrasena)
        contrasena.grid(column=4, row=5, sticky=(W, E))
        #Etiqueta Contraseña
        ttk.Label(mainframe, text="Contraseña: ").grid(column=3,row=5, sticky=E)
        #Componente vacío para dar apariecncia de separación
        ttk.Label(mainframe, text=" ").grid(column=3,row=6)
        #Componente Boton: tiene como parámetro text que se le configura el letrero o texto a mostrar en el boton
        #comand=es la función que se invocará al presionar el boton
        ttk.Button(mainframe, text="Ingresar", command=self.autentificar).grid(column=4, row=7, sticky=E)

    def autentificar(self):
        print("Intentará autentificar")


raiz = Tk()
#Tamaño de ventana
#raiz.geometry('200x200')
SessionInicio(raiz)
raiz.mainloop()