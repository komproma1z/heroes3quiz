from django.db import models
from django.contrib.postgres.fields import JSONField


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=400, blank=True)
    hero_class = models.CharField(max_length=20, blank=True)
    specialty = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=20, blank=True)
    base_charateristics = JSONField(default=dict((
        ('attack', 0),
        ('defense', 0),
        ('spell_power', 0),
        ('knowledge', 0),
    )), blank=True)
    base_spells = models.CharField(max_length=20, blank=True)
    has_spellbook = models.BooleanField(default=False)
    portrait = models.FileField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class QuizSessions(models.Model):
    questions = models.ManyToManyField(Question, verbose_name=("Questions"))
    answers = JSONField()
    current_question = models.IntegerField(default=0)


