from bootstrap_modal_forms.forms import BSModalForm
from django.forms import widgets, fields
from formset.renderers.bootstrap import FormRenderer
from formset.utils import FormMixin
from formset.widgets import DatePicker, DualSelector


class ModalForm(FormMixin, BSModalForm):
    default_renderer = FormRenderer()

    TRANSPORTATION_CHOICES = [
        ("Private Transport", [('foot', "Foot"), ('bike', "Bike"), ('mc', "Motorcycle"), ('car', "Car")]),
        ("Public Transport",
         [('taxi', "Taxi"), ('bus', "Bus"), ('train', "Train"), ('ship', "Ship"), ('air', "Airplane")]),
    ]

    title = fields.CharField(
        label="Title (works)",
        widget=widgets.TextInput(attrs={
            'class': 'form-control',
        }),
    )

    transportation_multiple = fields.MultipleChoiceField(
        label="Transportation Multiple (works)",
        choices=TRANSPORTATION_CHOICES,
        help_text="Available means of tranportation.",
    )

    publish_date = fields.DateField(
        label="Calendar (NOT works)",
        widget=DatePicker,
    )

    transportation_dual = fields.MultipleChoiceField(
        label="Transportation Dual (NOT works)",
        choices=TRANSPORTATION_CHOICES,
        widget=DualSelector(),
    )

