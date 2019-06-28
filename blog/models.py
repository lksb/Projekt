from django.conf import settings
from django.db import models
from django.utils import timezone

category_choices=(
    ('Games','Games'),
    ('Mobile','Mobile'),
    ('Tech','Tech'),
)

platform_choices=(
    ('PC','PC'),
    ('iPhone','iPhone'),
    ('Android','Android'),
    ('Playstation 3','Playstation 3'),
    ('Playstation 4','Playstation 4'),
    ('Xbox One','Xbox One'),
    ('Xbox 360','Xbox 360'),
    ('Nintendo Switch','Nintendo Switch'),
    ('Nintendo Wii U','Nintendo Wii U'),
    ('Nintendo Wii','Nintendo Wii'),
    ('Nintendo 3DS','Nintendo 3DS'),
    ('Nintendo DS','Nintendo DS'),
    ('Playstation Vita','Playstation Vita'),
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=8, choices=category_choices, default='---')
    platform = models.CharField(max_length=20, choices=platform_choices, default='---')
    #events
    eventname = models.CharField(max_length=200, default='')
    eventdate = models.CharField(max_length=20, default='')
    time = models.CharField(max_length=20, default='')
    location = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title