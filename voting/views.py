from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vote
def home(request):
  return HttpResponse("hello world!")
def external(request):
    return render(request, 'external.html', {})
def vote(request):

    if request.method == "POST":

        voter_id = request.POST.get("voter_id")

        aadhaar_id = request.POST.get("aadhaar_id")

        candidate = request.POST.get("vote")


        # Check empty fields

        if not voter_id and not aadhaar_id:

            return render(request, "vote.html", {

                "error": "Enter Voter ID or Aadhaar ID"

            })


        # Check duplicate Voter ID

        if voter_id:

            if Vote.objects.filter(voter_id=voter_id).exists():

                return render(request, "vote.html", {

                    "error": "This Voter ID has already voted"

                })


        # Check duplicate Aadhaar ID

        if aadhaar_id:

            if Vote.objects.filter(aadhaar_id=aadhaar_id).exists():

                return render(request, "vote.html", {

                    "alert": "This Aadhaar ID has already voted"

                })


        # Save Vote

        Vote.objects.create(

            voter_id=voter_id,

            aadhaar_id=aadhaar_id,

            candidate=candidate

        )


        return redirect('s')


    return render(request, "vote.html")


    return render(request, "vote.html")

def s(request):
    return render(request, 's.html')
def c(request):
    return render(request, 'c.html')