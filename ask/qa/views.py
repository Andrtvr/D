from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


def question_list(request):
    qs = Question.objects.all()
    qs = qs.order_by('-added_at')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'qa/list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'qa/list_rating.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)

    #answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    answers = Answer.objects.filter(question_id=pk)
    #answers = answers.get_text()
    return render(request, 'qa/detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
       # 'pk': pk,
    })


def question_ask(request):
    if request.method=='POST':
        form = AskForm(request.POST)

        if request.user.is_authenticated():
            pass
        else:

            if form.is_valid():
                post = form.save(commit=False)
                post.author = User(id=1)
                post.added_at = timezone.now()
                post.save()
                url = reverse('question_detail', args=[post.id])

                return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def question_answer(request, pk):

    if request.method == 'POST':
        '''
        form = AnswerForm(request.POST)

        if request.user.is_authenticated():
            pass
        else:

            if form.is_valid():
                post = form.save(commit=False)
                post.author = User(id=1)
                post.added_at = timezone.now()
                post.question = Question(id=pk)
                post.save()
                url = reverse('answer_st', args=[pk])


                return HttpResponseRedirect(url)
            '''
        url = reverse('answer_st', args=[pk])
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect('/', args=0)

def answer_st(request, pk):
    if request.method=='POST':
        form = AnswerForm(request.POST)

        if request.user.is_authenticated():
            pass
        else:
            if form.is_valid():
                post = form.save(commit=False)
                post.author = User(id=1)
                #q = Question.objects.filter(id=2)
                post.added_at = timezone.now()
                post.question = Question(id=pk)
                post.save()

                return HttpResponseRedirect('/answers/')
    else:
        form = AskForm()
    return render(request, 'qa/answer.html', {'form': form})

def answer_list(request):
    answ = Answer.objects.all()

    page, paginator = paginate(request, answ)
    paginator.baseurl = reverse('answers') + '?page='

    return render(request, 'qa/answers.html', {
        'answ': page.object_list,
        'page': page,
        'paginator': paginator,
    })
