from django.views.generic import CreateView
from authentication.models import VolundearUser
from authentication.forms import RelawanSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect

class RelawanSignUpView(CreateView):
    model = VolundearUser
    form_class = RelawanSignUpForm
    template_name = 'register_relawan.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'PJ'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('authentication:login')