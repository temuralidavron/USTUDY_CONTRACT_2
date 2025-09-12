from django import template

register = template.Library()

UZBEK_MONTHS = {
    "January": "Yanvar",
    "February": "Fevral",
    "March": "Mart",
    "April": "Aprel",
    "May": "May",
    "June": "Iyun",
    "July": "Iyul",
    "August": "Avgust",
    "September": "Sentabr",
    "October": "Oktabr",
    "November": "Noyabr",
    "December": "Dekabr",
}

@register.filter
def get_item(month_name):
    """Oy nomini uzbekchaga o‘giradi"""
    return UZBEK_MONTHS.get(month_name, month_name)
