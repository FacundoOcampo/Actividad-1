class Email:
     __Id= str
     __Dom= str
     __TipoDom= str
     __Contra= str
     def __init__ (self, Id=None,Dom=None,TipoDom=None,Contra=None):
         self.__Id=Id
         self.__Dom=Dom
         self.__TipoDom=TipoDom
         self.__Contra=Contra
     def RetornaMail (self):
         return (self.__Id + "@" + self.__Dom + "." + self.__TipoDom)
     def getDominio(self):
         return self.__Dom
     def crearCuenta(self,Correo,Contra):
         if(Correo.find('@')!=-1):
             AuxC=Correo.split("@")
             Usuario=AuxC[0]
             if(Correo.find('.')!=-1):
                 AuxD=AuxC[1].split(".")
                 Dominio=AuxD[0]
                 TipoD=AuxD[1]
                 self.__init__(Usuario,Dominio,TipoD,Contra)
                 print("\n")
             else:
                 print('No se encontro el "."\n')
         else:
             print('No se encontro el "@"\n')
     def CambiarContra(self):
         aux=input("Ingrese su contrasena: ")
         while self.__Contra!=aux:
             aux=input("Contraseña incorrecta, intente nuevamente:")
         self.__Contra=input("Ingrese la contraseña nueva: ")
         print("Contraseña cambiada con exito\n")
