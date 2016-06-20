from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import get_object_or_404

from x.models  import Temperature, MqttBroker


class Command(BaseCommand):
    help = 'Read temperature function'

    def handle(self, *args, **options):
        import paho.mqtt.client as mqtt
        i = 1
        check = True

        while check is True:
            try:
                Temperature.objects.get(id=i)
                global pk
                pk = i
                check = False
            except Temperature.DoesNotExist:
                i += 1

        if check is False:
            termos = Temperature.objects.get(id=pk)
            topic = termos.data.topic
            broker = MqttBroker.objects.get(topic=topic)

            def on_connect(client, userdata, flags, rc):
                print("Connected with result code " + str(rc))
                client.subscribe(broker.topic)

            def on_message(client, userdata, msg):
                print(str(msg.payload))
                if msg.payload != termos.temperature:
                    termos.temperature = msg.payload
                    termos.save()

            client = mqtt.Client()
            client.username_pw_set(broker.username, broker.password)
            client.on_connect = on_connect

            client.connect(broker.host, broker.port, 60)
            client.on_message = on_message
            client.loop_forever()

