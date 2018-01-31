# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.signals import user_logged_in
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.conf import settings


@python_2_unicode_compatible
class User(AbstractUser):
    phone = PhoneNumberField(blank=True, null=True)
    zip_code = models.CharField(max_length=6)
    pin = models.CharField(max_length=4, blank=True, null=True)
    approved = models.BooleanField(default=False)
    investment_start_date = models.DateTimeField(blank=True, null=True)
    amount_invested = models.DecimalField(default='0.00', max_digits=12, decimal_places=2)
    # class Meta:
    #     ordering = ['-created']

    def __str__(self):
        return self.username

    def logins(self):
        return self.userloginhistory_set.all()

    # def get_absolute_url(self):
    #     return reverse('users:detail', kwargs={'username': self.username})


class UserLoginHistory(models.Model):
    action = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='user_login')
    ip = models.GenericIPAddressField(null=True, default='0.0.0.0')
    browser = models.CharField(max_length=256, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.user.username, self.ip)


class Coin(models.Model):
    id = models.IntegerField(primary_key=True) # "1182"
    baseurl = models.CharField(max_length=100, null=True, blank=True) #  "https://www.cryptocompare.com"
    baseimageurl = models.CharField(max_length=100, null=True, blank=True) #     "https://www.cryptocompare.com"
    url = models.CharField(max_length=100, null=True, blank=True) # "/coins/btc/overview"
    imageurl = models.CharField(max_length=100, null=True, blank=True) #     "/media/19633/btc.png"
    name  = models.CharField(max_length=100) #    "btc"
    symbol = models.CharField(max_length=100) #   "btc"
    coinname = models.CharField(max_length=100) #     "bitcoin"
    fullname = models.CharField(max_length=100) #     "bitcoin (btc)"
    algorithm = models.CharField(max_length=100) #    "sha256"
    prooftype  = models.CharField(max_length=100) #   "pow"
    fullypremined = models.IntegerField() #    "0"
    totalcoinsupply = models.FloatField() #  "21000000"
    sortorder = models.IntegerField() #    "1"
    sponsored = models.BooleanField() #  false  
    type = models.IntegerField(default=0) #     "5"
    flags = models.IntegerField(default=0) #    "4"
    price = models.FloatField(default=0) #  9990.31
    lastupdate = models.FloatField(default=0) #    1517339767
    lastvolume = models.FloatField(default=0) #    0.05
    lastvolumeto = models.FloatField(default=0) #      492.0945
    lasttradeid = models.IntegerField(default=0) #  "2579183"
    volumeday = models.FloatField(default=0) #     122320.22370096412
    volumedayto = models.FloatField(default=0) #   1293796794.3637044
    volume24hour = models.FloatField(default=0) #      133976.55939420077
    volume24hourto = models.FloatField(default=0) #    1425328995.4532254
    openday = models.FloatField(default=0) #   11233.95
    highday = models.FloatField(default=0) #   11263.7
    lowday = models.FloatField(default=0) #    9871.21
    open24hour = models.FloatField(default=0) #    11203.49
    high24hour = models.FloatField(default=0) #    11316.18
    low24hour = models.FloatField(default=0) #     9829.2
    lastmarket = models.CharField(max_length=100, null=True, blank=True) #   "itbit"
    change24hour = models.FloatField(default=0) #      -1213.1800000000003
    changepct24hour = models.FloatField(default=0) #   -10.828590019717073
    changeday = models.FloatField(default=0) #     -1243.6400000000012
    changepctday  = models.FloatField(default=0) #     -11.070371507795576
    supply = models.FloatField(default=0) #    16835712
    mktcap = models.FloatField(default=0) #    168193981950.72
    totalvolume24h = models.FloatField(default=0) #    353725.6138677207
    totalvolume24hto = models.FloatField(default=0) #      3620690171.8505764
    fromsymbol = models.CharField(max_length=10, null=True, blank=True) #   "ƀ"
    startdate = models.DateField(null=True, blank=True) #  "03/01/2009"
    twitter = models.CharField(max_length=100, null=True, blank=True) #  "@bitcoin"
    affiliateurl = models.CharField(max_length=100, null=True, blank=True) #     "https://bitcoin.org/en/"

    def __str__(self):
        return self.name


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    browser = request.META.get('HTTP_USER_AGENT')
    browser = str(browser)
    UserLoginHistory.objects.create(action='user_logged_in', ip=ipaddress, user=user, browser=browser)

