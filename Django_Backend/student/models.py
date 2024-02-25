from django.db import models
from PIL import Image
from django.utils import timezone

# Create your models here.    
class Pupil(models.Model): 

    YEAR_CHOICES = [
        ('F.E.', 'First year'),
        ('S.E.', 'Second year'),
        ('T.E.', 'Third year'),
        ('B.E.', 'Fourth year')
    ]

    BatchChoice = models.TextChoices('BatchChoice', 'A B C D')

    uid = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    middle_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    img = models.ImageField(default = 'default.jpg', upload_to = 'student_pics')
    batch = models.CharField(max_length = 1, choices = BatchChoice.choices, default='A')
    year = models.CharField(max_length = 5, choices = YEAR_CHOICES, default='F.E.')

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)

class Attendance(models.Model):

    STATUS_CHOICES = [
        ('AB', 'Absent'),
        ('P', 'Present')
    ]

    pupils = models.ManyToManyField(Pupil)
    attend_date = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 2, choices = STATUS_CHOICES, default = 'AB')
