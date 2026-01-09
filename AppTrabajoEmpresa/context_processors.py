from .models import DatosEmpresa

def info_empresa(request):
    # Intentamos obtener el primer registro. Si no existe, devolvemos None.
    datos = DatosEmpresa.objects.first()
    
    # Esto crea una variable global 'empresa' que podrás usar en CUALQUIER template
    return {'empresa': datos}