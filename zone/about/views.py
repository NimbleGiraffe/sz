from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    if request.user.is_authenticated():
        signed_in = True
    else:
        signed_in = False
    return render_to_response("home.html", {'signed_in':signed_in}, context_instance=RequestContext(request))