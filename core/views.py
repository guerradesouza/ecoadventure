from django.views.generic import TemplateView
from .forms import InscricaoForm
from .models import Servico, Funcionario
from django.shortcuts import render

def IndexView(request):
        if request.method == "GET":
                form = InscricaoForm()
                context = {
                        'servicos':Servico.objects.all(),
                        'funcionarios':Funcionario.objects.all(),
                        'form':form,  
                }
                
                return render(request, 'index.html', context)
        else:
                form = InscricaoForm(request.POST)
                if form.is_valid():
                        inscricao = form.save()
                        form = InscricaoForm()
                
                context = {
                        'form': form
                }
                return render(request, "index.html", context)
            
    
    

