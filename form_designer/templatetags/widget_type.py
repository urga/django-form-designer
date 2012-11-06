from django import template
register = template.Library()


@register.filter
def field_type(field):
    """
    Show actual field type of a BoundField
    """
    return field.field.__class__.__name__


@register.filter
def widget_type(field):
    """
    Show widget type of the BoundField
    """
    return field.field.widget.__class__.__name__
