from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
     
def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.TextField()
    QuestionID=models.IntegerField()
     
def __str__(self):
        return self.answer      