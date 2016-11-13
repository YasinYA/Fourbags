from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# dr the preparing email process
def prepare_email_content(subject, content, to_email, from_email, cc=[], bcc=[]):
    message_content = EmailMessage(subject=subject, body=content, from_email=from_email, to=[to_email], cc=cc, bcc=bcc)
    return message_content

# send the mail
def send_email(subject, template, context_object, to_email, from_email, cc=[], bcc=[]):
    html_message = render_to_string(template, context_object)
    message = prepare_email_content(subject, html_message, to_email, from_email, cc, bcc)
    message.content_subtype = "html"
    message.send()


