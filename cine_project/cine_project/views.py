import datetime
from django.http import HttpResponse
from django.template import Template, Context


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
