from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import PageForm
from workforce.models import Clown
from django.http import HttpResponseRedirect

# Create your views here.
def get_name(request):
    if request.method == 'POST':

        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


class ResumeListView(ListView):
    """ Renders a list of all Resumes. """
    model = Clown

    def get(self, request):
        """ GET a list of Resumes. """
        clowns = self.get_queryset().all()
        return render(request, 'index.html', {
          'clowns': clowns
        })

class ResumeDetailView(DetailView):
    """ Renders a specific resume based on it's slug."""
    model = Clown

    def get(self, request, slug):
        """ Returns a specific resume by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class ResumeCreateView(CreateView):
    model = Clown

    def get(self, request):
        form = PageForm()
        context = {'form': form,}
        return render(request, "new-resume.html", context)

    def post(self, request):
        if request.method == "POST":
            form = PageForm(request.POST)
            if form.is_valid():
                resume = form.save()

                txt_message = resume.name+" has been successfully created"

                return render(request, 'page.html', {'page': resume})
            else:

                errors = "Resume was not created" 
                error_page('page-error', errors)
        else:
            form = PageForm()

        context = {'form': form}

        return render(request, 'clown/page.html', context)