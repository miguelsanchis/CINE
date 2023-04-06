import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def saludo(request, age):
    """Ejemplo de uso normal de una funcion pasandole paramentros como edad o la fecha"""
    date = datetime.datetime.now()
    saludo = f"""<!DOCTYPE html>
                <html>
                <head>
                    <title>Mi primera página HTML  </title>
                </head>
                <body>
                    <h1>Bienvenidos a mi página web</h1>
                    <p>Esta es una prueba de HTML. Esta es la fecha actual {date} y esta es la edad que he puesto en la url:{age} </p>
                </body>
                </html>"""

    return HttpResponse(saludo)

def uso_plantilla(request):
    """Esta funcion es una prueba de uso de una plantilla externa"""
    
    with open("/Users/miguel/repos/CINE/cine_project/cine_project/templates/saludo.html") as doc_externo:
        plt = Template(doc_externo.read())
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def saludo_con_diccionarios(request):
    """Esta funcion usa diccionarios"""
    nombre = "Miguel"
    with open("/Users/miguel/repos/CINE/cine_project/cine_project/templates/saludo_dicc.html") as doc_externo:
        plt = Template(doc_externo.read())
    ctx = Context({"mi_nombre":nombre,"mi_apellido":"Sanchis","familia":["Adri","Mare","Pare"]})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def uso_plantilla_cargadores(request):
    """Esta plantilla usa cargadores, una forma mas eficiente de uiliazr plantillas. En settings 'templates' hemos definido la ruta de
    donde hemos guardado todas nuestras plantillas e importado la clase loader"""

    nombre = "miguel"
    doc_externo=get_template("saludo_dicc.html")
    documento = doc_externo.render({"mi_nombre":nombre,"mi_apellido":"Sanchis","familia":["Adri","Mare","Pare"]})
    return HttpResponse(documento)

def uso_shortcuts(request):

    nombre = "miguel"
    ctx= {"mi_nombre":nombre,"mi_apellido":"Sanchis","familia":["Adri","Mare","Pare"]}

    return render(HttpRequest=request,template_name="saludo_dicc",context=ctx)