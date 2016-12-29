from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=40, unique=True)
    name = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=40)
    permission = models.PositiveSmallIntegerField(default=1)
    url = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return '{} "{}" {}'.format(self.first_name, self.name, self.last_name)


class Group(models.Model):
    owner = models.IntegerField()
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()


class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    permission = models.PositiveSmallIntegerField()


class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    repository = models.CharField(max_length=80)
    url = models.CharField(max_length=80)


class UserProject(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    permission = models.PositiveSmallIntegerField()


class Message(models.Model):
    content = models.TextField()
    date = models.DateField()


class UserMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'Statuses'

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Priority(models.Model):
    class Meta:
        verbose_name_plural = 'Priorities'

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=50)
    time = models.PositiveIntegerField()
    description = models.TextField()
    status = models.ForeignKey(Status)
    reporter = models.ForeignKey(User)
    priority = models.ForeignKey(Priority)


class UserTask(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)


class Comment(models.Model):
    task = models.ForeignKey(Task)
    content = models.TextField()
    date = models.DateField()


class UserComment(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)


class Sprint(models.Model):
    project = models.ForeignKey(Project)
    begin = models.DateField()
    end = models.DateField()
    number = models.IntegerField()
    status = models.BooleanField()


class SprintTask(models.Model):
    sprint = models.ForeignKey(Sprint)
    task = models.ForeignKey(Task)
    time = models.IntegerField()
