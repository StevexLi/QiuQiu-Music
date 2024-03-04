from django.core.paginator import Paginator
from django.db.models import Q

from Tool.checkDecorator import *
from Tool.pageTool import page_result
from random import randint


# Create your views here.
@method_checker('GET')
def search_song_by_name(request):
    """
    search the song by name or singer.
    must use "page_num" and "keywords".
    please warn that use the title OR the singer to do the search,
    or it may return no result.

    :param request: must use "keywords" and "page_num"
    :return: search result in the page
    """
    data = request.GET
    keywords = data.get('keywords').split(' ')
    if len(keywords) == 0:
        return JsonResponse({
            'code': '1002',
            'msg': '搜索关键词未传入'
        })
    cond_title = Q()
    cond_title.connector = Q.AND
    for key in keywords:
        cond_title.children.append(('title__icontains', key))
    cond_singer = Q()
    cond_singer.connector = Q.AND
    for key in keywords:
        cond_singer.children.append(('singer__icontains', key))
    res = Song.objects.filter((cond_title | cond_singer))
    paginator = Paginator(res, 50)
    page_num = data.get('page_num', 1)
    try:
        page_num_int = int(page_num)
        if page_num_int > paginator.num_pages:
            page_num_int = 1
        c_page = paginator.page(page_num_int)
        resp = []
        for _ in c_page.object_list:
            info = _.detail_info()
            resp.append(info)
        return JsonResponse({
            'code': '0',
            'msg': '搜索成功',
            'data': resp,
            'total_page': paginator.num_pages,
            'current_entry_num': len(resp),
        })
    except Exception as e:
        return JsonResponse({
            'code': '1003',
            'msg': '查询失败，失败原因：' + str(e)
        })


@method_checker('GET')
def search_list_by_name(request):
    data = request.GET
    keywords = data.get('keywords').split(' ')
    if len(keywords) == 0:
        return JsonResponse({
            'code': '1002',
            'msg': '搜索关键词未传入'
        })
    cond = Q()
    cond.connector = Q.AND
    for key in keywords:
        cond.children.append(('title__icontains', key))
    res = SongList.objects.filter((cond & Q(sharable=True)))
    paginator = Paginator(res, 50)
    page_num = data.get('page_num', 1)
    try:
        page_num_int = int(page_num)
        if page_num_int > paginator.num_pages:
            page_num_int = 1
        c_page = paginator.page(page_num_int)
        resp = []
        for _ in c_page.object_list:
            info = _.detail_info()
            resp.append(info)
        return JsonResponse({
            'code': '0',
            'msg': '搜索成功',
            'data': resp,
            'total_page': paginator.num_pages,
            'current_entry_num': len(resp),
        })
    except Exception as e:
        return JsonResponse({
            'code': '1003',
            'msg': '查询失败，失败原因：' + str(e)
        })


@method_checker('GET')
@null_checker(['tag'])
@page_num_checker
def search_song_by_tag(request):
    tag = request.GET.get('tag')
    page_num = request.GET.get('page_num', '1')
    cond = Q()
    cond.connector = Q.OR
    for _ in ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6']:
        cond.children.append((_ + '__icontains', tag))
    res = Song.objects.filter(cond)
    [resp, total_page] = page_result(res, int(page_num), 50)
    return JsonResponse({
        'code': '0',
        'msg': '搜索成功',
        'data': resp,
        'total_page': total_page,
        'current_entry_num': len(resp),
    })


@method_checker('GET')
@null_checker(['tag'])
@page_num_checker
def search_list_by_tag(request):
    tag = request.GET.get('tag')
    page_num = request.GET.get('page_num', '1')
    cond = Q()
    cond.connector = Q.OR
    for _ in ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6']:
        cond.children.append((_ + '__icontains', tag))
    res = SongList.objects.filter((cond & Q(sharable=True)))
    [resp, total_page] = page_result(res, int(page_num), 50)
    return JsonResponse({
        'code': '0',
        'msg': '搜索成功',
        'data': resp,
        'total_page': total_page,
        'current_entry_num': len(resp),
    })


@method_checker('GET')
@null_checker(['num', 'type'])
def random_recommend(request):
    num = request.GET.get('num')
    c_type = eval(request.GET.get('type'))
    if not num.isdigit():
        return JsonResponse({
            'code': '1003',
            'msg': '传入参数不是整数'
        })
    num = int(num)
    if c_type:
        max_id = Song.objects.last().song_id
        resp = []
        try_count = 0
        while len(resp) < num and try_count < 10000:
            try:
                choose_id = randint(1, max_id)
                obj = Song.objects.get(song_id=choose_id)
                if not resp.__contains__(obj):
                    resp.append(obj.detail_info())
            except Song.DoesNotExist:
                pass
            finally:
                try_count += 1
    else:
        max_id = SongList.objects.last().list_id
        resp = []
        try_count = 0
        while len(resp) < num and try_count < 10000:
            try:
                choose_id = randint(1, max_id)
                obj = SongList.objects.get(list_id=choose_id)
                if not resp.__contains__(obj):
                    resp.append(obj.detail_info())
            except SongList.DoesNotExist:
                pass
            finally:
                try_count += 1
    return JsonResponse({
        'code': '0',
        'msg': '查找成功',
        'data': resp,
    })


