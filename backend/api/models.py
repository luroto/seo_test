from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return (("[{}] ({})").format(self.id, self.name))

class UserTask(models.Model):
    description = models.CharField(max_length=200, unique=True)
    STATES = [
            ('to_do', 'to do'),
            ('done', 'done'),
            ]
    state = models.CharField(max_length=8, choices=STATES, default='select task state')
    user_id = models.ForeignKey('User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return(("'task_id': {}, 'task_description': {}, 'task_state': {}").format(self.id, self.description, self.state))
# Create your models here.
