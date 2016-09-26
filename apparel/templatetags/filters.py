from django import template

register = template.Library()

@register.filter()
def add_ringgit_sign(value):
    # Add Malaysian Ringgit Sign to the value
    new_value = str(value).split()
    new_value.insert(0, 'RM')
    return ''.join(new_value)

