import os
from django.conf import settings

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        return uri  # leave unchanged

    if not os.path.isfile(path):
        raise Exception(f"Media URI must start with {settings.MEDIA_URL} or {settings.STATIC_URL}")
    return path



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
