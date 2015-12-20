from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT_LEN = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateTimeField(blank=True, null=True)





    def __unicode__(self):
        return self.title


    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text [:SHORT_TEXT_LEN]
        else:
            return self.text

class Comments(models.Model):
    class Meta():
        db_table= 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)




