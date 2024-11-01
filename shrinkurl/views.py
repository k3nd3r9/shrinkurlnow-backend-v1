from django.http import HttpResponse
from .models import URLPair
import hashlib

def insert_or_retrieve_url(request):
    if request.method == "POST":
        longurl = request.POST['longurl']
        shorturl = generate_short_hash(longurl)
        newUrlPair = URLPair.objects.create(long_url = longurl, short_url = shorturl)
        return HttpResponse(shorturl)
    #check if get request is empty before processing
    elif request.method == "GET" and 'q' in request.GET:
        q = request.GET['q']
        if q is not None and q != '':
            shorturl = request.GET['shorturl']
            foundURLPair = URLPair.objects.filter(short_url = shorturl).get()
            return HttpResponse(foundURLPair.long_url)

def generate_short_hash(data):
    #Generates a short hash from the given data.

    # Use SHA-256 for security
    hash_object = hashlib.sha256(data.encode())
    hex_digest = hash_object.hexdigest()

    # Take the first 6 characters for a short hash
    return hex_digest[:6]