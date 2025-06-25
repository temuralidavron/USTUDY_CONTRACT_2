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
def uzbek_month(date_obj):
    return UZBEK_MONTHS.get(date_obj.strftime("%B"), date_obj.strftime("%B"))
