from django.db import models
from agents.models import Agent

# Create your models here.
class Property(models.Model):
    title = models.CharField('Title', max_length=100)
    owner = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property_category_choice = (
        ("LIVING HOUSE", "Living House"),
        ("HOUSE VILLA", "House Villa"),
        ("HOUSE APARTMENT", "House Apartment"),
        ("OFFICE FLOOR", "Office Floor")
    )
    property_category = models.CharField("Property Category", choices=property_category_choice, default="LIVING HOUSE", max_length=20,blank=True,null=True)
    property_type = models.CharField("Property Type", max_length=50, null=True, blank=True)
    price = models.DecimalField('Price', max_digits=20, decimal_places=2,blank=True,null=True)
    street = models.CharField('Street Address', max_length=100,blank=True,null=True)
    city = models.CharField('City',max_length=30,blank=True,null=True)
    zip_code = models.CharField("Zip Code", max_length=15,blank=True,null=True)
    status = models.CharField("Status",max_length=30,blank=True,null=True)
    date_listed = models.DateField("Listing Data", auto_now_add=True,blank=True,null=True)
    plot_size = models.IntegerField("Plot Size",blank=True,null=True)
    roof_type = models.CharField("Roof Type",max_length=50,blank=True,null=True)
    construction_company = models.CharField("Construction Company", max_length=50,blank=True,null=True)
    cooling = models.CharField("Cooling", max_length=50,blank=True,null=True)
    interior_size = models.CharField("Interior Size",max_length=50,blank=True,null=True)
    bedroom = models.IntegerField("Bedroom",blank=True,null=True)
    bedroom_size = models.CharField("Bedroom Size",max_length=50,blank=True,null=True)
    bathroom = models.IntegerField("Bathroom",blank=True,null=True)
    bathroom_size = models.CharField("Bathroom Size",max_length=50,blank=True,null=True)
    garage = models.IntegerField("Garage Capacity",blank=True,null=True)
    laundry_room_equipment = models.CharField("Laundry Equipments", max_length=50,blank=True,null=True)
    living_room_size = models.CharField("Living Room Size",max_length=50,blank=True,null=True)
    kitchen = models.CharField("Kitchen Size",max_length=50,blank=True,null=True)
    featured = models.BooleanField(("Feature This Property"), default=False)
    description = models.TextField(("Property Description"),null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.city}"


class Image(models.Model):
    property = models.ForeignKey(Property, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(("Add Image"), upload_to="Properties/",null=True, blank=True)

    def __str__(self):
        return f"{self.property.title} - Image"

    # bedroom





