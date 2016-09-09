from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Edition(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Adventure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    title = models.TextField()
    edition = models.ForeignKey(Edition)
    authors = models.ManyToManyField(Author)
    edition = models.ForeignKey(Publisher)
    published = models.DateField()
    min_level = models.IntegerField(help_text=('The minumum character level '
                                               'for the adventure'))
    max_level = models.IntegerField(help_text=('The maximum character level '
                                               'for the adventure'))
    min_characters = models.IntegerField(help_text=('The minumum number of '
                                                    'charactersfor the '
                                                    'adventure'))
    max_characters = models.IntegerField(help_text=('The maximum number of '
                                                    'charactersfor the '
                                                    'adventure'))
