import tkinter
from tkinter import*
import json
import random
# for displaying Questions & Options
global questions
global answer_choice,answers
with open('quiz.json', encoding="utf8") as f:
    data = json.load(f) 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,0,2,0,3,2,0,0,3,1,1,3,0,2,2,0,2,0,3,1]
# for Login & registration of username and password
global user
with open('info.json',) as json_file:
    users = json.load(json_file)
user_answer = []
MCQ= []
def gen():
    global MCQ
    while(len(MCQ) < 10):
        x = random.randint(0,19)
        if x in MCQ:
            continue
        else:
            MCQ.append(x)

    

def Checkbutton_Is_pressed():
    global MCQ
    global root,Checkbutton
    global Correctlabeltext
    global root
    correct_ans=tkinter.Tk()    
    correct_ans.title("Correct Answers")
    correct_ans.geometry("700x600")
    correct_ans.config(background="Salmon")
    t={0: "Which is the only planet not named after Greek gods or goddesses? - b)Earth",
       1 :"Which planet has supersonic winds - a)Neptune",
       2 :"Which is the oldest planet in the solar planet - c)Jupiter",
       3 :"Which planet rotates on its side - a)Uranus",
       4 :"What is the name of the largest moon of Jupiter - d)Ganymede",
       5:"Which planet is known as the Morning star - c)Venus",
       6:"Which star is the Alpha Usra Minoris- a)Polaris",
       7:"Who was the third astronaut to walk on the moon- a)Charles P.Coronad",
       8:"How many stars make up the Big dipper - d)8",
       9:"Vesta is which type of celestial body - b)Asteroid",
       10:"What is a highly magnetized rotating neuron star - a)Pulsar",
       11:"How many constellations are there - d)88",
       12:"Where is the coldest place in the universe - a) Boomerang Nebula",
       13:"What are the largest stars in the universe - c)Red Gaint",
       14:"How many moons are there in the solar system - c)200",
       15:"Uranus has been only been visited by what spacecraft - a)Voyager 2",
       16:"How long is one day on venus - c)116 days on earth",
       17:"Which is the biggest volcano on Mars - a) Olympus Mons",
       18:"Which is the first artificial satellite - d)Sputnik",
       19: "Who was the first man to enter space - b)Yuri Gagarin"
       }
    a=[]
    for i in range(len(MCQ)):
        for k in t:
            if MCQ[i]==k:
                Correctlabeltext=Label(correct_ans,text=t[k],background="snow",width="80",).pack(pady=(10,10)) 
        
def showresult(score):
    global lblQuestion,r1,r2,r3,r4 
    global root
    global labelresulttext,Checkbutton
    global Total_score
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    Total_score=StringVar()
    Total_score=score
    labelresulttext = Label(
        root,font = ("Bell MT",20),
        background = "light yellow",width="40",
        height="3",
        wraplength=400,)
    
    labelresulttext.pack(pady=(20,0))
    
    labelscore=Label(root,text=Total_score,font=("Bell MT",20),width="40",height="3",background="light yellow",).pack()                        
    if score >= 40:
        labelresulttext.configure(text="You Are Excellent!!\nYour score is")
    elif (score >= 25 and score < 40):
        labelresulttext.configure(text="You Can Be Better !!\nYour score is")
    else:
        labelresulttext.configure(text="You Should Work Hard !!\nYour score is")
    Checkbutton=Button(root,text="Correct \nAnswer",background="gold",activebackground="green2",width="8",height="4",command=Checkbutton_Is_pressed,).pack(pady=(20,2))
                
def calc():
    global MCQ,user_answer,answers
    global Total_score
    x = 0
    score=0
    for i in MCQ:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    showresult(score)
    Total_score=StringVar()
    Total_score=score
ques=1                
def selected():
    global radiovar,user_answer,MCQ
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[MCQ[ques]])
        r1['text'] = answers_choice[MCQ[ques]][0]
        r2['text'] = answers_choice[MCQ[ques]][1]
        r3['text'] = answers_choice[MCQ[ques]][2]
        r4['text'] = answers_choice[MCQ[ques]][3]
        ques += 1
    else:
        calc()

def startquiz():
    global root
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[MCQ[0]],
        font = ("Consolas", 16),
        width = "500",
        justify = "center",
        wraplength = "400",
        background = "snow",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[MCQ[0]][0],
        font = ("Times", 12),
        value = 0,
        width="20",
        variable = radiovar,
        command = selected,
        background = "IndianRed1",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[MCQ[0]][1],
        font = ("Times", 12),
        value = 1,
        width="20",
        variable = radiovar,
        command = selected,
        background = "green2",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[MCQ[0]][2],
        font = ("Times", 12),
        value = 2,
        width="20",
        variable = radiovar,
        command = selected,
        background = "DarkOrchid1",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[MCQ[0]][3],
        font = ("Times", 12),
        value = 3,
        width="20",
        variable = radiovar,
        command = selected,
        background = "yellow",
    )
    r4.pack(pady=5)

def startIspressed():
    global root
    global labeltext,canvas,img,btnStart,lblInstruction,lblRules
    labeltext.destroy()
    canvas.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()
 
def main_screenQuiz():
    main_screen.destroy()
    global root
    root=tkinter.Tk()    
    root.title("Quizz")
    root.geometry("700x600")
    root.config(background="cyan")
    root.resizable(0,0)
    global labeltext,canvas,img,btnStart,lblInstruction,lblRules
    labeltext = Label(
        root,
        text = "Quizz",
        font = ("Comic sans MS",45,"bold"),
        background = "cyan",
        )
    labeltext.pack(pady=(0,30))
    canvas=Canvas(root,width=310,height=190)
    canvas.pack()
    img= PhotoImage(file="C:/Quiz.gif")
    canvas.create_image(20,20,anchor=NW,image=img,) 
    
    btnStart = Button(
        root,
        text="Start >>",
        font=("Algerian Regular",10),
        command = startIspressed,
        background="gold",height="2",)
    btnStart.pack(pady=(2,2))

    lblInstruction = Label(
        root,
        text = "Rules",
        background = "snow",
        font = ("Consolas",14),
        justify = "center",
        )
    lblInstruction.pack(pady=(10,1))

    lblRules = Label(
        root,
        text = "This quiz contains 10 questions\nYou cannot recorrect the question you answered before\nhence think before you select\n You will get +5 for each correct answers",
        width = "100",
        font = ("Times",12),
        background = "lavender",
        foreground = "Navy",
        )                                 
    lblRules.pack()
    root.mainloop()
def login():
    global login_screen 
    login_screen=Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.config(background="LightSkyBlue1")
    Label(login_screen,text="Please enter details below to login",font=("Bell MT",12),bg="light salmon",width="35",height="2",).pack()
    global username_verify
    global password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    Label(login_screen, text="Username",background="LightSkyBlue1",).pack()
    username_login_entry=Entry(login_screen,textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="Password",background="LightSkyBlue1",).pack()
    password_login_entry=Entry(login_screen,textvariable=password_verify,show="*",).pack()
    Button(login_screen,text="Login",activebackground="green2",width="10",height="1",command=loginIspressed,).pack(pady=(5,2))
def loginIspressed():
    global login_screen
    global user
    username1=username_verify.get()
    password1=password_verify.get()
    if password1 in users and users[password1]==username1:
        Label(login_screen,text="Successfully logged in,\n Click on Let's Go to start the quiz",fg="blue2",).pack()
        Button(login_screen,text="Let's Go",background="yellow",width="6",height="2",command=main_screenQuiz,).pack()
    else: 
        Label(login_screen,text="User doesn't exist or wrong password").pack()
def register():
    global username
    global password
    global username_entry
    global password_entry
    global register_screen
    register_screen=Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.config(background="LightSkyBlue1")
    username=StringVar()
    password=StringVar()
    Label(register_screen,text="Please enter details below",font=("Bell MT",12),bg="light salmon",width="35",height="2",).pack(pady=(1,1))
    username_lable=Label(register_screen,text="Username * ",background="LightSkyBlue1",)
    username_lable.pack()
    username_entry=Entry(register_screen,textvariable=username,).pack()
    password_lable=Label(register_screen,text="Password * ",background="LightSkyBlue1",)
    password_lable.pack()
    password_entry=Entry(register_screen,textvariable=password,show="*",).pack()
    Button(register_screen,text="Register",activebackground="green2",width="10",height="1",command=registerIspressed,).pack(pady=(4,2))
def registerIspressed():
    global register_screen
    global user
    username_info=username.get()
    password_info=password.get()
    for i in range (1):
       if password_info not in users:
           users[password_info]=username_info
           with open("user.json","w") as fp:
               json.dump(users,fp)
           Label(register_screen,text="Registration success",fg="blue2",).pack()
           Button(register_screen,text="Let's Go",activebackground="green2",background="yellow",width="6",height="2",command=main_screenQuiz,).pack()
       else:
           Label(register_screen,text="Sorry the password you have\n entered is already in use\nSo, please enter anoter password",).pack()
def main_account_screen():
    global main_screen
    main_screen = tkinter.Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    main_screen.config(background="cornflower blue")
    Label(text="Choose Login Or Register",font=("Bell MT",12),bg="light salmon",width="35",height="2",).pack()
    LButton=Button(text="Login",activebackground="green2", height="2", width="25",command=login,).pack(pady=(10,2))
    RButton=Button(text="Register",activebackground="green2", height="2", width="25",command=register,).pack()
    main_screen.mainloop()
main_account_screen()
