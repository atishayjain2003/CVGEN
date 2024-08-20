from django.shortcuts import render,redirect
from .models import Resume

def home(request):
    if request.method=='POST':
        data=request.POST
        FullName=data.get('name')
        PhoneNumber=data.get('phone')
        Location=data.get('location')
        Email=data.get('email')
        LinkedinURL=data.get('linkedin')
        LeetcodeURL=data.get('leetcode')
        GithubURL=data.get('github')
        Objective=data.get('objective')
        Education1=data.get('education1')
        Education2=data.get('education2')
        TechnicalSkills=data.get('technical-skills')
        SoftSkills=data.get('soft-skills')
        OtherSkills=data.get('other-skills')
        Experience1=data.get('experience1')
        Project1=data.get('project1')
        Project2=data.get('project2')
        
        ExtraActivties=data.get('activities')
        Leadership=data.get('leadership')

        Resume.objects.create(
            name=FullName, phone=PhoneNumber, location=Location, email=Email, linkedin=LinkedinURL,leetcode=LeetcodeURL, github=GithubURL,
            objective=Objective, education1=Education1, education2=Education2, technical_skills=TechnicalSkills, soft_skills=SoftSkills,
            other_skills=OtherSkills, experience1=Experience1, project1=Project1, project2=Project2,
            activities=ExtraActivties, leadership=Leadership
        )
       
        
    queryset=Resume.objects.all()
    context={'entry':queryset}
    return render(request, 'form.html', context)
    
   