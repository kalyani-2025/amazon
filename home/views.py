from django.shortcuts import render


def home(request):

    nav_items = [
        "Today's Deals",
        "Coupons",
        "Hotel Booking",
        "Gift Cards",
        "Amazon Pay",
        "Browsing History",
        "Keep Shopping for",
        "Buy Again",
        "Prime",
        "Gift Ideas",
        "Fresh",
        "Grocery & Gourmet Foods"
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

    more_categories = [
        "Books",
        "Toys & Games",
        "Sports & Fitness",
        "Automotive",
        "Baby Products"
    ]

    programs = [
        "Gift Cards & Mobile Recharge",
        "Amazon Launchpad",
        "Amazon Business",
        "Handloom and Handicrafts"
    ]

    help_settings = [
        "Your Account",
        "Customer Service",
        "Sign in"
    ]

    return render(request, "home.html", {
        "nav_items": nav_items,
        "trending": trending,
        "digital": digital,
        "categories": categories,
        "more_categories": more_categories,
        "programs": programs,
        "help_settings": help_settings
    })