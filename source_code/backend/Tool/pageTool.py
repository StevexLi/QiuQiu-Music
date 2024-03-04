from django.core.paginator import Paginator


def page_result(res_list, page_num, entry_num=5):
    paginator = Paginator(res_list, entry_num)
    if page_num > paginator.num_pages:
        page_num = 1
    c_page = paginator.page(page_num)
    result = []
    for _ in c_page.object_list:
        result.append(_.detail_info())
    return result, paginator.num_pages
