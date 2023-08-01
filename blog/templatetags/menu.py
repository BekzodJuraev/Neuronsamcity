from django import template
from blog.models import Category


register=template.Library()
@register.inclusion_tag('menu.html')
def show_menu(menu_class='nav navbar-nav menu_nav ml-auto'):
    categories=Category.objects.all()
    return {"categories":categories, "menu_class":menu_class}


@register.inclusion_tag('footer.html')
def show_footer(menu_footer='nav navbar-nav menu_nav ml-auto'):
    categories=Category.objects.all()
    return {"categories":categories, "menu_footer":menu_footer}
