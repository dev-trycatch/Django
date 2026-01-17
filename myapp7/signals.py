from django.db.models.signals import post_save,pre_save

from django.dispatch import receiver
from .models import *

# Trigger before saving a blog
@receiver(pre_save,sender=Blog)
def before_blog_save(sender,instance,**kwargs):
    print(f'About to save blog [Pre-save] {instance.title}')

@receiver(post_save,sender=Blog)
def after_blog_save(sender,instance,created,**kwargs):
    print(f'About to save blog [Pre-save] {instance.title}')
    if created:
        print('New Blog created [post-save] {instance.title}')
    else:
        print('Blog Updated [post-save] {instance.title}')