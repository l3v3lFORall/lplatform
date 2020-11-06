from django import template

register = template.Library()

@register.simple_tag
def test(v1,v2,v3,v4):
    return v1*v2*v3*v4