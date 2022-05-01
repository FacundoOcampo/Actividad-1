from ClaseEmail import Email
from ClaseMenuu import Menu

def Test():
    print("Datos Correctos:")
    NuevoTest=Email()
    print("       Informatica@gmail.com")
    NuevoTest.crearCuenta("Informatica@gmail.com","Contraseña1")
    print("       Facundo-Ocampo@Hotmail.com")
    NuevoTest.crearCuenta("Facundo-Ocampo@Hotmail.com","Contraseña2")
    print("       Prueba.123@gmail.com")
    NuevoTest.crearCuenta("Prueba.123@gmail.com","Contraseña3")
    print("\nDatos Incorrectos:")
    print("       Informaticagmail.com")
    NuevoTest.crearCuenta("Informaticagmail.com","Contraseña4")
    print("       Facundo-Ocampo@Hotmail")
    NuevoTest.crearCuenta("Facundo-Ocampo@Hotmail","Contraseña5")

if __name__=='__main__':
    b=True
    NuevoEmail=Email()
    NuevoMenu=Menu()
    Num=int(input("¿Quiere ejecutar el test?\n1_Si \ 2_No\n"))
    if(Num==1):
        Test()
    print("\n__Menu__")
    while b!=False:
        Num=int(input("Elige una opcion:\n1_crear una instancia de la clase Email\n2_Cambiar Contrasena\n3_Crear un correo a partir de una dirreccion\n4_Leer un archivo y identificar si se repite el id\n5_Salir\n"))
        if(Num!=5):
            NuevoMenu.OpcionesMenu(Num,NuevoEmail)
        else:
            print("Se salio con exito")
            b=False



