from django.http import HttpResponse
from django.template import Template, Context

#Se puede importar asi from django.template import loader
#Sintaxis: loader.get_template()
#Importando asi, evitas usar el loader y simplemente usas get_template
#Sintaxis: get_template()
from django.template.loader import get_template
import datetime

class Persona (object):
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #Cargo primera plantilla/template
    #Creo una variable para pasarla a la platilla/template  
    # nombre = 'Juan'  
    # apellido = 'Sosa'
    persona = Persona('Alfredo', 'Gomez')
    fecha_actual = datetime.datetime.now()
    
    #Cargo el template con loader 
    template_loader = get_template('saludo.html')
    
    #Importar de pecho el template
    #doc_externo = open('project1/templates/saludo.html')
    
    #Almaceno el contenido de la plantilla html 
    # plt = Template(doc_externo.read())
    
    #doc_externo.close()
    
    #Creo el contexto
    contexto = Context({ #Si al template lo cargue con un loader puedo precindir de la variable contexto y para en render el dic 
        'nombre_persona':persona.nombre,
        'apellido_persona':persona.apellido, 
        'edad_persona':18, 
        'fecha_actual':fecha_actual
        })
    
    #Renderizo el documento hmtl
    documento = template_loader.render({ #paso el diccionario como parametro
        'nombre_persona':persona.nombre,
        'apellido_persona':persona.apellido, 
        'edad_persona':18, 
        'fecha_actual':fecha_actual
        })
    return HttpResponse(documento) # Create your views here.

def lista(request):   
    fecha_actual = datetime.datetime.now()    
    lista_temas = ['Introduccion','Parte 1', 'Parte 2', 'Parte 3', 'Parte 4', 'Final']
   
    plt = get_template('lista.html')
    
    documento = plt.render({
        'fecha_actual':fecha_actual,
        'temas': lista_temas,
        })
    return HttpResponse(documento) # Create your views here.



def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    documento= '''
    <html>
        <body>
            <h1>
                Fecha y hora actuales: %s               
            <h1/>
        <body/>
    <html/>''' % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request,edad, agno): #El parametro agno se pasa como valor en la url
    # edadActual = 18
    periodo = agno - 2022
    edadFutura = edad + periodo
    #%s son marcadores de posicion
    documento = '''
    <html>
        <body>
            <h2>
            En el año %s tendrás %s años
            </h2>
        </body>
    </html>''' % (agno, edadFutura)
    return HttpResponse(documento)