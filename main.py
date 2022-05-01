from ClaseEmail import Email
from ClaseMenu import Menu

if __name__=='__main__':
    b=True
    NuevoEmail=Email()
    NuevoMenu=Menu()
    print("__Menu__")
    while b!=False:
        Num=int(input("Elige una opcion:\n1_crear una instancia de la clase Email\n2_Cambiar Contrasena\n3_Crear un correo a partir de una dirreccion\n4_Leer un archivo y identificar si se repite el id\n5_Salir\n"))
        if(Num!=5):
            NuevoMenu.OpcionesMenu(Num,NuevoEmail)
        else:
            print("Se salio con exito")
            b=False



