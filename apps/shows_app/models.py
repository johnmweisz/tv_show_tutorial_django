from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):

    def validate(self, form, ftype=0):
        errors = {}
        if len(form['title']) < 3:
            errors['title'] = "Please enter at least 3 characters."
        if Shows.objects.filter(title=form['title']) and ftype == 0:
            errors['title'] = "Please enter a new title."            
        if len(form['network']) < 3:
            errors['network'] = "Please enter at least 3 characters."
        if len(form['release']) < 3:
            errors['release'] = "Please enter at least 3 characters."
        if datetime.today() < datetime.strptime(form['release'], '%Y-%m-%d'):
            errors['release'] = "Please enter a past date."
        if len(form['description']) < 20 and len(form['description']) > 0:
            errors['description'] = "Please enter at least 20 characters."
        return errors

    def add(self, form):
        return self.create(title = form['title'], network = form['network'], release = form['release'], description = form['description']).id

    def display(self, id):
        return self.get(id=id)
    
    def update(self, id, form):
        update = self.get(id=id)
        update.title = form['title']
        update.network = form['network']
        update.release = form['release']
        update.description = form['description']
        update.save()
        return update.id

    def destroy(self, id):
        return self.get(id=id).delete()

class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=60)
    release = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()