from django.shortcuts import render, redirect
from pools.models import *
from .forms import QuestionForm, ChoiceForm

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    return render(request,'pools/index.html',{'questions':Question.objects.filter(closed=False).order_by('-pub_date')})

def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/question.html', {'question':question})

def exibir_fechada(request):
    questions = ''
    #try:
    questions = Question.objects.filter(closed=True)
    #except Exception as e:
    #    print(e)
    #    return render(request, 'pools/question.html', {'questions':questions})       
    return render(request, 'pools/question.html', {'questions':questions})
    

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/results.html',{'question':question})

def vote(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += choice.votes
    choice.save()
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/question.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice = Choice.objects.get(id=request.POST['choice'])
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))

def apagar(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return render(request,'pools/index.html',{'questions': Question.objects.filter(closed=False).order_by('-pub_date')})

def status(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.closed == True:
        question.closed = False
        question.save()
    else:
        question.closed = True
        question.save()
    return render(request,'pools/index.html',{'questions': Question.objects.filter(closed=False).order_by('-pub_date')})


'''def cadastrar(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionForm()
    return render(request, 'pools/new_quest.html', {'form':form})'''

def cadastrar(request):
    valor = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            quest = Question(question_text=form.cleaned_data['question_text'])
            quest.save()
            valor = form.cleaned_data['question_text']
            form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'pools/new_quest.html', {'form':form, 'valor':valor})

def responder(request, question_id):
    quest = Question.objects.get(id=question_id)
    valor = ''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            quest.choices.create(choice_text=form.cleaned_data['choice_text'], 
                votes=form.cleaned_data['votes'])
            valor = form.cleaned_data['choice_text']
            form = ChoiceForm()    
    else:
        form = ChoiceForm()
    return render(request, 'pools/new_choice.html', {'form':form, 'question':quest, 'valor':valor})