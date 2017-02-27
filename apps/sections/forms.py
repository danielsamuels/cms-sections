from django import forms
from django.template.loader import render_to_string


class TypeWidget(forms.HiddenInput):

    def render(self, name, value, attrs=None):
        return render_to_string('admin/pages/page/type_widget.html', {
            'name': name,
            'value': value,
            'attrs': attrs,
            'super': super(TypeWidget, self).render(name, value, attrs=None)
        })
