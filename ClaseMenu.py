import csv

class Menu:
    __Num=int
    def __init__(self):
        self.__Num=int
    def OpcionesMenu(self,Num,CorreoAux):
        if(Num==1):
            self.Opcion1(CorreoAux)
        elif(Num==2):
            self.Opcion2(CorreoAux)
        elif(Num==3):
            self.Opcion3(CorreoAux)
        elif(Num==4):
            self.Opcion4()
        else:
            print("Valor ingresado incorrecto")
    def Opcion1(self,CorreoAux):
        Nom=input("Ingrese su nombre")
        Correo=input("Ingrese su correo")
        Contra=input("Ingrese su contraseña")
        CorreoAux.crearCuenta(Correo,Contra)
        print("Estimado {} te enviaremos tus mensajes aa la direccion {}".format(Nom,CorreoAux.RetornaMail()))
    def Opcion2(self,CorreoAux):
        CorreoAux.CambiarContra()
    def Opcion3(self,CorreoAux):
        aux=input('Ingrese la dirreccion de correo(su contraseña sera "Contraseña123)"')
        auxC="Contraseña123"
        CorreoAux.crearCuenta(aux,auxC)
    def Opcion4(self):
        cont=0
        path_archivo="Libreria.csv"
        Archivo = open(path_archivo,"r")
        reader = csv.reader(Archivo,delimiter=",")
        id=input("Ingrese el identificador de la cuenta")
        for fila in reader:
            if fila[0]==id:
                cont+=1
        if cont>1:
            print("El identificador se repite")
        else:
            print("El identificador no se repite")

