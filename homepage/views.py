from django.shortcuts import render
from .models import Booking
from .forms import BookingForm



# Create your views here.
def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    return render(request, 'index.html')
