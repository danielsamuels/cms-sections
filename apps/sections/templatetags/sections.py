import jinja2

from django import template
from django.template.loader import render_to_string
from django_jinja import library

register = template.Library()


@library.global_function
@jinja2.contextfunction
def render_section(context, page_section):
    try:
        context = dict(context)
        context['section'] = page_section
    
        return render_to_string('sections/types/{}'.format(page_section.template), context)
    except TemplateDoesNotExist as e:
        import os
        from django.conf import settings

        if settings.DEBUG:
            os.system('touch {{ project_name }}/apps/sections/templates/sections/types/{}'.format(
                page_section.template,
            ))

            return ''
        else:
            raise e

            
@library.global_function
@jinja2.contextfunction
def section_contains_image(context, section_obj):
    if not section_obj.content_left or not section_obj.content_right:
        return ''

    if any('<img' in s for s in[section_obj.content_left, section_obj.content_right]):
        return 'has-media'

    return ''
