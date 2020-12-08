# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.assignment_tag
def grouped_ingredients(items):
    grp = []

    def by2(lst, name=None, k=3):
        res = []
        for i in xrange(0, len(lst), k):

            if name:
                res.append((name, lst[i:i+k]))
            else:
                res.append(lst[i:i+k])
        return res

    for group, ing_list in items:

        if not group:
            grp += by2(ing_list, u'Без категории', (ing_list.count() / 2) + 1)
        else:
            grp.append((group, ing_list))

    return by2(grp,k=2)