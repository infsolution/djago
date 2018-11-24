# -*- coding: utf-8 -*-
from django.forms import ModelForm 
from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
	#question_text = forms.CharField(label="Question", max_length=256)
	class Meta:
		model = Question
		fields = ['question_text']
		widgets = {
			'Quest':forms.TextInput(attrs={'class':'form-control', 'max_length':256}),
		}

	def save(self, commit=True):
		quest = super(QuestionForm, self).save()
		return quest

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ['choice_text', 'votes']
		widgets ={
			'Escolha': forms.TextInput(attrs={'class':'form-control', 'max_length':256}),
			'Voto':forms.TextInput(attrs={'class':'form-control','max_length':256}),
		}

		def save(self, commit=True):
			choice = super(ChoiceForm, self).save()
			return choice
	
