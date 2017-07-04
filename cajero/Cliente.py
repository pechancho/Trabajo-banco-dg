import csv
from Persona import *
class Cliente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.numcliente = None
        self.fechaalta = None
        self.fechabaja= None
         
    def numcliente(self,cliente):  
        with open ('personas.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            
            
            for row in reader:
                if row['Numcliente'] == cliente:
                    self.numcliente = row['Numcliente']
                    self.fechaalta = row['fechaalta']
                    self.fechabaja = row['fechabaja']
                    
                    print self.numcliente
                    print Persona.nombre
                    print Persona.apellido
                    print Persona.edad
                    print Persona.dni    
                    print self.fechaalta
                    print self.fechabaja
                    

    def activo():
        if self.fechabaja == None:
            print "el cliente esta inactivo"
        else:
            print "el cliente esta activo"

         
                    
 
        
   
               
            
           