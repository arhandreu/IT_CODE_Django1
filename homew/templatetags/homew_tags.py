from django import template
from homew.models import NavBar

register = template.Library()


@register.inclusion_tag('homew/navbar.html', name='navbar')
def show_navbar():
    navbar = NavBar.objects.all()
    return {'navbar': navbar, }
