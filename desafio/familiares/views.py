from django.shortcuts import render
from familiares.models import Familiar

# Create your views here.
def crear_familiar(request):
    new_familiar = Familiar.objects.create(name = "Jorge", age="63", birthday="22/10/1959")
    # new_familiar = Familiar.objects.create(name = "Gabriela", age="52", birthday="27/02/1970")
    # new_familiar = Familiar.objects.create(name = "Vito", age="7", birthday="26/02/2015")
    context={
        'new_familiar':new_familiar
    }
    return render(request, 'index.html', context=context)

def list_familiares(request):
    familiares = Familiar.objects.all()
    context = {
        'familiares':familiares
    }
    return render(request, 'index.html', context=context )


# padre = Familiar("Jorge", 63, "22/10/1959")
# madre = Familiar("Gabriela", 52, "27/02/1970")
# perro = Familiar("Vito", 7, "26/02/2015")