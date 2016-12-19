from django import forms
from django.forms import ModelForm, DateInput, DateField, extras
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget


from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ "email", "firstname", "lastname", "phone", "avatar", "contacts" ]
        #form = UserForm();

class EventForm(ModelForm):
    class Meta:
        model = Event
        #fields = '__all__'
        fields = [ "name", "start", "end", "number_of_days", "description",
                'accommodation_type',]
                #"camping", "hotel", "rental", "activities","food"]
        widgets = {
            'name': forms.TextInput(attrs={'style':"width:80%",'placeholder': 'Name of the event you want others to see'}),
            'start':  SelectDateWidget(),
            'end':  SelectDateWidget(),
            'description':  forms.Textarea(attrs={'style':"width:100%",'placeholder': 'The purpose of this event'}),
            'number_of_days': forms.TextInput(attrs={'style':"width:400px",'placeholder': 'Leave empty if exact dates'}),
        }
        help_texts = {
            'start':  ('Approximate dates if it is not decided'),
            'end':  ('Approximate dates if it is not decided'),
        }

class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields=[ "group", "person", "organizer", "reply", "number_of_guests", "replied"]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ "user", "name","accommodation_type", "camping", "hotel", "rental", "activities", "food", "locations"]

"""
class UserEventProfilForm(ModelForm):
    class Meta:
        model = userEventProfile
        fields = [ "user", "event","profile"];
"""

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [ "proximity", "name" ];
        labels = {
            'name': "miles of ",
            "proximity": "Within"
        }
        widgets = {
                'name': forms.TextInput(attrs={'style':"width:300px",'placeholder': 'Street Address or closest city/town, state, zip'}),
                'proximity': forms.TextInput(attrs={'style':"width:60px",'placeholder': 'in miles'})
        }



class CampingForm(ModelForm): 
    class Meta:
        model = CampingOption
        fields = [ "rv", "tent", "tent_drivein", "hotshower", "wifi", "handicap", "swimming", "cabin", "water", "group", "boat", "campfire", "horse", "pet", "others"]

class HotelForm(ModelForm): 
    class Meta:
        model = HotelOption
        fields = ["freewifi", "privatebath", "parking", "restaurant", "gym", "pool", "freebreakfast", "handicap", "others"]

class RentalForm(ModelForm): 
    class Meta:
        model = RentalOption
        fields =["freewifi", "privatebath", "parking", "restaurant", "gym", "pool", "yard", "handicap", "others"]

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields="__all__"
        #fields=[ "art", "family", "food", "shopping", "leisure", "nightlife", "park", "sports", "tourist"]

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields=[ "vegan", "vegetarian", "kosher", "halah", "organic", "fastfood", "meat", "seafood", "desserts", "glutenfree", "three_star_restaurant", "zagat", "family", "grocery", "cafe", "brewery", "raw"]


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields=[ "name", "description", "image","imageURL", "url", "location", "camping","hotel","rental", "activities", "food"]

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields=[ "user","event","venue","start","num_days","price","paid"]


