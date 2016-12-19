from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.db.models import Q, Prefetch
from django.forms.models import model_to_dict
import random


import requests

from .models import *
from forms import *

# Create your views here.
#def index(request):
    # return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):
    user = User.objects.get(firstname="Leah")
    events = Event.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'db.html', {'events': events,'profiles': profiles, 'user':user})

def login(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('password',''):
            errors.append('Enter a password')
        if request.POST.get('email', '') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address')
        if not errors:
            user = User.objects.get(email=request.POST.get('email'))
            return HttpResponseRedirect('/user/{0}'.format(user.id))

    return render_to_response('index.html', { 'errors': errors, 'starting': 'login' }, context_instance=RequestContext(request))

def putInHash(gg,ss):
    for s in str(ss).split(","):
        try:
            n = gg[ s.strip() ]
            gg[ s.strip() ] = n + 1
        except:
            gg[ s.strip() ] = 1
    return gg

def collectInterest(eid):
    gg = {};
    ueps = UserEventProfile.objects.filter(event__id=eid)
    for u in ueps:
        ss = Activity.objects.get(id = u.profile.activities.id)
        putInHash(gg,ss)
    return gg

def collectFood(eid):
    gg = {};
    ueps = UserEventProfile.objects.filter(event__id=eid)
    for u in ueps:
        ss = Food.objects.get(id = u.profile.food.id)
        putInHash(gg,ss)
    return gg

def collectCamping(eid):
    gg = {};
    ueps = UserEventProfile.objects.filter(event__id=eid)
    for u in ueps:
        ss = CampingOption.objects.get(id = u.profile.camping.id)
        putInHash(gg,ss)
    return gg

def index(request):
    return login(request)
    #return render(request, 'index.html')

def user(request,uid):
    user = User.objects.get(id=uid)
    events = Event.objects.filter(Q(creator=user) | Q( rsvp__person=user)).distinct()
    #events = Event.objects.filter(Q(rsvp__person=user)).distinct()
    profiles = Profile.objects.filter(user=uid)
    return render(request, 'user.html', {'events': events,'profiles': profiles, 'user':user})

"""
def index(request):
    user = User.objects.get(firstname="Leah")
    events = Event.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'events': events,'profiles': profiles, 'user':user})
"""

def newevent(request, uid, id):
    user = User.objects.get(id=uid)
    #event = Event.objects.create()
    #form = EventForm(request.POST or None, instance=event)
    form = EventForm(request.POST or None)
    """
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    """
    return render(request, 'newevent.html', {'user':user,
        'event': event, 'form': form}) #, 'rsvp':rsvp, 'participants':participants, 'profiles': profiles, 'user':user})


def event(request, uid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=id)
    profiles = UserEventProfile.objects.filter(user=uid, event=event.id).prefetch_related()
    camp = collectCamping(id)
    food = collectFood(id)
    activity = collectInterest(id)
    putInHash(activity, event.activities)
    putInHash(food, event.food)
    participants = User.objects.filter(rsvp__group= event)
    form = LocationForm()
    rsvp = RSVP.objects.filter(group= event).prefetch_related(
       Prefetch('person', queryset=User.objects.order_by('firstname')))
    locations =Location.objects.filter(event= event)
    return render(request, 'event.html', {'event': event, 'locations': locations,
        'p': "Summary",
        'camp': camp,
        'foods': food,
        'activities': activity,
        'form':form,
        'rsvp':rsvp, 'participants':participants, 'profiles': profiles, 'user':user})


def profile(request,uid,id):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=id)
    foods = []
    accommodation = []
    activity = []
    locations = []
    if profile.food:
        for f in profile.food.__dict__:
            if profile.food.__dict__[f] == True:
               foods.append(f)
    if profile.activities:
        for f in profile.activities.__dict__:
            if profile.activities.__dict__[f] == True:
               activity.append(f)
    if profile.accommodation_type == "C":
        if profile.camping:
            for f in profile.camping.__dict__:
                if profile.camping.__dict__[f] == True:
                   accommodation.append(f)
    elif profile.accommodation_type == "R":
        if profile.rental:
            for f in profile.rental.__dict__:
                if profile.rental.__dict__[f] == True:
                   accommodation.append(f)
    elif profile.accommodation_type == "H":
        if profile.hotel:
            for f in profile.hotel.__dict__:
                if profile.hotel.__dict__[f] == True:
                   accommodation.append(f)
    contacts = User.objects.filter(user__id=uid)
    #contacts = User.objects.filter(contacts=uid)
        #profile = UserEventProfile.objects.get(user=uid, event=event.id)
    #profile = UserEventProfile.objects.get(user=uid, event=event.id)
    return render(request, 'profile.html',
            {'profile': profile,
                'p': "Summary",
                'foods': foods,
                'accommodation': accommodation,
                'activity': activity,
                'locations': locations,
                'contacts': contacts,
                'user':user})

def food(request,uid,pid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    food = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=food)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'food.html', {'form': form,
        'p': "Food",
        'user':user,'event': event, 'food': food})

def activity(request,uid,pid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    activity = Activity.objects.get(id=id)
    form = ActivityForm(request.POST or None, instance=activity)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'activity.html', {'form': form,
        'p': "Interests",
        'user':user,'event': event, 'activity': activity})

def camping(request,uid,pid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    camping = CampingOption.objects.get(id=id)
    form = CampingForm(request.POST or None, instance=camping)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'camping.html', {'form': form,
        'p': "Camping",
        'user':user,'event': event, 'camping': camping})

def rental(request,uid,pid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    rental = RentalOption.objects.get(id=id)
    form = RentalForm(request.POST or None, instance=rental)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'camping.html', {'form': form,
        'p': "Rental",
        'user':user,'event': event})

def addlocation(request,uid,pid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    location = Location.objects.get(id)
    form = LocationForm(request.POST or None, instance=location)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'location.html', {'form': form, 'user':user,'event': event, 'location': location})

def location(request,uid,pid):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=pid)
    location = Location.objects.filter(profile=profile)
    form = LocationForm()
    return render(request, 'location.html', {'form': form, 'user':user,'profile': profile, 'locations': location})

def pfood(request,uid,pid, id):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=pid)
    food = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=food)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'pfood.html', {'form': form, 'user':user,'profile': profile,
        'p': "Food",
        'food': food})

def pactivity(request,uid,pid, id):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=pid)
    activity = Activity.objects.get(id=id)
    form = ActivityForm(request.POST or None, instance=activity)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'pactivity.html', {'form': form,
        'p': "Interests",
        'user':user,'profile': profile, 'activity': activity})

def pcamping(request,uid,pid, id):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=pid)
    camping = CampingOption.objects.get(id=id)
    form = CampingForm(request.POST or None, instance=camping)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'pcamping.html', {'form': form, 'user':user,
        'p': "Camping",
        'profile': profile, 'camping': camping})

def business(request,uid,eid,id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=eid)
    business = Business.objects.get(id=id)
    return render(request, 'venue.html', {'user':user,'event': event,
        'p': "Booking",
        'venue': business})

def booking(request,uid,eid,id):
    accomm={ 'C': 'Camping/RV', 'R': 'Rental Property', 'H': 'Hotel/Motel/BnB' }
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=eid)

    booking = Booking.objects.filter(event__id=eid)
    for b in booking:
            venue= Business.objects.get(id=b.venue.id)
            b.name = venue.name
            b.imageURL = venue.imageURL
            b.description = venue.description
            b.location = Location.objects.get(business__id= b.venue.id)

    options = Options.objects.filter(event_id=eid)
    business = []
    for venue in options:
        b =  Business.objects.get(id=venue.id)
        b.votes = venue.votes
        b.distance = venue.distance
        b.accommodation_type = accomm[b.accommodation_type]
        b.ammenities = "{0},{1}".format(b.activities, b.food or "")
        business.append(b)
    """
    try:
    except:
        booking = None
    """

    #form = BookingForm(request.POST or None, instance=booking)
    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'booking.html', {'form': form, 'user':user,
        'p': "Booking",
        'event': event, 'venues': business, 'booking':booking})

def pcontacts(request,uid, pid):
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(id=pid)
    #contacts = User.objects.filter(contacts=uid)
    contacts = User.objects.filter(user__id=uid)
    return render(request, 'contacts.html', { 'user':user,
        'p': "Contacts",
        'contacts': contacts, 'profile': profile })

def econtacts(request,uid, pid):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=pid)
    #contacts = User.objects.filter(contacts=uid)
    contacts = User.objects.filter(user__id=uid)
    participants = User.objects.filter(rsvp__group= event)
    return render(request, 'contacts.html', { 'user':user,
        'p': "Contacts",
        'contacts': contacts, 'event':event})


def rsvp(request, uid, id):
    user = User.objects.get(id=uid)
    event = Event.objects.get(id=id)
    camps = collectCamping(id)
    foods = collectFood(id)
    activities = collectInterest(id)
    putInHash(activities, event.activities)
    putInHash(foods, event.food)
    """
    activities=Activity.objects.get(id=event.activities.id)
    foods=Food.objects.get(id=event.food.id)
    """
    profiles = UserEventProfile.objects.filter(user=uid, event=event.id).prefetch_related()
    participants = User.objects.filter(rsvp__group= event)
    rsvp = RSVP.objects.filter(group= event, reply="Y").prefetch_related(
       Prefetch('person', queryset=User.objects.order_by('firstname')))
    locations =Location.objects.filter(event= event)
    total=0
    needreply = True
    for rsv in rsvp:
        if rsv.person.id == user.id:
            needreply = False
        total+= rsv.number_of_guests

    return render(request, 'rsvp.html', {'event': event, 'activities':activities,'foods':foods,
        'p': 'Rsvp',
        'needreply': needreply,
        'total': total, 'locations': locations, 'rsvp':rsvp, 'participants':participants,
        'profiles': profiles, 'user':user})

"""
def db(request):
    greeting = Event()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')
"""

