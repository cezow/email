from django.conf import settings
from .models import Mailbox, Template, Email
from .serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from rest_framework import viewsets
from .filters import EmailFilter
from rest_framework.response import Response
from rest_framework import mixins
import logging
from .tasks import send_email


logger = logging.getLogger('django')


class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
    

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class EmailViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filterset_class = EmailFilter

    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usr_host            = Mailbox.objects.get(login=serializer.validated_data["mailbox"]).host
        usr_port            = Mailbox.objects.get(login=serializer.validated_data["mailbox"]).port
        usr_username        = Mailbox.objects.get(login=serializer.validated_data["mailbox"]).login
        usr_password        = Mailbox.objects.get(login=serializer.validated_data["mailbox"]).password
        usr_use_ssl         = Mailbox.objects.get(login=serializer.validated_data["mailbox"]).use_ssl
        usr_topic           = serializer.validated_data['template']
        usr_body            = Template.objects.get(subject=serializer.validated_data['template']).text
        usr_from_who        = serializer.validated_data['mailbox']
        usr_to              = serializer.validated_data['to'].split()
        usr_cc              = serializer.validated_data['cc'].split()
        usr_bcc             = serializer.validated_data['bcc'].split()
        usr_reply_to        = serializer.validated_data['reply_to'].split()

        if Mailbox.objects.get(login=serializer.validated_data["mailbox"]).is_active == True:
            if Template.objects.get(subject=serializer.validated_data['template']).attachment != '':
                attachment_path = settings.MEDIA_ROOT + '/' + str(Template.objects.get(subject=serializer.validated_data['template']).attachment)
            else:
                attachment_path = ''
        
            for attempt in range(3):
                try:
                    send_email.delay( 
                        host        = str(usr_host),
                        port        = int(usr_port), 
                        username    = str(usr_username), 
                        password    = str(usr_password), 
                        use_ssl     = bool(usr_use_ssl), 
                        topic       = str(usr_topic), 
                        body        = str(usr_body),
                        from_who    = str(usr_from_who), 
                        to          = list(usr_to), 
                        cc          = list(usr_cc),
                        bcc         = list(usr_bcc), 
                        reply_to    = list(usr_reply_to), 
                        attachment  = attachment_path
                    )
                    serializer.save()
                    break
                except Exception as e:
                    logger.error(e)
        
        return Response(serializer.data)