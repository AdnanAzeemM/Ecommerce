from django import template
from product.models import ProductReview

register = template.Library()


@register.filter(name='upper')
def upper(value):
    return value.upper()


@register.filter(name='the_list')
def the_list(rating):
    stars = []
    for i in range(rating):
        stars.append(rating)

    return stars


x = the_list
print(x)


@register.filter(name='list_Inactive')
def list_Inactive(value):
    stars = []
    tot_val = 5
    total = tot_val - value
    for i in range(total):
        stars.append(total)

    return stars


x = the_list
print(x)


# @register.filter(name='total_item')
# def total_item(value):
#     stars = []
#     for i in range(value):
#         stars.append(value)
#
#     return stars
#
#
# x = the_list
# print(x)
