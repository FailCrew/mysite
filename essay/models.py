from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from quiz.models import Question



@python_2_unicode_compatible
class Essay_Question(Question):
    AnswerID = models.CharField(verbose_name=_("AnswerID"), max_length=100, help_text="ID for answer", default = "")
    def check_if_correct(self, guess):
        answer = EssayAnswer.objects.filter(AnswerID = self.AnswerID)
        try:
            if guess == str(answer.get(answ = guess)):
                return True
            else:
                return False
        except EssayAnswer.DoesNotExist:
            return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay style question")
        verbose_name_plural = _("Essay style questions")

@python_2_unicode_compatible
class EssayAnswer(models.Model):
    question = models.ForeignKey("Essay_Question", verbose_name=_("EssayQuestion"), on_delete=models.CASCADE, )
    answ = models.CharField(verbose_name=_("CorrectAnswer"),help_text="Enter the right answer", max_length=1000, )
    AnswerID = models.CharField(verbose_name=_("AnswerID"), max_length=100, help_text="ID for answer", default = "")
    def __str__(self):
        return self.answ

    class Meta:
        verbose_name = _("EssayAnswer")
        verbose_name_plural = _("EssayAnswers")