from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render


def home(request):

    return render(request , 'home.html')
def random_p(request):

    return render(request , 'random_picker.html')


def random_done(request):
    optionss = request.GET.get('options')
    options_list = optionss.split(",")

    print(options_list)
    choice = random.choice(options_list)
    print(choice)
    context = {'choicep': choice}




    return render(request,'random_picker.html',context)


# stone paper
def stone_paper(request):


    game_op = {'opt': list}

    return render(request, 'stone_paper game.html' , game_op)

def gamer_choice(request):
    choices = int(request.GET.get("choice"))-1
    print(choices)
    computer = random.choice(range(0,3))
    print(computer)
    list = ['  Stone 🗿  ', '  Paper 📄  ', 'Sccissor ✂️', ' Thread 🧵 ']
    string =''
    if choices==0:

        if computer == 1 :
            string = 'computer choose paper you loss'
        elif computer ==2 :
            string ='computer choose sccissor you win '
        elif computer == 3:
            string = 'computer choose thread you win '

        else :
            string = 'opps computer also choose stone '

    if choices == 1:

        if computer == 0:
            string = 'computer choose stone you win'

        elif computer == 2:
            string = 'computer choose sccissor you loss '
        elif computer == 3:
            string = 'computer choose thread you loss '


        else:
            string = 'opps computer also choose paper '

    if choices == 2:

        if computer == 0:
            string = 'computer choose stone you loss'
        elif computer == 1:
            string = 'computer choose paper you win'


        elif computer == 3:
            string = 'computer choose thread you win '


        else:
            string = 'opps computer also choose sccissor '
    if choices == 3:

        if computer == 0:
            string = 'computer choose stone you win'
        elif computer == 1:
            string = 'computer choose paper you win'


        elif computer == 2:
            string = 'computer choose thread you loss '


        else:
            string = 'opps computer also choose thread '

    cont = {'result': string}








    return render(request,'stone_paper game.html',cont)

def love_calculator (request):
    return render(request,'love-calculator.html')



