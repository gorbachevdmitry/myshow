from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from parler.models import TranslatableModel, TranslatedFields
from embed_video.fields import EmbedVideoField


class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True, unique_for_date='publish')
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        body = models.TextField(blank=True),
        citata = models.TextField(blank=True),
        anecdot = models.TextField(blank=True)
    )
    category = models.ForeignKey(Category, related_name='products')
    alt_image = models.CharField(max_length=250)
    image_dog = models.ImageField(upload_to='products/%Y/%m/%d',
                                  blank=True)
    alt_image_dog = models.CharField(max_length=250)
    video = EmbedVideoField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)
        # index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
