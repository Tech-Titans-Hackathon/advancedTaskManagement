from django.shortcuts import render

# Create your views here.
def HomeView(request, *args, **kwargs):
    context = {
        "days": range(1, 32),
        "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "years": range(2021, 2031),
        "current_year": 2021,
        "current_month": 1,
        "current_day": 1,
        "username":"Shaan"
    }
    return render(request, 'dashboard/home.html', context)