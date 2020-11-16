from django.db import models

# Create your models here.
# models = tables


class Question(models.Model):
    # Django automatically creates an id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ForeignKey serves as a link between the primary key(question_text) and the choice
    # basically creating a relation between the two tables
    # We use "on_delete=models.CASCADE" to dispose of all the choices of a question that's been deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
