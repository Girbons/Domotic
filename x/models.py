from django.db import models


class Gpio(models.Model):
    STATE = (
        ('gpio.HIGH', 'HIGH'),
        ('gpio.LOW', 'LOW'),
    )

    COMMANDS = (
        ('gpio.setmode', 'setmode_BOARD'),
        ('gpio.setmode', 'setmode_BCM'),
        ('gpio.setup', 'setup'),
        ('gpio.input', 'input'),
        ('gpio.output', 'output'),
    )


class GpioR1(models.Model):
    CHOICES = ((0, 0), (1, 1), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14),
                 (15, 15), (18, 18), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25))
    text = models.CharField(max_length=50, default='configuration name')
    pin = models.IntegerField(choices=CHOICES)
    command = models.CharField(choices=Gpio.COMMANDS, max_length=30)

    def __str__(self):
        return self.text


class GpioR2(models.Model):
    CHOICES = ((2, 2), (3, 3), (4, 4), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (14, 14),
                 (15, 15), (17, 17), (18, 18), (22, 22), (23, 23), (24, 24), (25, 25),)
    text = models.CharField(max_length=50, default='configuration name  ')
    pin = models.IntegerField(choices=CHOICES)
    command = models.CharField(choices=Gpio.COMMANDS, max_length=30)

    def __str__(self):
        return self.text