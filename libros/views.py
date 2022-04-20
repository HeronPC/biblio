from django.shortcuts import render
from .models import Libro

# Create your views here.

def index(request):
    # Página home de la aplicación
    num_libros = Libro.objects.all().count()
    context = {
        'num_libros': num_libros
    }
    return render(request, 'index.html', context)


def libro_list(request):
    # Página listado de libros
    libro_list = Libro.objects.all()
    context = {
        'libro_list': libro_list
    }
    return render(request, 'libros/libro_list.html', context)


def libro_detail(request, id):
    # Método para operación CRUD Recuperar libro
    # Recuperamos el libro y lo mostramos
    libro = Libro.objects.get(id=id)
    context = {'libro': libro}
    return render(request, 'libros/libro_detail.html', context)


def libro_create(request):
    # Método para operación CRUD Crear nuevo libro
    if request.method == 'POST' and request.POST.get('libro_id'):
        # En caso de que exista un id quiere decir que hay que actualizar no crear
        return libro_update(request, int(request.POST.get('libro_id')))
    elif request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        libro = Libro.objects.create(
            titulo=request.POST.get('titulo'),
            sinopsis=request.POST.get('sinopsis'),
            isbn=request.POST.get('isbn'),
            pags=request.POST.get('pags'),
            año=request.POST.get('año')
        )
        context = {'libro': libro}
        return render(request, 'libros/libro_detail.html', context)

    else:
        return render(request, 'libros/libro_form.html')


def libro_update(request, id):
    # Método para operación CRUD Actualizar libro
    if request.method == 'GET' and id:
        # Recuperamos el libro y lo cargamos en el formulario para poder editarlo
        libro = Libro.objects.get(id=id)
        context = {'libro': libro}
        return render(request, 'libros/libro_form.html', context)
    elif request.method == 'POST' and id:
        # Se ha pulsado guardar y se quiere editar el libro, la diferencia con crear es que aquí ya tenemos un id
        libro = Libro()
        libro.id = id
        libro.titulo = request.POST.get('titulo')
        libro.sinopsis = request.POST.get('sinopsis')
        libro.isbn = request.POST.get('isbn')
        libro.pags = request.POST.get('pags')
        libro.año = request.POST.get('año')
        libro.save()
        # Redirigimos al detalle del libro para que se visualicen los cambios guardados
        context = {'libro': libro}
        return render(request, 'libros/libro_detail.html', context)

    # si no se cumplen las condiciones volvemos a la página principal
    return index(request)


def libro_delete(request, id):
    # Método para operación CRUD borrar libro
    if request.method == 'GET':
        # Cuando la peticion es GET mostramos la confirmación de si quiere borrar
        libro = Libro.objects.get(id=id)
        context = {'libro': libro}
        return render(request, 'libros/libro_delete.html', context)
    elif request.method == 'POST':
        # Cuando la petición es POST quiere decir que ha pulsado que SÍ quiere borrar
        libro = Libro.objects.get(id=id)
        libro.delete()

    # volvemos a la página principal
    return index(request)
