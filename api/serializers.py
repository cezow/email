from .models import Mailbox, Template, Email
from rest_framework import serializers


class MailboxSerializer(serializers.HyperlinkedModelSerializer):
    sent = serializers.ReadOnlyField()
    
    class Meta:
        model = Mailbox
        fields = '__all__'
        

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'