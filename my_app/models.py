from django.db import models
from django.db import models
class Portfolio(models.Model):
    title=models.CharField(max_length=120,verbose_name="title",help_text="product jazin'")
    text=models.TextField(verbose_name="desciption",help_text="komment qaldirin'")
    img=models.ImageField(verbose_name="image or picture",upload_to="products/")


    def __str__(self):
        return self.title
# Create your models here.
class About(models.Model):
    company_name = models.CharField(max_length=120, verbose_name="company", help_text="kompaniya ati")
    slogan = models.CharField(max_length=200, verbose_name="Slogan", blank=True)
    description = models.TextField(verbose_name="Kompaniya haqinda")
    logo = models.ImageField(upload_to="about/", verbose_name="Logo")
    founded_year = models.IntegerField(verbose_name="jaratilg'an jil")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    address = models.CharField(max_length=255, verbose_name="Ma'nzil")

    def __str__(self):
        return self.company_name


class Home(models.Model):
    title = models.CharField(max_length=200, verbose_name="home")
    description = models.TextField(verbose_name="description")
    button_text = models.CharField(max_length=50, verbose_name="Button")
    demo_link = models.URLField(verbose_name="link", blank=True)
    hero_image = models.ImageField(upload_to="home/", verbose_name="img")

    def __str__(self):
        return self.title


class ServiceSection(models.Model):

    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(upload_to="services/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class cm(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject = models.CharField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f'{self.name} - {self.subject}'
# Create your models here.
