from tkinter import *

ventana = Tk()
ventana.title("Estructura de Datos Avanzados")
ventana.geometry("470x470")
scroll=Scrollbar(ventana)
scroll.pack(side=RIGHT, fill=Y)
etiqueta2=Listbox(ventana, yscrollcommand=scroll.set)

#variables
nombre=StringVar()
texto=StringVar()
conta=StringVar()
#Funciones
def file():# Crea el archivo
    txt="Inventarios"
    archivo=open(txt,"a")
    texto=nombre.get()
    archivo.write(texto)
    archivo.write("\n")
    archivo.close()

def consultar(): #importa la base de datos
    y1=90
    txt="Inventarios"
    archivo=open(txt,"r")
    for linea in archivo.readlines():
        etiqueta2= Label(ventana,text=linea).place(x=10,y=y1)
       #scroll.config(command=Listbox.yview)
        y1=y1 + 18
    archivo.close()

def OrdenarIn(): #importa la base de datos
    y1=90
    txt="InvA-Z"
    archivo=open(txt,"r")
    for linea in archivo.readlines():
        etiqueta2= Label(ventana,text=linea).place(x=10,y=y1)
       #scroll.config(command=Listbox.yview)
        y1=y1 + 18
    archivo.close()
    
def OrdenarDe(): #importa la base de datos
    y1=90
    txt="InvZ-A"
    archivo=open(txt,"r")
    for linea in archivo.readlines():
        etiqueta2= Label(ventana,text=linea).place(x=10,y=y1)
       #scroll.config(command=Listbox.yview)
        y1=y1 + 18
    archivo.close()

def buscar():
    txt="inventarios" #Frecuencia
    with open (txt) as archivo:
        contador = {}  # guarda el numero de repeticiones de una palabra
        for linea in archivo:
            palabras = linea.split() #Sirve para separar las lienas en palabras por espacio en blanco
            for palabra in palabras:
                if palabra not in contador:   # el "no" es un operador logico en python que devolvera True si la expresion es False
                    contador[palabra]=1
                else:
                    contador[palabra]+=1
    archivo.close()

    for palabra in sorted(contador, key=contador.get,reverse=True):
        if palabra == nombre.get():
            conta.set(contador[palabra])
            etiqueta2= Label(ventana,text=" ")

            etiqueta2= Label(ventana,text="Palabra: " + palabra + "      " + conta.get() + " veces repetidas").place(x=10,y=70)
   
#Etiquetas
etiqueta1 =Label(ventana,text="Escribe el nombre").place(x=10,y=10)

#Entrada
Entrada1 =Entry(ventana,textvariable=nombre).place(x=120,y=10)
                                                   
#Botones
boton1 = Button(ventana,text="Registrar",command=file).place(x=10,y=40)                                                  
boton2 = Button(ventana,text="Consultar",command=consultar).place(x=70,y=40)                                                  
boton3 = Button(ventana,text="Buscador",command=buscar).place(x=135,y=40)
boton4 = Button(ventana,text="Ordenar Ascendente",command=OrdenarIn).place(x=197,y=40)
boton4 = Button(ventana,text="Ordenar Descendente",command=OrdenarDe).place(x=320,y=40)

