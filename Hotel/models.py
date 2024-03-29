from django.db import models

CATEGORY_CHOICES = (
    ("Rooms & Apartments", "Rooms & Apartments"),
    ("Food & Restaurant", "Food & Restaurant"),
    ("Spa & Fitness", "Spa & Fitness"),
    ("Sports & Gaming", "Sports & Gaming"),
    ("Event & Party", "Events & Party"),
    ("GYM & Yoga", "GYM & Yoga")
)


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="Products_images")


    class Meta:
        verbose_name_plural = "Products"


    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name
    


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Reviews_images")

    class Meta:
        verbose_name_plural = "Reviews"


    def __str__(self):
        return self.name
    


class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="staff_images")


    class Meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.name
        


class Contact(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   subject = models.CharField(max_length=100)
   message = models.TextField()

   class Meta:
       verbose_name_plural = "Contacts"

   def __str__(self):
      return self.name