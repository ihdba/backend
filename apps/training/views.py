from django.shortcuts import render, redirect

from .models import Exercise
from .forms import ExerciseForm


def training(request):

    exercises = Exercise.objects.all()


    context = {
        'title': 'Training',
        'exercises': exercises,
    }


    return render(request, 'training/training.html', context=context)



    

def add_training(request):  
    if request.method == "POST":  
        form = ExerciseForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('training')  
            except:  
                pass  
    else:  
        form = ExerciseForm()  
    return render(request,'training/add_training.html',{'form':form})  



def edit_training(request, id):  
    exercise = Exercise.objects.get(id=id)
    form = ExerciseForm(initial={'session': exercise.session, 'exercise': exercise.exercise, 'note': exercise.note})
    if request.method == "POST":  
        form = ExerciseForm(request.POST, instance=exercise)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('training')  
            except Exception as e: 
                pass    
    return render(request,'training/edit_training.html',{'form':form}) 