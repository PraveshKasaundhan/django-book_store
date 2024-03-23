from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=10)

    def __str__(self):
        return f"ID: {self.id} |Country: {self.name}, {self.code}\n"

    class Meta:
        verbose_name_plural="Countries"

class Address(models.Model):
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    code=models.CharField(max_length=10)

    def full_address(self):
        return f"{self.street}, {self.city}, {self.code}"
    
    def __str__(self):
        return f"ID: {self.id} |City: {self.city}\n"
    
    class Meta:
        # versbose_name = "Address"  #not required
        verbose_name_plural = "Address_Entries"  # to fix Addresss

class Author(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.f_name} {self.l_name}"
    
    def __str__(self):
        return f"ID:{self.id} |Name: {self.full_name()}\n"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=(MinValueValidator(1),MaxValueValidator(5)))
    # author = models.CharField(null=True,max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,related_name="books")
    is_best = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False, db_index=True)
    countries = models.ManyToManyField(Country)

#Do not need below code anymore because we configure the ModelAdmin
    # def save(self, *args, **kwargs):
    #     self.slug=slugify(self.title)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return f"ID: {self.id} |Title: {self.title} \n"
