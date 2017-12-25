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
    phone = PhoneNumberField()
    zip_code = models.CharField(max_length=6)
    pin = models.CharField(max_length=4)
    approved = models.BooleanField(default=False)
    amount_invested = models.DecimalField(default='0.00', max_digits=12, decimal_places=2)
    # class Meta:
    #     ordering = ['-created']

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('users:detail', kwargs={'username': self.username})


class UserLoginHistory(models.Model):
    action = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='user_login')
    ip = models.GenericIPAddressField(null=True)
    browser =  models.CharField(max_length=256, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    browser = request.META.get('HTTP_USER_AGENT')
    # UserLoginHistory.objects.create(action='user_logged_in', ip=ip, user=user, browser=browser)

