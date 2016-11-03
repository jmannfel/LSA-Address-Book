from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse

from contacts.models import Contact

class LoggedInMixin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ContactListView(LoggedInMixin, ListView):
	model = Contact
	template_name = "contact_list.html"

class ContactView(LoggedInMixin, DetailView):
	model = Contact
	template_name = 'contact.html'


class CreateContactView(LoggedInMixin, CreateView):
	model = Contact
	fields = ['first_name', 'last_name', 'phone', 'email', 'address']
	template_name = "edit_contact.html"

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self, **kwargs):

		context = super(CreateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-new')

		return context

class UpdateContactView(LoggedInMixin, UpdateView):
	model = Contact
	fields = ['first_name', 'last_name', 'phone', 'email', 'address']
	template_name = "edit_contact.html"

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self, **kwargs):

		context = super(UpdateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-edit',
			kwargs={'pk': self.get_object().id})

		return context

class DeleteContactView(LoggedInMixin, DeleteView):
	model = Contact
	fields = ['first_name', 'last_name', 'phone', 'email', 'address']
	template_name = 'delete_contact.html'

	def get_success_url(self):
		return reverse('contacts-list')

