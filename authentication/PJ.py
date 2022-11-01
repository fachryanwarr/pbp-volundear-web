from django.views.generic import CreateView
from authentication.models import VolundearUser
from authentication.forms import PJSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect

class PJSignUpView(CreateView):
    model = VolundearUser
    form_class = PJSignUpForm
    template_name = 'register_PJ.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Relawan'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('authentication:login')