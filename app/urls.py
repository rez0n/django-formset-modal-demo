from django.urls import path

from demo.views import IndexView, ModalFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('modal_form_view', ModalFormView.as_view(), name='modal_form'),
]
