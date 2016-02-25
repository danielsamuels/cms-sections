from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def section(context, page_section):
    context.update({'section': page_section})

    return render_to_string('sections/types/{}'.format(
        page_section.template
    ), context)


@register.simple_tag(takes_context=True)
def section_contains_image(context, section_obj):
    if not section_obj.content_left or not section_obj.content_right:
        return ''

    if any('<img' in s for s in[section_obj.content_left, section_obj.content_right]):
        return 'has-media'

    return ''
