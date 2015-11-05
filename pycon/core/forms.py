from django.contrib.auth import get_user_model
from django.forms import ModelForm

class SignupForm(ModelForm):
    '''
    We are extending fields required by django-allauth during the
    signup process
    '''
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
    def save(self, user):
        user.save()
