from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254,unique=True) 
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    created = models.DateTimeField('date created', auto_now_add=True)
    avatar = models.ImageField(upload_to='uploads/',blank=True,null=True)
    contacts = models.ManyToManyField('User',blank=True)

    def __str__(self):
        return self.firstname+" "+self.lastname


class Event(models.Model):
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User,related_name="creator")
    created = models.DateTimeField('date created', auto_now_add=True)
    start = models.DateTimeField('date from',blank=True,null=True)
    end = models.DateTimeField('date to',blank=True,null=True)
    number_of_days = models.IntegerField()
    description = models.TextField(max_length = 500)
    particpants = models.ManyToManyField(
                    User,
                    through='RSVP',
                    through_fields=('group', 'person'),
                    blank=True,
                    related_name="participants"
                )
    locations = models.ManyToManyField('Location',blank=True)
    ACCOMMODATION_CHOICES = (
        ('C', 'Camping/RV'),
        ('R', 'Rental Property'),
        ('H', 'Hotel/Motel/BnB'),
    )
    accommodation_type = models.CharField(
        max_length=1,
        choices=ACCOMMODATION_CHOICES,
        default='H',
    )
    camping = models.ForeignKey('CampingOption',blank=True,null=True) 
    hotel = models.ForeignKey('HotelOption',blank=True,null=True) 
    rental = models.ForeignKey('RentalOption',blank=True,null=True) 
    #accommodation = models.ForeignKey('Accommodation',blank=True,null=True)
    activities = models.ForeignKey('Activity',blank=True) 
    food = models.ForeignKey('Food',blank=True) 

    def __str__(self):
        return "{0} ({1})".format(self.name,self.start)

class RSVP(models.Model):
    group = models.ForeignKey(Event, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.BooleanField(default=False)
    REPLY_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('U', 'Undecided'),
    )
    reply = models.CharField(
        max_length=1,
        choices=REPLY_CHOICES,
        default='U',
    )
    number_of_guests = models.IntegerField(default=1)
    invited = models.DateTimeField('invited on', auto_now_add=True)
    replied = models.DateTimeField('replied on', auto_now_add=False)

    def __str__(self):
        return "{0} {1} {2}".format(self.group.name,self.person.firstname,self.reply)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    ACCOMMODATION_CHOICES = (
        ('C', 'Camping/RV'),
        ('R', 'Rental Property'),
        ('H', 'Hotel/Motel/BnB'),
    )
    accommodation_type = models.CharField(
        max_length=1,
        choices=ACCOMMODATION_CHOICES,
        default='H',
    )
    camping = models.ForeignKey('CampingOption',blank=True,null=True) 
    hotel = models.ForeignKey('HotelOption',blank=True,null=True) 
    rental = models.ForeignKey('RentalOption',blank=True,null=True) 
    activities = models.ForeignKey('Activity',blank=True) 
    food = models.ForeignKey('Food',blank=True) 
    locations = models.ManyToManyField('Location',blank=True)

    def __str__(self):
        return self.name

class UserEventProfile(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return "{0} {1}".format(self.event.name,self.profile.name)


class Location(models.Model):
    name = models.CharField(max_length = 500)
    lat_coord = models.FloatField(blank=True)
    long_coord = models.FloatField(blank=True)
    proximity = models.IntegerField(default=10)

    def __str__(self):
        if self.proximity == 0:
            return self.name
        else:
            return "within {0} miles of {1} ".format(self.proximity, self.name)


class Accommodation(models.Model): 
    cc={
    'C': 'Camping/RV',
    'R': 'Rental Property',
    'H': 'Hotel/Motel/BnB'}
    ACCOMMODATION_CHOICES = (
        ('C', 'Camping/RV'),
        ('R', 'Rental Property'),
        ('H', 'Hotel/Motel/BnB'),
    )
    accommodation_type = models.CharField(
        max_length=1,
        choices=ACCOMMODATION_CHOICES,
        default='H',
    )
    def __str__(self):
        return cc[self.accommodation_type]

class CampingOption(models.Model): 
    rv = models.BooleanField(default=False)
    tent = models.BooleanField(default=False)
    tent_drivein = models.BooleanField(default=False)
    hotshower = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    handicap = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    cabin = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    group = models.BooleanField(default=False)
    boat = models.BooleanField(default=False)
    campfire = models.BooleanField(default=False)
    horse = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    others = models.CharField(max_length = 500,blank=True)

    def __str__(self):
        options = []
        for f in self.__dict__:
            if f != 'id' and self.__dict__[f] == True:
               options.append(str(f))
        return ", ".join(options)

class HotelOption(models.Model): 
    freewifi = models.BooleanField(default=False)
    privatebath = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    freebreakfast = models.BooleanField(default=False)
    handicap = models.BooleanField(default=False)
    others = models.CharField(max_length = 500,blank=True)

    def __str__(self):
        options = []
        for f in self.__dict__:
            if f != 'id' and self.__dict__[f] == True:
               options.append(str(f))
        return ", ".join(options)

class RentalOption(models.Model): 
    freewifi = models.BooleanField(default=False)
    privatebath = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    yard = models.BooleanField(default=False)
    handicap = models.BooleanField(default=False)
    others = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self):
        options = []
        for f in self.__dict__:
            if f != 'id' and self.__dict__[f] == True:
               options.append(str(f))
        return ", ".join(options)

class Activity(models.Model):
    art = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    leisure = models.BooleanField(default=False)
    nightlife = models.BooleanField(default=False)
    park = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    tourist = models.BooleanField(default=False)
    hiking = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    beach = models.BooleanField(default=False)
    outdoors = models.BooleanField(default=False)
    rockclimbing = models.BooleanField(default=False)
    fishing = models.BooleanField(default=False)
    adventure_sports = models.BooleanField(default=False)

    def __str__(self):
        options = []
        for f in self.__dict__:
            if f != 'id' and self.__dict__[f] == True:
               options.append(str(f))
        return ", ".join(options)

class Food(models.Model):
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    kosher = models.BooleanField(default=False)
    halah = models.BooleanField(default=False)
    organic = models.BooleanField(default=False)
    fastfood = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    seafood = models.BooleanField(default=False)
    desserts = models.BooleanField(default=False)
    glutenfree = models.BooleanField(default=False)
    three_star_restaurant = models.BooleanField(default=False)
    zagat = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    grocery = models.BooleanField(default=False)
    cafe = models.BooleanField(default=False)
    brewery = models.BooleanField(default=False)
    raw = models.BooleanField(default=False)

    def __str__(self):
        options = []
        for f in self.__dict__:
            if f != 'id' and self.__dict__[f] == True:
               options.append(str(f))
        return ", ".join(options)

class Business(models.Model):
    name = models.CharField(max_length=256); # yes, no, undecided
    description = models.TextField(max_length=1024); # yes, no, undecided
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    imageURL = models.URLField(max_length=200,blank=True,null=True)
    url = models.URLField(max_length=200,blank=True,null=True)
    location = models.ForeignKey(Location)
    ACCOMMODATION_CHOICES = (
        ('C', 'Camping/RV'),
        ('R', 'Rental Property'),
        ('H', 'Hotel/Motel/BnB'),
        ('N', 'None'),
    )
    accommodation_type = models.CharField(
        max_length=1,
        choices=ACCOMMODATION_CHOICES,
        default='H',
    )
    camping = models.ForeignKey('CampingOption',blank=True,null=True) 
    hotel = models.ForeignKey('HotelOption',blank=True,null=True) 
    rental = models.ForeignKey('RentalOption',blank=True,null=True) 
    activities = models.ForeignKey(Activity,blank=True,null=True) 
    food = models.ForeignKey(Food,blank=True,null=True)

    def __str__(self):
        return "{0} {1}".format(self.name,self.location)
  
class Options(models.Model):
    user = models.ForeignKey('User')
    event = models.ForeignKey('Event')
    venue = models.ForeignKey('Business')
    distance = models.IntegerField(default= 100)
    points = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return "{0} {1} {2}".format(self.user.firstname, self.event.name, self.venue.name)

class Booking(models.Model):
    user = models.ForeignKey('User')
    event = models.ForeignKey('Event')
    venue = models.ForeignKey('Business')
    start = models.DateTimeField('startdate', auto_now_add=False)
    num_days = models.IntegerField()
    price = models.FloatField(default=0)
    paid = models.FloatField(default=0)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.user.firstname, self.event.name, self.venue.name, self.start)


