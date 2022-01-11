 
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm ,HoodForm, BusinessForm, PostForm 
from django.http  import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
    return render(request,'index.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    # project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile})    

def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})     

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():      
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    
    return render(request, 'update_profile.html',{"form":form})   



    
@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():

            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        
        return HttpResponseRedirect('/profile')

    else:
        hood_form = HoodForm()


    context = {'hood_form':hood_form}
    return render(request, 'hood/create_hood.html',context)

@login_required(login_url="/accounts/login/")
def hoods(request):
    current_user = request.user
    hoods = NeighborHood.objects.all().order_by('-id')

    context ={'hoods':hoods}
    return render(request, 'hood/hood.html', context) 

@login_required(login_url='/accounts/login/')
def single_hood(request,name):
    hood = NeighborHood.objects.get(name=name)
    
    return render(request,'single_hood.html',{'hood':hood})    

def join_hood(request,id):
    neighborhood = get_object_or_404(NeighborHood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')       

@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
           
            business.save()

        return HttpResponseRedirect('/businesses')
    else:

        form=BusinessForm()

    return render (request,'create_business.html', {'form': form, 'profile': profile})




@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    businesses = Business.objects.all().order_by('-id')
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighborhood = NeighborHood.objects.all()
        
        businesses = Business.objects.all().order_by('-id')
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "business.html", {"businesses": businesses})
      

@login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.hood = hood
            post.user=current_user
            post.save()
            return redirect('/post')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.filter(user_id=current_user.id)
        
        locations = Location.objects.all()
        neighborhood = NeighborHood.objects.all()
        
        businesses = Business.objects.filter(user_id=current_user.id)
        
        return render(request, "profile.html", {"danger": "Update Profile ", "locations": locations, "neighborhood": neighborhood,  "businesses": businesses,"posts": posts})
    else:
        neighborhood = profile.neighborhood
        posts = Post.objects.filter(user_id=current_user.id)
        return render(request, "posts.html", {"posts": posts})    

@login_required(login_url="/accounts/login/")
def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_hood = NeighborHood.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "search.html", {"message": message, "hood": searched_hood})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})        