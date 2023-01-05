from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=30)
    
    #additional 
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
    
    # Below code inserted by intellisense auto snippets :
    
    '''
    
            get_email_sent(request,receive  r=[],subject='',context = {},template='emails/progress.html') 
    
    '''
    '''
    from django.conf import settings
    from django.template.loader import render_to_string
    from django.core.mail import EmailMultiAlternatives
    from django.utils.html import strip_tags
    
    def function(request,**kwargs):
        sender = settings.EMAIL_HOST_USER
        receiver = kwargs['receiver']
        subject = kwargs['subject']
        context = kwargs['context']
        html_content = render_to_string(kwargs['template'], context) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
        email = EmailMultiAlternatives(subject, text_content, sender, receiver)
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=True)
        return True

    '''        
   # End inserted code 
   
   
    
    
