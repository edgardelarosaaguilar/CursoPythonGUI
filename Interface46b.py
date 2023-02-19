
#Desarrollado por Edgar de la Rosa Aguilar
from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Muestra Widgets")

        for r in range(2):
            self.master.rowconfigure(r)    
        for c in range(2):
            self.master.columnconfigure(c)

        Frame1 = Frame(master,relief=RAISED,borderwidth=6)
        Frame1.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 
        
        Frame2 = Frame(master,relief=RAISED,borderwidth=6)
        Frame2.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, sticky = W+E+N+S)
        

        Frame3 = Frame(master)
        Frame3.columnconfigure=3
        #row=2 porque esta en el renglon 2 del frame prinicipal=master
        Frame3.grid(row = 2, column = 0, rowspan = 2, columnspan = 1, sticky = W+E+N+S)

        
        Frame4 = Frame(master)
        Frame4.grid(row = 0, column = 1, padx=(50,50),pady=(10,10))
        Frame4.rowconfigure(0,weight=1)
        Frame4.columnconfigure(0,weight=1)

        Frame5 = Frame(master)
        Frame5.rowconfigure(3)
        Frame5.columnconfigure(1)
        Frame5.grid(row = 1, column = 1, rowspan = 1, columnspan = 1, sticky = W+E+N+S)


        #Componente vacío para dar apariencia de separación
        Label(Frame1, text=" ").grid(column=0,row=0)

        labelNombre = Label(Frame1, text="Nombre:    ").grid(column=0,row=1)
        textboxNombre = Entry(Frame1, text="Escriba nombre",width=40)
        textboxNombre.grid(column=1,row=1)

        #Componente vacío para dar apariecncia de separación
        Label(Frame1, text=" ").grid(column=0,row=2)

        labelPaterno = Label(Frame1, text="A. Paterno:").grid(column=0, row=3)
        textboxPaterno = Entry(Frame1, text="Escriba Apellido Paterno",width=40)
        textboxPaterno.grid(column=1,row=3)

        #Componente vacío para dar apariecncia de separación
        Label(Frame1, text=" ").grid(column=0,row=4)

        labelMaterno = Label(Frame1, text="A. Materno:").grid(column=0, row=5)
        textboxMaterno = Entry(Frame1, text="Escriba Apellido Materno",width=40)
        textboxMaterno.grid(column=1,row=5)

        #Componente vacío para dar apariecncia de separación
        Label(Frame1, text=" ").grid(column=0,row=6)

        labelCorreo= Label(Frame1, text="Correo:       ").grid(column=0, row=7)
        textboxCorreo = Entry(Frame1, text="Escriba Correo",width=40)
        textboxCorreo.grid(column=1,row=7)

        #Componente vacío para dar apariecncia de separación
        Label(Frame1, text=" ").grid(column=0,row=8)

        labelMovil = Label(Frame1, text="Móvil:          ").grid(column=0, row=9)
        textboxMovil = Entry(Frame1, text="Escriba Correo",width=40)
        textboxMovil.grid(column=1,row=9)

        #Componente vacío para dar apariecncia de separación
        #Label(Frame2, text=" ").grid(column=0,row=0)

        #Llenado del Frame 2
        label = Label(Frame2,text="Aficiones:").grid(column=1,row=1)
        #Componente vacío para dar apariecncia de separación
        Label(Frame2, text=" ").grid(column=0,row=2)

        chkBotonMusica = Checkbutton(Frame2, text="Leer                              ").grid(column=1,row=3,columnspan=1,sticky = W+E+N+S)
        chkBotonLeer = Checkbutton(Frame2, text="Musica                              ").grid(column=3,row=3,columnspan=1,sticky = W+E+N+S)
        chkBotonVideojuegos = Checkbutton(Frame2, text="Videojuegos").grid(column=5,row=3,columnspan=1,sticky = W+E+N+S)

        btnGuardar = Button(Frame3,text="Guardar")
        btnGuardar.grid(row=0,column=0)
        #Componente vacío para dar apariecncia de separación
        Label(Frame3, text="                                                                   ").grid(column=1,row=0)
        btnCancelar = Button(Frame3,text="Cancelar")
        btnCancelar.grid(row=0,column=2)

        rbEstudiante = Radiobutton(Frame4,text="Estudiante")
        #rbEstudiante.grid(column=2,row=0)
        rbEstudiante.grid(column=2,row=2, sticky=W)
        rbEmpleado = Radiobutton(Frame4,text="Empleado")
        #rbEmpleado.grid(column=2,row=1)
        rbEmpleado.grid(column=2,row=3, sticky=W)
        rbDesempleado = Radiobutton(Frame4,text="Desempleado")
        #rbDesempleado.grid(column=2,row=2)
        rbDesempleado.grid(column=2,row=4, sticky=W)
       
    
        #Crear comobobox
        #Tipo de letra para combobox
        fontStyle = ("cooper",17, "bold")
        variableEstadoSeleccionado = tk.StringVar()
        estadosMexico = [
                            "Estados (32)",
                            "Aguascalientes",
                            "BC",
                            "BCS",
                            "Sonora",
                            "Sinaloa",
                            "Nayarit",
                            "Chichuahua",
                            "Coahuila",
                            "Nuevo León",
                            "Tamaulipas",
                            "San Luis Potosí",
                            "Zacatecas",
                            "Durango",
                            "Jalisco",
                            "Guanajuato",
                            "Colima",
                            "Michoacan",
                            "Guerrero",
                            "México",
                            "Queretaro",
                            "Hidalgo",
                            "Morelos",
                            "Tlaxcala",
                            "Puebla",
                            "Oaxaca",
                            "Chiapas",
                            "Tabasco",
                            "Campeche",
                            "Yucatán",
                            "Quintana Roo"
                        ]
        
        estadosCombobox = ttk.Combobox(Frame5, values = [
                            "Estados (32)",
                            "Aguascalientes",
                            "BC",
                            "BCS",
                            "Sonora",
                            "Sinaloa",
                            "Nayarit",
                            "Chichuahua",
                            "Coahuila",
                            "Nuevo León",
                            "Tamaulipas",
                            "San Luis Potosí",
                            "Zacatecas",
                            "Durango",
                            "Jalisco",
                            "Guanajuato",
                            "Colima",
                            "Michoacan",
                            "Guerrero",
                            "México",
                            "Queretaro",
                            "Hidalgo",
                            "Morelos",
                            "Tlaxcala",
                            "Puebla",
                            "Oaxaca",
                            "Chiapas",
                            "Tabasco",
                            "Campeche",
                            "Yucatán",
                            "Quintana Roo"
                        ], font = fontStyle, width=10)
        #Otra opcion de cargar los valores al combobox
       # estadosCombobox['values']=('Estados (32)','Aguascalientes',
        #                   'BCS',
       #                    'BC',
         #                  'Sonora',
          #                 'Sinaloa',
           #                'Nayarit',
            #               'Chichuahua',
             #              'Coahuila',
              #             'Nuevo León',
               #            'Tamaulipas',
                #           'San Luis Potosí',
                 #          'Zacatecas',
                  #         'Durango',
                   #       'Jalisco',
                    #       'Guanajuato',
                    #       'Michoacan',
                   #        'Colima',
                   #        'Guerrero',
                    #       'México',
                     #      'Queretaro',
                      #     'Hidalgo',
         #                  'Morelos',
          #                 'Tlaxcala',
           #                'Puebla',
            #               'Oaxaca',
             #              'Chiapas',
              #             'Tabasco',
               #            'Campeche',
                #           'Yucatán',
                 #          'Quintana Roo')
        
        estadosCombobox.grid(column=2,row=2, sticky="NSEW",padx=100,pady=50)
        estadosCombobox.current(0)
        print(estadosCombobox.current(), estadosCombobox.get())




root = Tk()
root.geometry("755x440")
app = Application(master=root)
app.mainloop()