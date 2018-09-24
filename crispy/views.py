# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from crispy.forms import PersonForm
from crispy.models import Person


class PersonCreateView(CreateView):
	model = Person
	fields = ('name', 'email', 'job_title', 'bio')


class PersonUpdateView(UpdateView):
	model = Person
	form_class = PersonForm
	template_name = 'crispy/person_update_form.html'


class PersonListView(ListView):
	model = Person
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['date'] = timezone.now()
		return context


class PersonDeleteView(DeleteView):
	model = Person
	success_url = reverse_lazy('crispy:list')
