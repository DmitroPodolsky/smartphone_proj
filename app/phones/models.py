from django.db import models
from django.contrib.auth.models import User


class Phones(models.Model):
    name = models.TextField()
    price = models.TextField()
    photo1 = models.TextField()
    photo2 = models.TextField()
    photo3 = models.TextField()
    description = models.TextField()
    version_os = models.TextField()
    corpus = models.TextField()
    sim_card = models.TextField()
    size = models.TextField()
    weight = models.TextField()
    display_type = models.TextField()
    diagonale = models.TextField()
    allow_display = models.TextField()
    photo_kamera = models.TextField()
    front_kamera = models.TextField()
    headphone_jack = models.TextField()
    standart = models.TextField()
    interface = models.TextField()
    prochessor = models.TextField()
    yadra = models.TextField()
    giga_vstoeno = models.TextField()
    giga_operate = models.TextField()
    sloy_card = models.TextField()
    accumulator = models.TextField()
    dop_infa = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    brand = models.TextField()
    audio = models.TextField(default='hello')
    types = models.TextField(default='смартфон')
    count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5)

    def __str__(self):
        return self.name


class AirPods(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    brand = models.TextField()
    price = models.TextField()
    photo1 = models.TextField()
    photo2 = models.TextField()
    type = models.TextField()
    type_connection = models.TextField()
    enterface = models.TextField()
    color = models.TextField()
    anti_shum = models.TextField()
    ambushur = models.TextField()
    type_vipe = models.TextField()
    date_create = models.TextField()
    country = models.TextField()
    garantee = models.TextField()
    time_work = models.TextField()
    description = models.TextField(default='1')
    weight = models.TextField(default='1')
    corpus = models.TextField(default='1')
    vid = models.TextField(default='1')
    dop_infa = models.TextField(default='1')
    types = models.TextField(default='extra')
    count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5)

    def __str__(self):
        return self.name


class Phone_comments(models.Model):
    comment = models.TextField()
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField()
    username = models.TextField(default='1')


class AirPods_comments(models.Model):
    comment = models.TextField()
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    airpod = models.ForeignKey(AirPods, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField()
    username = models.TextField(default='1')


class Bascet_products(models.Model):
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    group_product = models.IntegerField()
    product_id = models.IntegerField()
    product_buy = models.BooleanField(default=False)
    name = models.TextField(default='1')
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=1)
    slug = models.TextField(default='bref')
    image = models.TextField(default='bref')
    time = models.DateTimeField(null=True, blank=True)

    def get_display_price(self):
        return self.price
