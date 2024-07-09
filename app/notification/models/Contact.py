from . import *

class Contact(BaseClassModel):  
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
