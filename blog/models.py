from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=255,verbose_name='title')
    slug=models.SlugField(max_length=255, verbose_name='Url', unique=True)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
        ordering=['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    teacher = models.CharField(max_length=100,verbose_name='Преподаватель',default='')
    fee= models.CharField(max_length=100, verbose_name='Стоимость курса',default='')
    seat = models.CharField(max_length=100, verbose_name='Количество мест',default='')
    duration = models.CharField(max_length=100,verbose_name='Длительность урока',default='')
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Обпубликовано')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    views=models.IntegerField(default=0, verbose_name='Кл просмторов')
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts',default='')
    #tags = models.ManyToManyField(Tag,blank=True,related_name='posts')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post',kwargs={"slug":self.slug})


    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering=['created_at']



class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    #author = models.CharField(max_length=100,default='author')
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Обпубликовано')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    views=models.IntegerField(default=0, verbose_name='Кл просмторов')
    #category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts')
    #tags = models.ManyToManyField(Tag,blank=True,related_name='posts')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news',kwargs={"slug":self.slug})


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering=['created_at']


class Teacher(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обпубликовано')





    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering=['created_at']



class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обпубликовано')


    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'
        ordering = ['created_at']


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обпубликовано')



    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='отзывы'
        ordering = ['created_at']