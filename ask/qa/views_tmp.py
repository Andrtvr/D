from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, Answer, QuestionManager
from django.core.paginator import Paginator, EmptyPage

def qa(request, *args, **kwargs):
    return HttpResponse('qa')
'''
def new_quest(request):
    #quest = Question.objects.all()
    quest = QuestionManager()
    #q_new = quest.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(quest.new(), limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/list.html', {
        'quest': page.object_list,
        'paginator': paginator, 'page': page,
    })1
'''
def new_quest(request):
    try:
        limit = request.GET.get('limit', 10)
    except ValueError:
        limit = 10
    if limit > 100:
        limit=10
    try:
      page = request.GET.get('page', 1)
    except ValueError:
        raise Http404

    quest = QuestionManager()
    paginator = Paginator(quest.new(), limit)
    if quest.new() ==[]:
        raise Http404
    else:

        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
            return page, paginator


        return render(request, 'qa/list.html', {
            'quest': page.object_list,
            'paginator': paginator, 'page': page,
        })

def popular(request):
    quest = QuestionManager()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(quest.popular(), limit)
    paginator.baseurl = 'popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/list_rating.html', {
        'quest': page.object_list,
        'paginator': paginator, 'page': page,
    })

def question(request, slug):
    q = QuestionManager()
    a = Answer()
    quest = q.quest(slug=slug)
    if quest == None:
        raise Http404

    else:
        return render(request, 'qa/detail.html', {
        'quest': quest,
   #     'answer': a.id(),
    })

'''

def qa(request, *args, **kwargs):
    return HttpResponse('qa')

def new_quest(request, *args, **kwargs):
    return HttpResponse('new')

def popular(request, *args, **kwargs):
    return HttpResponse('pop')

def question(request, id):
    return HttpResponse('qa %s' %id )
'''
