import random

from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import View

from .models import Choice, Question, QuizSessions, Hero
        
def index(request):
    return render(request, 'polls/index.html')

class DetailView(View):
      
    template_name = 'polls/detail.html'

    def get(self, request, pk=None):
        try:
            session = QuizSessions.objects.get(pk=pk)
        except QuizSessions.DoesNotExist:
            raise Http404("Session does not exist")
        else:
            question = session.questions.order_by('id').all()[session.current_question]
            hero = Hero.objects.get(name=question.question_name)
            answers = [i for i in question.choice_set.all()]
            random.shuffle(answers)
            return render(request, self.template_name, {'question': question, 'session': session, 'hero': hero, 'answers': answers})

    def post(self, request, pk):
        selected_choice = request.POST['choice']
        try:
            session = QuizSessions.objects.get(pk=pk)
        except QuizSessions.DoesNotExist:
            raise Http404("Session does not exist")
        else:
            answers = session.answers
            answers[session.questions.order_by('id').all()[session.current_question].pk] = selected_choice
            session.answers = answers
            session.current_question += 1
            session.save()
            if session.current_question >= len(session.questions.all()):
                return redirect(reverse('polls:results', args=(session.id,)))
            return redirect(reverse('polls:detail', args=(session.id,)))


def create_session(request):
    session = QuizSessions.objects.create(answers={})
    questions = list(Question.objects.all())
    random.shuffle(questions)
    session_questions = questions[:12]
    session.questions.set(session_questions)
    return redirect(reverse('polls:detail', args=(session.id,)))


def results(request, pk):
    session = QuizSessions.objects.get(pk=pk)
    questions = session.questions.all()
    correct_answers = []
    incorrect_answers = []
    for i in questions:
        answer = session.answers[str(i.pk)]
        hero = Hero.objects.get(name=i.question_name)
        if i.question_name == answer:
            correct_answers.append((i, answer, hero))
        else:
            incorrect_answers.append((i, answer, hero))
    return render(request, 'polls/results.html', {'session': session, 'correct_answers': correct_answers, 'incorrect_answers': incorrect_answers})








