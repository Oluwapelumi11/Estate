from django.db import models
from agents.models import Agent

# Create your models here.
class Property(models.Model):
    title = models.CharField('Title', max_length=100)
    owner = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property_type = (
        ("LIVING HOUSE", "Living House"),
        ("HOUSE VILLA", "House Villa"),
        ("HOUSE APARTMENT", "House Apartment"),
        ("OFFICE FLOOR", "Office Floor")
    )
    type = models.CharField("Property Type", choices=property_type, default="LIVING HOUSE", max_length=20)
    price = models.DecimalField('Price', max_digits=20, decimal_places=2)
    street = models.CharField('Street Address', max_length=100)
    city = models.CharField('City',max_length=30)
    zip_code = models.CharField("Zip Code", max_length=15)
    status = models.CharField("Status",max_length=30)
    date_listed = models.DateField("Listing Data", auto_now_add=True)
    plot_size = models.IntegerField("Plot Size")
    roof_type = models.CharField("Roof Type",max_length=50)
    construction_company = models.CharField("Construction Company", max_length=50)
    cooling = models.CharField("Cooling", max_length=50)
    interior_size = models.CharField("Interior Size",max_length=50)
    bedroom = models.IntegerField("Bedroom")
    bedroom_size = models.CharField("Bedroom Size",max_length=50)
    bathroom = models.IntegerField("Bathroom")
    bathroom_size = models.CharField("Bathroom Size",max_length=50)
    garage = models.IntegerField("Garage Capacity")
    laundry_room_equipment = models.CharField("Laundry Equipments", max_length=50)
    living_room_size = models.CharField("Living Room Size",max_length=50)
    kitchen = models.CharField("Kitchen Size",max_length=50)


    # bedroom


    def __str__(self):
        return f"{self.title} - {self.city}"



