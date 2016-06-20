from django.db import models


class Gpio(models.Model):
    STATE = (
        ('gpio.HIGH', 'HIGH'),
        ('gpio.LOW', 'LOW'),
    )

    ACTIONS = (
        ('toggle light', 'toggle light'),
        ('lock', 'lock'),
        # ('camera', 'camera'),
    )

    STATUS = (
        ('UNDEFINED', 'Undefined'),
        ('ON', 'ON'),
        ('OFF', 'OFF'),
    )


class Room(models.Model):
    name = models.CharField(max_length=70, blank=False, null=False)

    def __str__(self):
        return self.name


class GpioR2(models.Model):
    CHOICES = ((2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12),  (13, 13),
               (14, 14), (15, 15), (16, 16), (17, 17), (19, 19), (18, 18), (20, 20), (21, 21), (22, 22), (23, 23),
               (24, 24), (25, 25), (26, 26), (27, 27))
    room = models.ForeignKey(Room)
    item = models.CharField(max_length=50, default='')
    pin = models.IntegerField(choices=CHOICES)
    action = models.CharField(choices=Gpio.ACTIONS, max_length=30, default='')
    status = models.CharField(choices=Gpio.STATUS, default='', max_length=10, )

    def __str__(self):
        return self.item


class MqttBroker(models.Model):
    host = models.TextField()
    port = models.IntegerField()
    username = models.CharField(blank=False, null=False, default='', max_length=30)
    password = models.TextField()
    topic = models.CharField(max_length=200, blank=False, null=False)


class Temperature(models.Model):
    room = models.ForeignKey(Room, blank=False)
    temperature = models.FloatField(blank=True, null=True)
    data = models.ForeignKey(MqttBroker, blank=True, null=True)
