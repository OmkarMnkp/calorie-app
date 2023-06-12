
#CREATED BY OMKAR MANKAPE

#importing libraries

from tkinter import *
from tkinter import messagebox as tmsg
from ttkbootstrap import *
from ttkbootstrap.constants import*
import matplotlib.pyplot as plt 
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

#frame window
root= Window(themename="superhero")
root.geometry("520x420")
root.title("BEFIT")

#creating notebook
notebook = ttk.Notebook(root)

#frames
frame1 = Frame(notebook)#turquoise  khaki  sienna2  orchid3
frame2 = Frame(notebook)
frame3 = Frame(notebook)
frame4 = Frame(notebook)
frame5 = Frame(notebook)
frame6 = Frame(notebook)
frame7 = Frame(notebook)
frame8 = Frame(notebook)

#packing the frames
frame1.pack(fill="both",expand=1)
frame2.pack(fill="both",expand=1)
frame3.pack(fill="both",expand=1)
frame4.pack(fill="both",expand=1)
frame5.pack(fill="both",expand=1)
frame6.pack(fill="both",expand=1)
frame7.pack(fill="both",expand=1)
frame8.pack(fill="both",expand=1)

#adding frames to the notebook
notebook.add(frame1,text="")
notebook.add(frame2,text="")
notebook.add(frame3,text="")
notebook.add(frame4,text="")
notebook.add(frame5,text="")
notebook.add(frame6,text="")
notebook.add(frame7,text="")
notebook.add(frame8,text="")

notebook.pack(expand=True,fill="both")

                
#creating a function for each frames
def show_frame1():
        notebook.select(frame1)

def show_frame2():
        notebook.select(frame2)

def show_frame3():
        notebook.select(frame3)

def show_frame4():
        notebook.select(frame4)

def show_frame5():
        notebook.select(frame5)

def show_frame6():
        notebook.select(frame6)

def show_frame7():
        notebook.select(frame7)

def show_frame8():
        notebook.select(frame8)

#creating front and back buttons in each frame

Button_f = Button(frame8,text="NEXT",command=show_frame1,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame8,text="BACK",command=show_frame7,bootstyle = "info outline").place(x=200,y=350)



#FRAME 1 

#main label
label = ttk.Label(frame1,text="PERSONAL INFO",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=1,padx=10,pady=10)

label = Label(frame1,text="Let's start with some information",bootstyle ="default",font="comicsansms 11 bold",padding=5).place(x=3,y=45)

#adding the image
image1 = PhotoImage(file="personal-information (1).png")
label1 = Label(frame1,image=image1)
label1.place(x=330,y=60)

#showing main bmi info
def info ():
    tmsg.showinfo("info","bmi < 18.5 --->(UNDERWEIGHT)\n bmi > 18.5 and bmi < 24.5 ---> (NORMAL)\n bmi>24.5 ---> (OVERWEIGHT)")

#function for calculating the bmi
def calculate_bmi():
    weight = float(weight_v.get())
    height = float(height_v.get()) / 100
    bmi = weight / (height**2)
    bmi_label.config(text="BMI: {:.2f}".format(bmi))

weight_v = StringVar()
height_v = StringVar()

name_label = ttk.Label(frame1, text=" NAME",bootstyle="default").place(x=18,y=85)
name_entry = ttk.Entry(frame1).place(x=100,y=80)

age_label = ttk.Label(frame1, text="AGE",bootstyle="default").place(x=18,y=125)
age_entry = ttk.Entry(frame1).place(x=100,y=120)

height_label = ttk.Label(frame1, text=" HEIGHT (cm)",bootstyle="default").place(x=18,y=165)
height_entry = ttk.Entry(frame1,textvariable=height_v).place(x=100,y=160)

weight_label = ttk.Label(frame1, text=" WEIGHT (kg)",bootstyle="default").place(x=18,y=205)
weight_entry = ttk.Entry(frame1,textvariable=weight_v).place(x=100,y=200)

calculate_button = ttk.Button(frame1, text="CALCULATE", command=calculate_bmi,bootstyle="primary outline")
calculate_button.place(x=120,y=260)

info_button = ttk.Button(frame1,text="MORE INFO",command=info,bootstyle="primary outline")
info_button.place(x=230,y=260)

bmi_label = ttk.Label(frame1, text="BMI:", font=("Helvetica", 10),bootstyle="default")
bmi_label.place(x=18,y=300)

button_f = Button(frame1, text="NEXT", command=show_frame2,bootstyle = "info outline").place(x=260,y=350)
button_b = Button(frame1,text="BACK",command=show_frame8,bootstyle = "info outline").place(x=200,y=350)

#FRAME 2

label = ttk.Label(frame2,text="CALORIE BURN",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=1,padx=10,pady=10)

label = Label(frame2,text="Get your calorie burn per day value",bootstyle="default",font="comicsansms 11 bold",padding=5).place(x=3,y=45)

image2 = PhotoImage(file="calories (2).png")
label2 = Label(frame2, image=image2)
label2.place(x=330,y=40)

#function for calculating the calorie burn per day 
def cal_burn():
    target = int(target_v.get())
    days = int(days_v.get())
    burn = ((target*7700)/days)
    burn_label.config(text="BURN/DAY:{:.2f}".format(burn)) 

target_v = StringVar()
days_v = StringVar()

target_label = ttk.Label(frame2,text="TARGET:",bootstyle = "default").place(x=18,y=85)
target_entry = ttk.Entry(frame2,textvariable=target_v).place(x=100,y=80)

days_label = ttk.Label(frame2,text="DAYS:",bootstyle = "default").place(x=18,y=125)
days_entry = ttk.Entry(frame2,textvariable=days_v).place(x=100,y=120)

calculate_button = ttk.Button(frame2, text="CALCULATE", command=cal_burn,bootstyle="primary outline")
calculate_button.place(x=120,y=180)

burn_label = ttk.Label(frame2, text="BURN/DAY", font=("Helvetica", 9),bootstyle="default")
burn_label.place(x=20,y=230)

dietimg = PhotoImage(file="diet.png")
labeldiet = Label(frame2,image=dietimg)
labeldiet.place(x=7,y=310)

Button_f = Button(frame2,text="NEXT",command=show_frame3,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame2,text="BACK",command=show_frame1,bootstyle = "info outline").place(x=200,y=350)

#FRAME 3

label = ttk.Label(frame3,text="SELECT CATEGORY",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=0,padx=10,pady=10)
label = Label(frame3,text="Select category and get info",bootstyle="default",font="comicsansms 11 bold",padding=5).place(x=3,y=45)

image3 = PhotoImage(file="age-group.png")
label3 = Label(frame3, image=image3)
label3.place(x=330,y=40)

image20 = PhotoImage(file="playtime.png")
label20= Label(frame3, image=image20)
label20.place(x=40,y=230)

image21 = PhotoImage(file="teenage.png")
label21= Label(frame3, image=image21)
label21.place(x=120,y=230)

image22 = PhotoImage(file="man.png")
label22= Label(frame3, image=image22)
label22.place(x=200,y=230)

image23 = PhotoImage(file="grandmother.png")
label23= Label(frame3, image=image23)
label23.place(x=280,y=230)

#Showing the information using the (tmsg.showinfo)
def children():
    tmsg.showinfo("PRESCHOOL AGE CHILDREN ","active play through a variety of enjoyable physical activities")

def adolescent():
    tmsg.showinfo("CHILDREN AND ADOLESCENTS","60 min or moderate vigorous physical activity.\nactivity for strengthens muscles such as pushups .\n for strengthens bones such as gymnastics or skipping")

def adult():
    tmsg.showinfo("ADULTS","brisk walking at least 150 min a week.\nstrengthen muscles activities for at least 2 days a week")

def older():
    tmsg.showinfo("OLDER ADULTS","brisk walking at least 150 min a week.\nactivities to improve balance such as standing on one foot")

#using the radio button
var  =  StringVar()
var.set("radio")
radio = ttk.Radiobutton(frame3,text="Preschool Age Children (3--5 Years)",variable=var,value="1",command=children).place(x=18,y=90)
radio = ttk.Radiobutton(frame3,text="Children And Adolecents(6--17 Years)",variable=var,value="2",command=adolescent).place(x=18,y=120)
radio = ttk.Radiobutton(frame3,text="Adults (18--64 Years)",variable=var,value="3",command=adult).place(x=18,y=150)
radio = ttk.Radiobutton(frame3,text="Older Adults(65 Years and above )",variable=var,value="4",command=older).place(x=18,y=180)

Button_f = Button(frame3,text="NEXT",command=show_frame4,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame3,text="BACK",command=show_frame2,bootstyle = "info outline").place(x=200,y=350)

#FRAME 4

label = ttk.Label(frame4,text="CALORIE TRACK ",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=1,padx=10,pady=10)

label = Label(frame4,text="Enter consumed carbs,proteins,fats and get total intake",bootstyle="default",font="comicsansms 11 bold",padding=5).place(x=3,y=45)

image4 = PhotoImage(file="burn (1).png")
label4 = Label(frame4, image=image4)
label4.place(x=340,y=80)

def cal_cal():
        carbohydrates = float(carbs_v.get())
        proteins= float(proteins_v.get())
        fats = float(fats_v.get())
        #multiplying carbs by 4, proteins by 4 and fats by 9
        calories = (carbohydrates * 4) + (proteins * 4) + (fats *9)

        #using :.2f for rounding of the number
        calorie_label.config(text="CALORIE CONSUMED :{:.2f}".format(calories)) 

#using the textvariable Stringvar,intvar etc

carbs_v = StringVar()
proteins_v = StringVar()
fats_v = StringVar()

var.set(str)

carbs_l = Label(frame4,text="CARBOHYDRATES",bootstyle = "default").place(x=18,y=85)
carbs = Entry(frame4,width=14,textvariable=carbs_v).place(x=140,y=80)

proteins_l = Label(frame4,text="PROTEINS",bootstyle = "default").place(x=18,y=125)
proteins = Entry(frame4,width=14,textvariable=proteins_v).place(x=140,y=120)

fats_l = Label(frame4,text="FATS",bootstyle = "default").place(x=18,y=165)
fats  = Entry(frame4,width=14,textvariable=fats_v).place(x=140,y=160)

cal_button = ttk.Button(frame4,text="CALCULATE",command=cal_cal,bootstyle="primary outline")
cal_button.place(x=143,y=220)

calorie_label = ttk.Label(frame4,text="CALORIE CONSUMED" ,font=("Helvetica", 9),bootstyle="default")
calorie_label.place(x=20,y=270)

imagedatascience = PhotoImage(file="data-science.png")
labeldatascience = Label(frame4, image=imagedatascience)
labeldatascience.place(x=440,y=310)

Button_f = Button(frame4,text="NEXT",command=show_frame5,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame4,text="BACK",command=show_frame3,bootstyle = "info outline").place(x=200,y=350)


#FRAME 5


Label(frame5,text="MONITOR PROCESS",bootstyle = "default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=1,padx=10,pady=10)

label = Label(frame5,text="Get you progress in graph's",bootstyle="default",font="comicsansms 11 bold",padding=5).place(x=3,y=45)

image5 = PhotoImage(file="monitoring.png")
label5 = Label(frame5, image=image5)
label5.place(x=360,y=55)

def plot_graph():
    carb_value = float(carbs_v.get())
    fat_value = float(fats_v.get())
    protein_value = float(proteins_v.get())

    #creating a list of labels and values
    labels = ["carbohydrates","proteins","fats"]
    values = [carb_value,fat_value,protein_value]

    #using plt function to plot graph
    plt.pie( values,labels=labels, autopct='%1.1f%%', startangle=20)
    plt.show()

def subtract_and_plot():
    total = float(calorieintake_v.get())
    consumed = float(calorieconsumed_v.get())
    remaining = total - consumed

    labels = ['Consumed','Remaining']
    values = [consumed, remaining]

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.show()

# error function for wrong entries
def error():
     calorie_c = float(calorieconsumed_v.get())
     calorie_t = float(calorieintake_v.get())

     if calorie_c> calorie_t:
          tmsg.showerror("error","enter value correctly")
     else:
          tmsg.showinfo("correct","correct entries")
    
def nonnegative():
     calorie_c_n = float(calorieconsumed_v.get())
     calorie_t_n = float(calorieintake_v.get())

     if(calorie_c_n> calorie_t_n):
          tmsg.showerror("error","calorie consumed must be greater than calorie target")

calorieintake_v =StringVar()
calorieconsumed_v = StringVar()

calorie_consumed = ttk.Label(frame5,text="CALORIES CONSUMED",bootstyle ="default").place(x=18,y=85)
calorie_entry = ttk.Entry(frame5,textvariable=calorieconsumed_v).place(x=150,y=80)

calorie_intake = ttk.Label(frame5,text="CALORIES TARGET",bootstyle ="default").place(x=18,y=125)
calorie_entry = ttk.Entry(frame5,textvariable=calorieintake_v).place(x=150,y=120)

ttk.Label(frame5,text="CHECK",justify=LEFT).place(x=195,y=165)
check_button = Button(frame5,text="check",command=error ,bootstyle="primary outline")
check_button.place(x=190,y=190)

ttk.Label(frame5,text=" GRAPH ",justify=LEFT).place(x=130,y=235)
plot_button = Button(frame5, text="PLOT CALORIES ", command=plot_graph,bootstyle="primary outline")
plot_button.place(x=100,y=260)

ttk.Label(frame5,text=" TRACK PROGRESS",justify=LEFT).place(x=223,y=235)
subtract_button = Button(frame5, text="PLOT COMPARE ", command=subtract_and_plot ,bootstyle="primary outline")
subtract_button.place(x=220,y=260)

imagegraph = PhotoImage(file="graph.png")
labelgraph = Label(frame5, image=imagegraph)
labelgraph.place(x=7,y=310)

"adding the frame to the projects the available "
Button_f = Button(frame5,text="NEXT",command=show_frame6,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame5,text="BACK",command=show_frame4,bootstyle = "info outline").place(x=200,y=350)


#FRAME 6

#creating dictionaries for different exercises of kay values pair of info,video,label
pushups = {
    'info':  "\nStart with arms straight the body lifted in a straight line horizontal to the floor.\n Keep the feet together and the toes flexed to support the body.The palms \nshould be flat on the floor shoulder-width apart,with the fingers facing straight \nahead or slightly inward.slowly bend the elbows outward and lower the body\n down to the floor.Try to keep the hips and lower back in line." ,
    'video': 'https://www.youtube.com/watch?v=DsTgbEJ6ZT8',
    'label':"PUSH-UPS STEPS"
}

squats = {
    'info': 'Stand with the feet slightly wider than hip-width apart,\nangling the toes slightly outward.\nKeep the hands down by the sides,\nwith the palms facing in and keep the shoulders back. \nEngage the abdominal muscles to support the back.\nShift the hips back and bend the knees as though taking a seat,\nKeep lowering down to the ground until the thighs are parallel with the floor.\nPush through the feet to straighten back up into the starting position.',
    'video': 'https://www.youtube.com/watch?v=U3HJUIgK1Do',
    'label':"SQUATS STEPS"
}

lunges = {
    'info': "Lunges are a great exercise for strengthening the legs and glutes.\nStart in a plank position with the arms straight and the body lifted in a straight line\n horizontal to the floor. Keep the feet together and the toes flexed to support the body.\nThe palms should be flat on the f with the fingers facing straight ahead or slightly inward.\nKeeping the head in line wiloor shoulder-width apart,th the spine,\nslowly bend the elbows outward and lower the body down to the floor.\nUse the arm muscles to press the body back up into the starting position.\nKeep the abdominal muscles engaged throughout to help support the back.",
    'video': 'https://www.youtube.com/watch?v=U3HJUIgK1Do',
    'label':"LUNGES STEPS"
}

planks = {
    'info': 'Start with the elbows and lower arms on the floor,*\nkeeping the elbows in line with the shoulders.\n*Lift the body so that it forms a straight line horizontal to the floor.\n*Keep the feet together and the toes flexed to support the body.\n*Hold for 20–30 seconds.\n*Slowly lower to the floor and rest for 1 minute, then repeat 3 to 5 times..',
    'video': 'https://www.youtube.com/watch?v=U3HJUIgK1Do',
    'label':"PLANKS STEPS"
}

dumbbell ={
     'info':'Use an overhand grip, so that your knuckles are facing up \nand your palms are towards your body. \nYour elbows should be pressed along your sides so that the dumbbells\n are directly in front of your shoulders.[5]re not \nleaning back or hunching over.',
     'video':'https://youtu.be/WDNQk_vJ2xE',
     'label':'DUMBELL STEPS'
}

abs ={
     'info':'if youre just starting, its wise to take it slow.\nTry starting with 2 sets of 10 repetitions for each exercise \nthen gradually work your way up to 3 sets of 12 repsAvoid \nexercising or stretching if your muscles are sore.\n If you have a muscle strain, working out will make \nmatters worse.',
     'video':'https://youtu.be/jZhKPgjb0yg',
     'label':'ABS STEPS'
}

meditate={
     'info':'Sit up straight on your cushion or chair.\nRest your hands in a comfortable position,\nTilt your chin downward and close your eyesFocus on your breathing.\n',
     'video':'https://youtu.be/O-6f5wQXSu8',
     'label':'MEDITATE STEPS' 
}

bicycle = {
     'info':'',
     'video':'https://youtu.be/0MLnC3bzXgQ',
     'label':'BICYCLE STEPS'
}


#function for displaying exercises

def display_exercise(exercise):
    info = exercise['info']
    video = exercise['video']
    label = exercise['label']
    
    #creating a new window
    exercise_window= tb.Window(themename="superhero")
    exercise_window.geometry("520x370")

    info_label = tk.Label(exercise_window, text=info,font="comicsansms 10 bold")
    info_label.pack()

    video_link = tk.Label(exercise_window, text=video, fg='blue', cursor='hand2')
    video_link.pack()

    l_info = tk.Label(exercise_window,text=label,font="comicsansms 15 bold")
    l_info.pack(anchor=S)

    
    #opening the video linkusing webbrowser function
    def open_video_link(event):
        exercise_window.destroy()
        webbrowser.open(video)
        
    video_link.bind("<Button-1>", open_video_link)
 

lunge_button = Button(frame6, text="LUNGES",command=lambda: display_exercise(lunges),bootstyle="primary outline")
lunge_button.place(x=110,y=240)

squat_button = Button(frame6, text="SQUATS", command=lambda: display_exercise(squats),bootstyle="primary outline")
squat_button.place(x=110,y=170)

pushup_button = Button(frame6, text="PUSH-UPS", command=lambda: display_exercise(pushups),bootstyle="primary outline")
pushup_button.place(x=110,y=100)

plank_button = Button(frame6, text="PLANK", command=lambda: display_exercise(planks),bootstyle="primary outline")
plank_button.place(x=110,y=310)

bicycle_button = Button(frame6,text = "BICYCLE",command=lambda:display_exercise(bicycle),bootstyle = "primary outline")
bicycle_button.place(x= 385,y= 100)

dumbbell_button = Button(frame6,text="DUMBBELL",command= lambda:display_exercise(dumbbell),bootstyle ="primary outline" )
dumbbell_button.place(x=385,y=170)

meditate_button = Button(frame6,text="MEDITATE",command= lambda:display_exercise(meditate),bootstyle ="primary outline" )
meditate_button.place(x=385,y=240)

pullups_button = Button(frame6,text="ABS",command= lambda:display_exercise(abs),bootstyle ="primary outline" )
pullups_button.place(x=385,y=310)

label = ttk.Label(frame6,text=" LET'S EXERCISE ",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=3,padx=10,pady=10)
label = ttk.Label(frame6,text=" Exercises That Helps You To Stay Fit. ",bootstyle = "default",font="comicsansms 11 bold",padding=5).place(x=0,y=45)

image14 = PhotoImage(file="push-up.png")
label14 = Label(frame6, image=image14)
label14.place(x=20,y=80) 

image15 = PhotoImage(file="squat.png")
label15 = Label(frame6, image=image15)
label15.place(x=20,y=150)

image16 = PhotoImage(file="lunges.png")
label16 = Label(frame6, image=image16)
label16.place(x=20,y=220)

image17 = PhotoImage(file="plank.png")
label17 = Label(frame6, image=image17)
label17.place(x=20,y=290)

image24 = PhotoImage(file="exercises.png")
label24 = Label(frame6, image=image24)
label24.place(x=315,y=290) 

image25 = PhotoImage(file="yoga.png")
label25 = Label(frame6, image=image25)
label25.place(x=300,y=220) 

image26 = PhotoImage(file="dumbbell.png")
label26 = Label(frame6, image=image26)
label26.place(x=300,y=150) 

image27 = PhotoImage(file="bicycle.png")
label27 = Label(frame6, image=image27)
label27.place(x=300,y=80) 

Button_f = Button(frame6,text="NEXT",command=show_frame7,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame6,text="BACK",command=show_frame5,bootstyle = "info outline").place(x=200,y=350)


#FRAME 7

Label(frame7,text="TODAY'S REPORT",bootstyle="default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=2,padx=10,pady=10)

label = Label(frame7,text=" let's see your today's all over report.",bootstyle = "default",font="comicsansms 11 bold",padding=5).place(x=0,y=45)

imagesio = PhotoImage(file="seo-report.png")
labelsio = Label(frame7,image=imagesio)
labelsio.place(x=370,y=87)

def generate_report():
    name = name_v.get()
    age = age_v.get()
    bmi = bmi_v.get()
    consumed = consumed_v.get()
    target = target_ve.get()
    gender = gender_var.get()

    #creating a canvas
    report = canvas.Canvas("person_report.pdf", pagesize=letter)

    # Set the title of the document
    report.setTitle("Person Information Report")

    # Add the input data to the document
    #here (30,750) are coordinates of x and y axis
    report.drawString(30, 750, f"Name: {name}")
    report.drawString(30, 725, f"Age: {age}")
    report.drawString(30, 700, f"bmi: {bmi}")
    report.drawString(30, 675, f"consumed: {consumed}")
    report.drawString(30, 650, f"target: {target}")
    report.drawString(30, 625, f"gender: {gender}")

    # Save and close the PDF document
    report.save()

    # Show success message to user
    tmsg.showinfo("Report Generated", "The report has been generated successfully!")

def download_pdf():
    # Open the file explorer to select save location
    filename = os.path.abspath("person_report.pdf")
    os.startfile(filename)


image0 = PhotoImage(file="report.png")
label0 = Label(frame7, image=image0)
label0.place(x=445,y=310)

name_v = StringVar()
name_l = ttk.Label(frame7, text="NAME:",bootstyle="default").place(x=18,y=85)
name_e = ttk.Entry(frame7,textvariable=name_v).place(x=100,y=80)

age_v = StringVar()
age_l = Label(frame7,text="AGE:",bootstyle="default").place(x=18,y=120)
age_e = Entry(frame7,textvariable=age_v).place(x=100,y=115)

bmi_v =StringVar()
bmi_l = Label(frame7,text="BMI:",bootstyle="default").place(x=18,y=155)
bmi_e = Entry(frame7,textvariable=bmi_v).place(x=100,y=150)

consumed_v = StringVar()
consumed_l = Label(frame7,text="COUSUMED:",bootstyle="default").place(x=18,y=190)
consumed_e = Entry(frame7,textvariable=consumed_v).place(x=100,y=185)

target_ve = StringVar()
target_l = Label(frame7,text="TARGET:",bootstyle="default").place(x=18,y=225)
target_e = Entry(frame7,textvariable= target_ve).place(x=100,y=220)

gender_var = StringVar()
gender_var.set("Male")
Radiobutton(frame7, text="Male", variable=gender_var, value="Male").place(x=100,y=260)
Radiobutton(frame7, text="Female", variable=gender_var, value="Female").place(x=160,y=260)

submit_button = Button(frame7, text="Generate Report",bootstyle="primary outline" ,command=generate_report)
submit_button.place(x=100,y=295)

download_button = Button(frame7, text="Download PDF", bootstyle="primary outline",command=download_pdf)
download_button.place(x=250,y=295)

# i buttons for each frame

def showinfo1():
     tmsg.showinfo("PERSONAL INFO","user has to enter personal info name,age,height,weight \nand will get the bmi")

def showinfo2():
     tmsg.showinfo("CALORIE BURN","user has to enter targer weight , days and will \nget a calorie burn per day value")

def showinfo3():
     tmsg.showinfo("SELECT CATEGORY","user has to select the category ")

def showinfo4():
     tmsg.showinfo("CALORIE TRACK","user has to enter carbs,fats,proteins values \nand will total calorie intake value")

def showinfo5():
     tmsg.showinfo("MONITOR PROGRESS","user has to enter calorie consumed and calorie target \nand can view their progress in graphical format")

def showinfo6():
     tmsg.showinfo("LET'S EXERCISE","user has to select their desired exercise and will get \ninformation and can view youtube video")

def showinfo7():
     tmsg.showinfo("TODAY'S REPORT","user will get their today's report and can download it in the form of pdf")

ibtn = Button(frame1,text="I",bootstyle="primary outline",command=showinfo1).place(x=450,y=10)
ibtn = Button(frame2,text="I",bootstyle="primary outline",command=showinfo2).place(x=450,y=10)
ibtn = Button(frame3,text="I",bootstyle="primary outline",command=showinfo3).place(x=450,y=10)
ibtn = Button(frame4,text="I",bootstyle="primary outline",command=showinfo4).place(x=450,y=10)
ibtn = Button(frame5,text="I",bootstyle="primary outline",command=showinfo5).place(x=450,y=10)
ibtn = Button(frame6,text="I",bootstyle="primary outline",command=showinfo6).place(x=450,y=10)
ibtn = Button(frame7,text="I",bootstyle="primary outline",command=showinfo7).place(x=450,y=10)

Button_f = Button(frame7,text="NEXT",command=show_frame8,bootstyle="info outline").place(x=260,y=350)
button_b = Button(frame7,text="BACK",command=show_frame6,bootstyle = "info outline").place(x=200,y=350)


#FRAME 8

#function for opening apps using webbrowser.open_new
def open_instagram(event):
    import webbrowser
    webbrowser.open_new(r"https://www.instagram.com/")

def open_youtube(event):
    import webbrowser
    webbrowser.open_new(r"https://www.youtube.com/")

def open_twitter(event):
    import webbrowser
    webbrowser.open_new(r"https://twitter.com/")

def open_facebook(event):
    import webbrowser
    webbrowser.open_new(r"https://www.facebook.com/")

def open_whatsapp(event):
    import webbrowser
    webbrowser.open_new(r"https://www.whatsapp.com/")

Label(frame8,text="REACH US AT  ",bootstyle = "default,inverse",font="comicsansms 15 bold",padding=4).grid(row=0,column=2,padx=10,pady=10)

label = Label(frame8,text="You can support us on ",bootstyle = "default",font="comicsansms 11 bold",padding=5).place(x=0,y=45)

image12= PhotoImage(file="follow-us.png")
label12 = Label(frame8, image=image12)
label12.place(x=360,y=55)

image_insta = PhotoImage(file="instagram (1).png")
label_insta = Label(frame8, image=image_insta)
label_insta.place(x=30,y=80)

image_facebbok = PhotoImage(file="facebook (1).png")
label_facebbok= Label(frame8, image=image_facebbok)
label_facebbok.place(x=30,y=130)

image_twitter = PhotoImage(file="twitter.png")
label_twitter = Label(frame8, image=image_twitter)
label_twitter.place(x=30,y=180)

image_youtube = PhotoImage(file="youtube.png")
label_youtube = Label(frame8, image=image_youtube)
label_youtube.place(x=30,y=230)

image_whatsapp = PhotoImage(file="whatsapp (1).png")
label_whatsapp = Label(frame8, image=image_whatsapp)
label_whatsapp.place(x=30,y=280)

#creating links and binding them
instagram_link = tk.Label(frame8, text="INSTAGRAM", fg="blue", cursor="hand2",font=("Helvetica", 10))
instagram_link.place(x=80,y=85)
instagram_link.bind("<Button-1>", open_instagram)

facebook_link = tk.Label(frame8, text="FACEBOOK", fg="blue", cursor="hand2",font=("Helvetica", 10))
facebook_link.place(x=80,y=135)
facebook_link.bind("<Button-1>", open_facebook)

twitter_link = tk.Label(frame8, text="TWITTER", fg="blue", cursor="hand2",font=("Helvetica", 10))
twitter_link.place(x=80,y=185)
twitter_link.bind("<Button-1>", open_twitter)

youtube_link = tk.Label(frame8, text="YOUTUBE", fg="blue", cursor="hand2",font=("Helvetica", 10))
youtube_link.place(x=80,y=235)
youtube_link.bind("<Button-1>", open_youtube)

wathsapp_link = tk.Label(frame8, text="WHATSAPP", fg="blue", cursor="hand2",font=("Helvetica", 10))
wathsapp_link.place(x=80,y=285)
wathsapp_link.bind("<Button-1>", open_whatsapp)

image11 = PhotoImage(file="follow.png")
label11 = Label(frame8, image=image11)
label11.place(x=430,y=287)

root.mainloop()
