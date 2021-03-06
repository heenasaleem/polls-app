from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	"""docstring for ChoiceInline"""
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	#fields = [ 'question_text', 'pub_date']
	fieldsets = [
		('Question',              {'fields': ['question_text']}),
		('Date Information',{'fields':['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)