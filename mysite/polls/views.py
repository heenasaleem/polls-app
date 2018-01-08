from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import Question,Choice
from django.template import loader
from django.http import HttpResponseRedirect
# from django.urls import reverse

# from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
from django.core.urlresolvers import reverse

# Create your views here.
'''
def index(request):
	return HttpResponse('hello ,you are at the polls index.') '''

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question' : question})
	
		####by importing Http404######
'''		
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question doesnt exist")'''
		
	
	#return HttpResponse("you're looking at the question %s." % question_id)
	

def results(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question' : question})
	

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
	    selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })    
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
		# return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
'''
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ','.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context) #shortcut code
   # return HttpResponse(template.render(context, request))

