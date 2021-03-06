import os
import logging
from django.contrib.auth.models import User
from django.db import models

from alarm import events


LOGGER = logging.getLogger('mordor')


class Alarm(models.Model):
    """A user alarm."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarms')
    members = models.ManyToManyField(User, related_name='alarm_members')
    active = models.BooleanField(default=False)
    joined = models.DateField(auto_now_add=True)
    label = models.CharField(max_length=150, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    events = events.observable

    @classmethod
    def create(cls, username, password):
        """Create a new alarm."""
        alarm = cls()
        user, created = User.objects.get_or_create(username=username)
        if created is True:
            user.set_password(password)
            user.save()
        alarm.owner = user
        alarm.save()

        return alarm

    @classmethod
    def is_active_for(cls, username):
        # pylint: disable=no-member
        return cls.objects.values('active').get(owner__username=username).get('active')

    @classmethod
    def get_by_username(cls, username):
        # pylint: disable=no-member
        return cls.objects.get(owner__username=username)

    @classmethod
    def notify(cls, event_type, *args, **kwargs):
        """Trigger event."""
        event = getattr(cls.events, event_type, None)
        if not event:
            LOGGER.debug("Ignoring %s, event not defined.", event_type)
        event.trigger(*args, **kwargs)

    def activate(self):
        self.active = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()

    @staticmethod
    def images_upload_path(instance, filename):
        path = "{}/{}".format(instance.alarm.pk, filename)
        return os.path.join(instance.UPLOAD_TO, path)

    def save(self, *args, **kwargs):
        if not self.label:
            self.label = "alarm-{}".format(self.owner.username)

        super(Alarm, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.owner, self.active)


class AlarmImage(models.Model):
    UPLOAD_TO = 'alarm-images'

    alarm = models.ForeignKey(Alarm, related_name='images')
    image = models.ImageField(upload_to=Alarm.images_upload_path)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url
