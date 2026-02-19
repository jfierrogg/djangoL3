from django.shortcuts import render
from .forms import ContactoForm

def home(request):
    return render(request, 'index.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save() # Guarda en la BD
            return render(request, 'success.html')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})