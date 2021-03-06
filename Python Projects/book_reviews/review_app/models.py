from datetime import datetime
import re
from django.db import models
import bcrypt
from dateutil.relativedelta import relativedelta

class Manager(models.Manager):
  def validator(self, postData):
    errors = {}
    result = re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', postData.get('birthday'))
    if not result:
      errors['birthday'] = 'Birthday input does not match pattern'
    if len(postData['first_name']) < 2:
      errors['first_name'] = 'First name should be at least 2 characters'
    if len(postData['last_name']) < 2:
      errors['last_name'] = 'Last name should be at least 2 characters'
    if postData['password'] != postData['password_confirm']:
      errors['pw'] = 'Passwords must match.'
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['email']):           
      errors['email'] = 'Invalid email address'
    try:
      birthday = postData['birthday']
      today = datetime.now()
      datetime_birthday = datetime.strptime(birthday, '%Y-%m-%d')
      time_difference = relativedelta(today, datetime_birthday)
      difference_in_years = time_difference.years
      if difference_in_years < 13:
        errors['birthday'] = 'You must be at least 13 to register.'
    except:
      print('Error- birthday likely not formatted correctly')
    return errors



class User(models.Model):
  first_name = models.CharField(max_length=255, blank=False)
  last_name = models.CharField(max_length=255, blank=False)
  password = models.CharField(max_length=255, blank=False)
  email = models.EmailField(unique=True)
  birthday = models.DateField()
  username = models.CharField(max_length=255, blank=False, default='test')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = Manager()

class Book(models.Model):
  title = models.CharField(max_length=255, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return f"<book object: {self.title} ({self.id})>"

class Author(models.Model):
  name = models.CharField(max_length=255)
  book = models.ManyToManyField(Book, related_name='authors')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
  msg_content = models.TextField(blank=False)
  user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
  book = models.ForeignKey(Book, related_name = 'reviews', on_delete=models.CASCADE)
  author = models.ForeignKey(Author, related_name = 'reviews', on_delete=models.CASCADE)
  rating = models.IntegerField(blank=False) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)









