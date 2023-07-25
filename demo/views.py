from bootstrap_modal_forms.generic import BSModalFormView
from django.views.generic import TemplateView

from demo.forms import ModalForm
from formset.calendar import CalendarResponseMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class ModalFormView(CalendarResponseMixin, BSModalFormView):
    template_name = 'modal.html'
    form_class = ModalForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
