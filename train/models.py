import email
from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

STATION_CHOICES = (
    ("None", "None"),
    ("Virar", "Virar"),
    ("Nallasopara", "Nallasopara"),
    ("Vasai Road", "Vasai Road"),
    ("Naigaon", "Naigaon"),
    ("Bhayandar", "Bhayandar"),
    ("Mira Road", "Mira Road"),
    ("Dahisar", "Dahisar"),
    ("Borivali", "Borivali"),
    ("Kandivali", "Kandivali"),
    ("Malad", "Malad"),
    ("Goregaon", "Goregaon"),
    ("Ram Mandir", "Ram Mandir"),
    ("Jogeshwari", "Jogeshwari"),
    ("Andheri", "Andheri"),
    ("Vile Parle", "Vile Parle"),
    ("Santacruz", "Santacruz"),
    ("Khar Road", "Khar Road"),
    ("Bandra", "Bandra"),
    ("Mahim Junction", "Mahim Junction"),
    ("Matunga Road", "Matunga Road"),
    ("Dadar", "Dadar"),
    ("Prabhadevi", "Prabhadevi"),
    ("Lower Parel", "Lower Parel"),
    ("Mahalaxmi", "Mahalaxmi"),
    ("Mumbai Central", "Mumbai Central"),
    ("Grant Road", "Grant Road"),
    ("Charni Road", "Charni Road"),
    ("Marine Lines", "Marine Lines"),
    ("Churchgate", "Churchgate")
)

TICKET_TYPE_CHOICES = (
    ("Journey", "Journey"),
    ("Single", "Single")
)

TICKET_CLASS_TYPE_CHOICES = (
    ("First", "First"),
    ("Second", "Second")
)

TICKET_TRAIN_TYPE_CHOICES = (
    ("Ordinary", "Ordinary"),
    ("Air Conditioned", "Air Conditioned")
)

TICKET_PAYMENT_TYPE_CHOICES = (
    ("Payment Gateway", "Payment Gateway"),
    ("R Wallet", "R Wallet")
)

class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, password=None):
        if not name:
            raise ValueError("Users must enter a name!")
        if not username:
            raise ValueError("Users must have a valid mobile no.")

        user  = self.model(
                name = name,
                username = username,
			)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, password):
        user  = self.create_user(
                username = username,
				name=name,
                password=password
			)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    name                    = models.CharField(verbose_name='name', max_length=100)
    username                = models.CharField(verbose_name = 'phone_no', max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    city                    = models.CharField(verbose_name='City', max_length=20, null=True)
    address                 = models.TextField(verbose_name="Address", max_length=200, null=True)
    email                   = models.EmailField(verbose_name='Email', max_length=30, null = True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['name']

    objects = MyAccountManager()
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Train(models.Model):
    train_id                = models.IntegerField(verbose_name='Train ID', primary_key=True)
    train_source            = models.CharField(verbose_name='Train Source', choices=STATION_CHOICES, null=False, default="None", max_length=20)
    train_destination       = models.CharField(verbose_name='Train Destination', choices=STATION_CHOICES, null=False, default="None", max_length=20)
    train_time              = models.TimeField(verbose_name='Train Time', auto_now=False, auto_now_add=False)

class Ticket(models.Model):
    ticket_id               = models.IntegerField(verbose_name='Ticket ID', primary_key=True)
    ticket_source           = models.CharField(verbose_name='Ticket Source', choices=STATION_CHOICES, null=False, default="None", max_length=20)
    ticket_destination      = models.CharField(verbose_name='Ticket Destination', choices=STATION_CHOICES, null=False, default="None", max_length=20)
    ticket_type             = models.CharField(verbose_name='Ticket Type', choices=TICKET_TYPE_CHOICES, null=False, default="None", max_length=20)
    ticket_class            = models.CharField(verbose_name='Ticket Class', choices=TICKET_CLASS_TYPE_CHOICES, null=False, default="None", max_length=20)
    ticket_train            = models.CharField(verbose_name='Ticket Train', choices=TICKET_TRAIN_TYPE_CHOICES, null=False, default="None", max_length=20)
    ticket_payment          = models.CharField(verbose_name='Ticket Payment Method', choices=TICKET_PAYMENT_TYPE_CHOICES, null=False, default="None", max_length=20)
    ticket_booked_at        = models.DateTimeField(verbose_name='Ticket Booked at', auto_now_add=True)
    ticket_fare             = models.SmallIntegerField(verbose_name='Ticket Fare', null=False, default=0)
    ticket_user             = models.ForeignKey(Account, verbose_name='Ticket Holder', related_name="Ticket_Holder", null=False, default=None, on_delete=models.DO_NOTHING)