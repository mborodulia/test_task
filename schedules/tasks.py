# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=(crontab(minute="*/1")))
def clear_votes():
    from api.models import Post

    for post in Post.objects.all():
        print(post)
        post.amount_of_upvotes = 0
        post.save()
