from django.db import models


class Teacher(models.Model):
    """
    class model for teacher data
    """
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    teacher_subject = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True)
    biography = models.TextField()

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчителі'


class Timetable(models.Model):
    """
    class for model timetable and call schedule
    """
    lesson_picture = models.ImageField(upload_to='images_timetable')
    date_of_publication = models.DateTimeField()

    class Meta:
        verbose_name = 'Розклад уроків'
        verbose_name_plural = 'Розклади уроків'
        # ordering = ('-date_of_publication',)


class Call_schedule(models.Model):
    """
    class model for call
    """
    call_picture = models.ImageField(upload_to='images_call')
    date_of_publication = models.DateTimeField()

    class Meta:
        # verbose_name = 'Розклад уроків'
        verbose_name_plural = 'Розклад дзвінків'


class News_main(models.Model):
    picture = models.ImageField(upload_to='images_news', null=True)
    title = models.CharField(max_length=40)
    date_public = models.DateTimeField()
    text_news = models.TextField()

    class Meta:
        ordering = ('-date_public',)
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class Gallery(models.Model):
    """
    model
    """
    image = models.ImageField(upload_to='gallery')
    article = models.ForeignKey(News_main, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Pride_school(models.Model):
    """
    models for collect the best children
    """
    image = models.ImageField(upload_to='pride_school')
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    grade = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Гордість школи'
        verbose_name_plural = 'Гордість школи'
