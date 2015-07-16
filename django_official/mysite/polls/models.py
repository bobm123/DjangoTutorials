from django.db import models


# creating an instance of these classes (since they are based on models.Model)
# generates a new entry in the database. There are several class methods that
# do things like get all such entries and saving changes.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):              # __str__ on Python 3
           return self.question_text

    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

 
class Choice(models.Model):
    question = models.ForeignKey(Question)          # this associates each choice (possible answer) with a question.
    choice_text = models.CharField(max_length=200)  # The actual text.
    votes = models.IntegerField(default=0)          # And since this is a poll, how many times it was selected
    
    def __unicode__(self):              # __str__ on Python 3
        return self.choice_text