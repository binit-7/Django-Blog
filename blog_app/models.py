from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)  # unique = true means no two categories can have the same name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories' # to show plural name correctly in admin panel

    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
)    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True) # slug field for SEO friendly URLs, same name as title but with hyphens instead of spaces
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y%m/%d/', blank=True, null=True)
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=5000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    
   