from django.shortcuts import render


def home(request):

    nav_items = [
        "Fresh",
        "Prime Video",
        "Sell",
        "Bestsellers",
        "Today's Deals",
        "Mobiles",
        "New Releases",
        "Customer Service",
        "Prime",
        "Electronics",
        "Amazon Pay"
    ]

    trending = [
        "Bestsellers",
        "New Releases"
    ]

    digital = [
        "Echo & Alexa",
        "Fire TV",
        "Kindle E-Readers & eBooks",
        "Audible Audiobooks",
        "Amazon Prime Video",
        "Amazon Music"
    ]

    categories = [
        "Mobiles, Computers",
        "TV, Appliances, Electronics",
        "Men's Fashion",
        "Women's Fashion",
        "Home, Kitchen, Pets",
        "Beauty, Health, Grocery"
    ]

    programs = [
        "Gift Cards",
        "Amazon Launchpad",
        "Amazon Business",
        "Handloom and Handicrafts"
    ]

    help_settings = [
        "Your Account",
        "Customer Service",
        "Sign in"
    ]

    return render(request, 'home.html', {
        'nav_items': nav_items,
        'trending': trending,
        'digital': digital,
        'categories': categories,
        'programs': programs,
        'help_settings': help_settings
    })