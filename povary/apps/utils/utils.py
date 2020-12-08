from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q


def get_complex_paginator(object_list, page, part, objects_per_page, pages_per_part):

    object_paginator = Paginator(object_list, objects_per_page)
    part_paginator = Paginator(object_paginator.page_range, pages_per_part)

    lists = []
    for paginator, i in zip((object_paginator, part_paginator), (page, part)):
        try:
            lst = paginator.page(i)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            lst = paginator.page(paginator.num_pages)

        lists.append(lst)

    prev_base_page = part_paginator.page(int(part) - 1) \
        if int(part) != 1 else None

    if prev_base_page and prev_base_page.object_list:
        prev_base_page = prev_base_page.object_list[0]

    next_base_page = part_paginator.page(int(part) + 1) \
        if int(part) != part_paginator.num_pages else None

    if next_base_page and next_base_page.object_list:
        next_base_page = next_base_page.object_list[0]

    return lists[0], lists[1], prev_base_page, next_base_page


def search(q, field, queryset):
    query = q.split()
    compiled = \
        reduce(Q.__or__, [Q(**{'%s__icontains' % field: word}) for word in query])
    return queryset.filter(compiled)