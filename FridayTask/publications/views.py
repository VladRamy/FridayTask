from django.shortcuts import render, redirect
from .models import Publications
from .forms import PublicationsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def publ_home(request):
    publications = Publications.objects.order_by('-date')
    return render(request, 'publications/publ_home.html', {'publications': publications})

class PublUpdateView(UpdateView):
    model = Publications
    template_name = 'publications/create.html'

    form_class = PublicationsForm

class PublDeleteView(DeleteView):
    model = Publications
    template_name = 'publications/publ-delete.html'
    success_url = '/publications/'

class PublDetailView(DetailView):
    model = Publications
    template_name = 'publications/details_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = PublicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = PublicationsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'publications/create.html', data)