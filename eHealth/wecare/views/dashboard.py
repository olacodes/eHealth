from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


# @login_required
class Dashboard(TemplateView):  
    template_name = 'dashboard.html'