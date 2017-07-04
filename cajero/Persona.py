import csv
class Persona():
     def __init__(self):
        self.nombre = None
        self.apellido = None
        self.dni = None
        self.edad = None
       

     def personas(self,cliente):  
        with open ('personas.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            
            
            for row in reader:
                if row['Numcliente'] == cliente:
                    
                
                    self.nombre= row['Nombre']
                    self.apellido =row['Apellido']
                    self.dni =row['DNI']
                    self.edad =row['Edad']
                    
                   
                    
                    return "continuar"