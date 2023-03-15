from django import forms
from django.utils.safestring import mark_safe

from catsite import settings


class PictureWidget(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)
        value = f'{settings.MEDIA_URL}{value}' if isinstance(value, str) else value.url
        img_html = mark_safe(f"<br/><img height='200px' style='margin-top: 10px' id='preview-{name}' src='{value}' />")
        return f'{input_html}{img_html}'
