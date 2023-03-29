
from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter as tk
import random








#Funcion para la hora del reloj digital
def reloj_digital():
    etiqueta_hm.config(text= strftime ("%H:%M"))
    etiqueta_s.config(text= strftime ("%S"))
    etiqueta_fecha.config(text= strftime ("%A, %d/%m/%Y"))
   
    if cb[0] == 100:
        boton_cargador.config(fg="yellow")
    
    funcion_cargar_texto()

    etiqueta_s.after(1000, reloj_digital)


#FUNCION DE BLUETOOTH
def bluetooth():
       
    contador_blue = [0]

    # Creamos la lista de dispositivos móviles cercanos
    devices = ["iPhone de Esteban", "iPhone de Carolina", "iPhone de Alberto", "iPhone de Luismi","Redmi Note 11S"]

    # Creamos la lista de dispositivos cercanos en la interfaz
    listbox = tk.Listbox(app, width=50, height=10)
    for device in devices:
        listbox.insert(tk.END, device)
    listbox.place(x= 200, y = 200)

    # Función que se ejecuta al pulsar el botón "Enlazar"
    def enlazar():
        if contador_blue[0] == 0:
            # Obtenemos el elemento seleccionado de la lista
            seleccionado = listbox.get(tk.ACTIVE)

          

            mensaje_conectado = Label(app, background="white", text="Conectado a {} correctamente !!".format(seleccionado))
            mensaje_conectado.place(x= 250, y = 400)
            contador_blue[0] = 1

        
            #nuevo boton
            button.destroy()

            def borrarblue():
                listbox.destroy()
                mensaje_conectado.destroy()
                button_continuar.destroy()
                luz()

            button_continuar = tk.Button(app, text="Continuar", command=borrarblue)
            button_continuar.place(x= 350, y = 450)

            

            

           



    # Configuramos el botón de enlazar
    button = tk.Button(app, text="Enlazar", command=enlazar)
    button.place(x= 350, y = 400)

    
   





#Funcion luz
def luz():

    
    if cb[0] <= 80:
        #ENCENDER
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))
        etiqueta_bateria.place(x = 600,y = 750)

    elif primera_vez[0] == True:

        #grado de encendido
        primera_vez[0] = False

        # crear los labels y los inputs
        nombre_label = tk.Label(app, text="Nombre:")
        nombre_input = tk.Entry(app)

        
        apellido_label = tk.Label(app, text="Apellidos:")
        apellido_input = tk.Entry(app)

        nacimiento_label = tk.Label(app, text="Año de nacimiento:")
        nacimiento_input = tk.Entry(app)

        altura_label = tk.Label(app, text="Altura:")
        altura_input = tk.Entry(app)

        peso_label = tk.Label(app, text="Peso:")
        peso_input = tk.Entry(app)

        localizacion_label = tk.Label(app, text="Localización:")
        localizacion_input = tk.Entry(app)

        actividades_label = tk.Label(app, text="Nº de actividades semanales:")
        actividades_input = tk.Entry(app)

        deportes_label = tk.Label(app, text="Deportes favoritos:")
        deportes_input = tk.Entry(app)

        # agregar los widgets a la ventana principal
        espacio1 = Label(app, text="    ", background="black")
        espacio1.pack()

        nombre_label.pack()
        nombre_input.pack()
        espacio2 = Label(app, text="    ", background="black")
        espacio2.pack()

        apellido_label.pack()
        apellido_input.pack()
        espacio3 = Label(app, text="    ", background="black")
        espacio3.pack()

        nacimiento_label.pack()
        nacimiento_input.pack()
        espacio4 = Label(app, text="    ", background="black")
        espacio4.pack()

        altura_label.pack()
        altura_input.pack()
        espacio5 = Label(app, text="    ", background="black")
        espacio5.pack()

        peso_label.pack()
        peso_input.pack()
        espacio6 = Label(app, text="    ", background="black")
        espacio6.pack()

        localizacion_label.pack()
        localizacion_input.pack()
        espacio7 = Label(app, text="    ", background="black")
        espacio7.pack()

        actividades_label.pack()
        actividades_input.pack()
        espacio8 = Label(app, text="    ", background="black")
        espacio8.pack()

        deportes_label.pack()
        deportes_input.pack()

        espacio9 = Label(app, text="    ", background="black")
        espacio9.pack()

        
        #Funcion que borra el imput y empieza el reloj
        def destruir_widgets():
            
            nombre_label.destroy()
            nombre_input.destroy()
            apellido_label.destroy()
            apellido_input.destroy()
            nacimiento_label.destroy()
            nacimiento_input.destroy()
            altura_label.destroy()
            altura_input.destroy()
            peso_label.destroy()
            peso_input.destroy()
            localizacion_label.destroy()
            localizacion_input.destroy()
            actividades_label.destroy()
            actividades_input.destroy()
            deportes_label.destroy()
            deportes_input.destroy()
            limpiar_btn.destroy()

            espacio1.destroy()
            espacio2.destroy()
            espacio3.destroy()
            espacio4.destroy()
            espacio5.destroy()
            espacio6.destroy()
            espacio7.destroy()
            espacio8.destroy()
            espacio9.destroy()
        
            bluetooth()

        limpiar_btn = tk.Button(app, text="EMPEZAR", command=destruir_widgets)
        limpiar_btn.pack()
        
        
        
    else:

        label_imagen_negro.destroy()

        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))

        etiqueta_bateria.place(x = 600,y = 750)

        etiqueta_bateria.destroy()

        #HORA
        frame_hora.pack()
        frame_hora.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #FECHA
        etiqueta_fecha.pack(anchor="center")


        #Funcion para que cambie a negro
        def cambiar_color_a_negro():
            app.config(bg='black')
            Label_imagen_usb.config(background= "black")

        #Cambiamos a azul claro
        app.config(background= "light blue")
        Label_imagen_usb.config(background= "light blue")

        #Indicamos tiempo de espera
        app.after(3000, cambiar_color_a_negro)




#Funcion que cambia la imagen del cargador

def cambiar_imagen_cargador():
    if cargando[0] == False:
        Label_imagen_usb.config(image=imagen_usb_conectado)
        boton_cargador.config(fg="green")

        cargando[0] = True
        app.after(3000, funcion_cargar)


    elif cargando[0] == True:
        # Crear un widget Label y asignarle la imagen
        label_imagen_negro = Label(app, image=imagen_negro, background="black")
        label_imagen_negro.place(x= 180, y= 730)  


        Label_imagen_usb.config(image=imagen_usb)
        boton_cargador.config(fg="yellow")

        cargando[0] = False
        

    
#Funcion cargar
 

def actualizar_bateria():
    if cargando[0] == True:
      
        if cb[0] == 100:
            etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA: {} %".format(cb[0]))
    
        elif cb[0] < 10:
            etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:      {} %".format(cb[0]))

        else:
            etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))

        etiqueta_bateria.place(x = 600,y = 750)
        
        if cb[0] == 51:
            cb[0] = 60

        elif cb[0] < 100:
            cb[0] += 5
        

        app.after(2000, actualizar_bateria)

def funcion_cargar():



    if cb[0] >= 100:
        cb[0] = 100
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA: {} %".format(cb[0]))
    
    elif cb[0] < 10:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:      {} %".format(cb[0]))

    else:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))
 


    etiqueta_bateria.place(x = 600,y = 750)
    app.after(500, actualizar_bateria)

def funcion_cargar_texto():



    if cb[0] >= 100:
        cb[0] = 100
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA: {} %".format(cb[0]))
    
    elif cb[0] < 10:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:      {} %".format(cb[0]))

    else:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))
 


    etiqueta_bateria.place(x = 600,y = 750)
    




#Funcion descargar

def descargar():
    

    cb[0] = cb[0] - 5

    if cb[0] < 0:
        cb[0] = 0

    if cb[0] == 100:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA: {} %".format(cb[0]))
    
    elif cb[0] < 10:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:      {} %".format(cb[0]))

    else:
        etiqueta_bateria = Label(app,font=("digitalk", 15),text ="BATERIA:   {} %".format(cb[0]))
 
    etiqueta_bateria.place(x = 600,y = 750)
    etiqueta_s.after(30000, descargar)


    
   


app = Tk ()

#VARIABLES

cargando = [False]
primera_vez=[True]

 # Cargar la imagen
imagen_sol = PhotoImage(file="sol.png")

imagen_nube = PhotoImage(file="nube.png")

imagen_negro = PhotoImage(file= "negro.png")
label_imagen_negro = Label(app, image=imagen_negro, background="black")
label_imagen_negro.place(x= 180, y= 730)  

def llamando_carga_solar():
    
    carga_solar() 
   
    app.after(5000, llamando_carga_solar)

def carga_solar():
    
    label_imagen_nube = Label()
    label_imagen_sol = Label()
    label_imagen_negro = Label()
   
    
    if cargando[0] == False  and primera_vez[0] == False and cb[0] < 100:
        label_imagen_negro.destroy()
        label_imagen_nube.destroy()
        label_imagen_sol.destroy()

        #Esta amaneciendo
        if strftime("%H") == "06" or strftime("%H") == "07" or strftime("%H") == "08": 

            luz = "amaneciendo"
            # Crear un widget Label y asignarle la imagen
            label_imagen_sol = Label(app, image=imagen_sol, background="black")
            label_imagen_sol.place(x= 195, y= 728)

            cb[0] =  cb[0] + 1


        #Es de dia 
        elif  strftime("%H") == "09" or strftime("%H") == "10" or strftime("%H") == "11" or strftime("%H") == "12" or strftime("%H") == "13" or strftime("%H") == "14" or strftime("%H") == "15":
            
            
            numero_aleatorio = random.randint(0, 1)
            
            #soleado
            if numero_aleatorio == 0:
                luz = "dia soleado"

                # Crear un widget Label y asignarle la imagen
                label_imagen_sol = Label(app, image=imagen_sol, background="black")
                label_imagen_sol.place(x= 195, y= 728)

                cb[0] =  cb[0] + 5

            #nublado
            elif numero_aleatorio == 1:
                luz = "dia nublado"
                
                cb[0] =  cb[0] + 2

            # Crear un widget Label y asignarle la imagen
                label_imagen_nube = Label(app, image=imagen_nube, background="black")
                label_imagen_nube.place(x= 195, y= 730) 



        elif strftime("%H") == "16" or strftime("%H") == "17" or strftime("%H") == "18" or strftime("%H") == "19" or strftime("%H") == "20":
            
            numero_aleatorio = random.randint(0, 1) 
            
            #soleado
            if numero_aleatorio == 0:
                luz = "tarde soleada"

                cb[0] =  cb[0] + 3

                # Crear un widget Label y asignarle la imagen
                label_imagen_sol = Label(app, image=imagen_sol, background="black")
                label_imagen_sol.place(x= 195, y= 728)




            #nublado
            elif numero_aleatorio == 1:
                luz = "tarde nublada"

                cb[0] =  cb[0] + 1

                # Crear un widget Label y asignarle la imagen
                label_imagen_nube = Label(app, image=imagen_nube, background="black")
                label_imagen_nube.place(x= 195, y= 730)  

        else:
            luz = "noche"

        if luz != "noche":
            boton_cargador.config(fg="green")

        

    else:
       
        # Crear un widget Label y asignarle la imagen
        label_imagen_negro = Label(app, image=imagen_negro, background="black")
        label_imagen_negro.place(x= 180, y= 728)  


   








#Titulo
app.title('Reloj digital')

#Modificar si es ecalable
app.resizable(False,False)

#Fondo
app.config(bg= 'black')

app.geometry('800x800')



#Frame de la hora y fecha
frame_hora = Frame(app, width="800", height="800")


#Etiqueta horas y minutos
etiqueta_hm = Label(frame_hora, font=("digitalk",70),text="H:M")
etiqueta_hm.grid(row=0, column = 0)

#Etiqueta segundos
etiqueta_s = Label(frame_hora, font=("digitalk", 30),text = "s")
etiqueta_s.grid(row=0, column=1, sticky="n")

#Etiqueta fecha
etiqueta_fecha = Label(font=("digitalk", 30),text ="dia d/m/aaaa")


#Bonton light
boton_luz = tk.Button(app, text="Light", font=("digitalk", 12), borderwidth=8,command=luz)
boton_luz.place(x = 10,y = 100)





#Imagen usb

imagen_usb = PhotoImage(file="usb_hembra.png")
imagen_usb_conectado = PhotoImage(file="usb_hembra_conectado.png")

Label_imagen_usb = Label(app,image=imagen_usb, background="black")
Label_imagen_usb.place(x= 280, y= 730)


#Boton 

boton_cargador = tk.Button(app, text="C", font=("digitalk", 15), command=cambiar_imagen_cargador,fg="yellow" ,bg="black", borderwidth=0)
boton_cargador.place(x= 490, y= 750)



#BATERIA

#carga bateria

cb = [51]


#tiempo de carga
t = 2


#Descargar
app.after(10000, descargar)





reloj_digital()

carga_solar()
llamando_carga_solar()

app.mainloop()
