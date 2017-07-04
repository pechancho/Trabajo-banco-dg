import csv
class Cuenta():
    def __init__(self,cliente,cont):
        self.contrasenia=None
        with open ('cuentas.csv') as csvfile:
            reader = csv.DictReader(csvfile)
    
            for row in reader:
                if row['numcliente'] == cliente and row['contrasenia'] == cont:
                    self.numcliente=row['numcliente']
                    self.saldo=row['saldo']
                    self.contrasenia=row['contrasenia']
        if cont!=self.contrasenia:
            print "contrasenia incorrecta"
                   
                    
    def tienedinero(f):
        def nuevafuncion(self, *arg, **kwargs):
            #import pdb; pdb.set_trace()
            if int(arg[0])>int(self.saldo):
                print "no puede extraer  $", arg[0]
                print "su saldo es de $", self.saldo
            else:
                print "else"
                f(self,*arg, **kwargs)    

        return nuevafuncion
                
       
    def consultar(self):
        print self.saldo
            
    def agregar_din_cuenta(self,din): 
        self.saldo=int(self.saldo)+din
        print "se han agregado  $", din, "a su cuenta"
        print "saldo: ", self.saldo
   
    @tienedinero    
    def extraer_din_cuenta(self, din):
        self.saldo=int(self.saldo)-din
        print "se han extraido  $", din, "a su cuenta"        
        print "saldo: ", self.saldo
      