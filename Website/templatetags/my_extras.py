from django import template

register = template.Library() # Call the library 


@register.filter(name='cut') # register a filter 
def cut(value, arg):
    return value.replace(arg, '')

register.filter('cut', cut) # Another way to register a filter 