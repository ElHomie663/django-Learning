from django import template
register = template.Library()


@register.filter(name="add+attr")
def add_attr(field, css):
    attrs = {}
    calse, valor = css.split(':')
    attrs[calse] = valor
    return field.as_widget(attrs=attrs)
