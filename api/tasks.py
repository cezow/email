
from celery import shared_task
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend



@shared_task
def send_email(host, port, username, password, use_ssl, topic, body, from_who, to, cc, bcc, reply_to, attachment):

    backend = EmailBackend(
        host            = host,
        port            = port , 
        username        = username,
        password        = password,
        use_ssl         = use_ssl, 
        fail_silently   = False
    )

    email = EmailMessage(
        topic,
        body,
        from_who,
        to,
        cc          = cc,
        bcc         = bcc,
        reply_to    = reply_to,
        connection  = backend
    )

    if attachment != '':
        email.attach_file(rf"{attachment}")

    sent = email.send()
    return sent
