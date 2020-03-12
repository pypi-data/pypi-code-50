"""
Este es el módulo de Base de Datos
"""
import os
from libretronic import archivos
from tqdm import tqdm, trange
import time


def consulta_de_archivo(servidor,base,usuario,rutaDeScript,nombreConsulta):
    """Esta función consulta desde un archivo.sql a un servidor específico"""
    print('Consultando '+nombreConsulta+'.sql')
    archivoConsulta = os.path.join(rutaDeScript,nombreConsulta)
    Cadena='psql -h '+servidor+' -U '+usuario+' -d '+base+' -A -F"|" -f '+'\"'+archivoConsulta+'.sql" > "'+archivoConsulta+'.csv"'      
    os.system(Cadena)        
    #archivos.csv_to_xlsx(rutaDeScript+'\\',nombreConsulta+'.csv',nombreConsulta)

def consulta_de_archivo_v1(servidor,base,usuario,rutaDeScript,nombreConsulta):
    """Esta función consulta desde un archivo.sql a un servidor específico"""    
    archivoConsulta = os.path.join(rutaDeScript,nombreConsulta)
    Cadena='psql -h '+servidor+' -U '+usuario+' -d '+base+' -A -F"|" -f '+'\"'+archivoConsulta+'.sql" > "'+archivoConsulta+'.csv"'      
    os.system(Cadena)        
    #archivos.csv_to_xlsx(rutaDeScript+'\\',nombreConsulta+'.csv',nombreConsulta)

def consulta_de_lista(servidor,base,usuario,rutaDeScript,listadeConsultas):
    """Esta función realiza consultas a partir de un archivo.dat
    que a su ves contiene  una lista de consultas
    """
    print("Barriendo ",listadeConsultas)
    
    #archivoConsulta=rutaDeScript+'\\'+listadeConsultas
    archivoConsulta=os.path.join(rutaDeScript,listadeConsultas)
    infile = open(archivoConsulta,'r')
    Consultas = infile.readlines()
    infile.close()
    for nombreConsulta in Consultas:
        nombreConsulta=nombreConsulta.rstrip('\n')
        consulta_de_archivo(servidor,base,usuario,rutaDeScript,nombreConsulta)         

def consulta_de_lista_v1(servidor,base,usuario,rutaDeScript,listadeConsultas):
    """Esta función realiza consultas a partir de un archivo.dat
    que a su ves contiene  una lista de consultas
    """     
     
    archivoConsulta=os.path.join(rutaDeScript,listadeConsultas)
    infile = open(archivoConsulta,'r')
    Consultas = infile.readlines()
    infile.close()
    barra = tqdm(Consultas) 
    for nombreConsulta in barra:
        barra.set_description("Consultando %s" % dato)
        nombreConsulta=nombreConsulta.rstrip('\n')
        consulta_de_archivo_v1(servidor,base,usuario,rutaDeScript,nombreConsulta)         
