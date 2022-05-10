import uuid
from django.db import models


class Mailbox(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host        = models.CharField(max_length=64, blank=False, null=False)
    port        = models.IntegerField(default=465, blank=False, null=False)
    login       = models.CharField(max_length=64, blank=False, null=False, unique=True)
    password    = models.CharField(max_length=64, blank=False, null=False)
    email_from  = models.CharField(max_length=64, blank=False, null=False)
    use_ssl     = models.BooleanField(default=True, blank=False, null=False)
    is_active   = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def sent(self):
        return Email.objects.filter(mailbox=self.id).count()

    def __str__(self):
        return f"{self.login}"


class Template(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject     = models.CharField(max_length=64, blank=False, null=False)
    text        = models.TextField(max_length=64, blank=False, null=False)
    attachment  = models.FileField(null=True)
    date        = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject}"


class Email(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox     = models.ForeignKey(Mailbox, blank=False, null=False, on_delete=models.CASCADE, related_name='emails')
    template    = models.ForeignKey(Template, blank=False, null=False, on_delete=models.CASCADE, related_name='emails')
    to          = models.CharField(max_length=64, blank=True)
    cc          = models.CharField(max_length=64, blank=True)
    bcc         = models.CharField(max_length=64, blank=True)
    reply_to    = models.CharField(max_length=64 ,null=True, blank=False)
    sent_date   = models.DateField(default=None)
    date        = models.DateField(auto_now_add=True)
