import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from tkinter import font as tkFont
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#from ApI import name_entry

class thanks:
    def show(self):
        login_win = tk.Toplevel()
        login_win.title("page 3")
        screen_width = login_win.winfo_screenwidth()
        screen_height = login_win.winfo_screenheight()
        login_win.geometry(f"{screen_width}x{screen_height}")
        login_win.resizable(True, True)

        def website():
           webbrowser.open_new("https://eci.gov.in/")
           print("mission sucessful")
        def exists():
            login_win.destroy()
            print("mission sucessful")

        try:
            self.bg_img = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/orange.jpg")
            self.bg_img_resized = ImageTk.PhotoImage(self.bg_img.resize((1640, 1000)))
            self.bg_label = Label(login_win, image=self.bg_img_resized)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_label.image = self.bg_img_resized
        except Exception as e:
            print("Background not loaded:", e)
      #  try:
          #  self.bg_imgt1 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/pleasure.jpg")
           # self.bg_img_resizedt1 = ImageTk.PhotoImage(self.bg_imgt1.resize((200,200)))
           # self.bg_label = Label(login_win, image=self.bg_img_resizedt1)
           # self.bg_label.place(x=600, y=0)
        #except Exception as e:
           # print("Background not loaded:", e)
        try:
            self.bg_imgt2 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/tick.jpg")
            self.bg_img_resizedt2 = ImageTk.PhotoImage(self.bg_imgt2.resize((150,150)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt2)
            self.bg_label.place(x=650, y=250)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt3 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/direction.jpg")
            self.bg_img_resizedt3 = ImageTk.PhotoImage(self.bg_imgt3.resize((65,65)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt3)
            self.bg_label.place(x=0, y=480)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt4 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/direction.jpg")
            self.bg_img_resizedt4 = ImageTk.PhotoImage(self.bg_imgt4.resize((65,65)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt4)
            self.bg_label.place(x=0, y=550)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt5 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/direction.jpg")
            self.bg_img_resizedt5 = ImageTk.PhotoImage(self.bg_imgt5.resize((65,65)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt5)
            self.bg_label.place(x=0, y=620)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt6 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/pahchan.jpg")
            self.bg_img_resizedt6 = ImageTk.PhotoImage(self.bg_imgt6.resize((200,200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt6)
            self.bg_label.place(x=0, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt7 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/state.jpg")
            self.bg_img_resizedt7 = ImageTk.PhotoImage(self.bg_imgt7.resize((200,200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt7)
            self.bg_label.place(x=200, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt8 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/download.jpg")
            self.bg_img_resizedt8 = ImageTk.PhotoImage(self.bg_imgt8.resize((200,200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt8)
            self.bg_label.place(x=400, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt9 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/president.jpg")
            self.bg_img_resizedt9 = ImageTk.PhotoImage(self.bg_imgt9.resize((320, 200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt9)
            self.bg_label.place(x=600, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt10 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/mainpersons.jpg")
            self.bg_img_resizedt10 = ImageTk.PhotoImage(self.bg_imgt10.resize((340, 200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt10)
            self.bg_label.place(x=920, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt11 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/election.jpg")
            self.bg_img_resizedt11= ImageTk.PhotoImage(self.bg_imgt11.resize((300, 200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt11)
            self.bg_label.place(x=1250, y=0)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt12 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/women.jpg")
            self.bg_img_resizedt12 = ImageTk.PhotoImage(self.bg_imgt12.resize((550, 200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt12)
            self.bg_label.place(x=10, y=240)
        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.bg_imgt13 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/men.jpg")
            self.bg_img_resizedt13 = ImageTk.PhotoImage(self.bg_imgt13.resize((550, 200)))
            self.bg_label = Label(login_win, image=self.bg_img_resizedt13)
            self.bg_label.place(x=900, y=240)
        except Exception as e:
            print("Background not loaded:", e)
        Label(login_win, text="your valuable vote are submit under the election commission of India", fg="black", font=("Helvetica",33)).place(x=80,y=480)
        Label(login_win, text="Result Notification will come on your E-mail Adress by the Department", fg="black",font=("Helvetica", 33)).place(x=80, y=550)
        Label(login_win, text="official website of election commission of india visited them happily", fg="black",font=("Helvetica", 33)).place(x=80, y=620)
        Label(login_win, text="  "+"Made by: Naman singhal\n position:Undergraduate\nCourse:BCA\ncollege:Mukund lal national college\nuniversity:kurushtera university ", fg="black", font=("Helvetica",13)).place(x=1150, y=680)

        # button wisit website()
        custom_font = tkFont.Font(family="Arial", size=15, weight="bold", slant="roman")
        Thanks = tk.Button(login_win, text="Click FOR website", font=custom_font, fg="black", borderwidth=12,bg="#4CAF50", cursor="hand2", command=website).place(x=560, y=700)
        # exit button
        exits = tk.Button(login_win, text="Click For Exit", font=custom_font, fg="black", borderwidth=12, bg="#4CAF50",cursor="hand2", command=exists).place(x=800, y=700)

        login_win.mainloop()

class voting:
    def page(self,political_party):
        import mysql.connector as m
        db = m.connect(host="localhost", user="sensative_information", password="sensative_information", database="voting")
        mycursor=db.cursor()
        pattern='%'+political_party[-1]
        query = f"UPDATE voting_count SET votes = votes + 1 WHERE party_name LIKE '{pattern}'"
        mycursor.execute(query)
        db.commit()
        db.close()
        print("vote sucessfully store in database")
        #print("total vote of bjp",count_bjp)
        #print("total vote of congress",count_congress)
       # messagebox.showinfo("completing","your vote are submitted \n thanks for giving your \n valueable vote to your candidate")
        thank()
        login_win.destroy()

    def page3(self):
        global login_win
        login_win = tk.Toplevel(reg_win)
        login_win.title("page 3")
        screen_width = login_win.winfo_screenwidth()
        screen_height = login_win.winfo_screenheight()
        login_win.geometry(f"{screen_width}x{screen_height}")
        login_win.resizable(True, True)

        try:
            self.bg_img = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/darkyellow.jpg")
            self.bg_img_resized = ImageTk.PhotoImage(self.bg_img.resize((1640, 1000)))
            self.bg_label = Label(login_win, image=self.bg_img_resized)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_label.image = self.bg_img_resized
        except Exception as e:
            print("Background not loaded:", e)
        try:
         self.lockimg1r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/welcome1.jpg")
         self.resized_lock1r = self.lockimg1r.resize((350, 70))
         self.lock_photo1r = ImageTk.PhotoImage(self.resized_lock1r)
         self.img_label = Label(login_win, image=self.lock_photo1r)
         self.img_label.image = self.lock_photo1r  # gola
         self.img_label.place(x=580, y=0)

        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.lockimg2r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/congress.jpg")
            self.resized_lock2r = self.lockimg2r.resize((200,200))
            self.lock_photo2r = ImageTk.PhotoImage(self.resized_lock2r)
            self.img_label = Label(login_win, image=self.lock_photo2r)
            self.img_label.image = self.lock_photo2r  # gola
            self.img_label.place(x=60, y=100)

        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.lockimg3r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/bjp.jpg")
            self.resized_lock3r = self.lockimg3r.resize((200, 200))
            self.lock_photo3r = ImageTk.PhotoImage(self.resized_lock3r)
            self.img_label = Label(login_win, image=self.lock_photo3r)
            self.img_label.image = self.lock_photo3r  # gola
            self.img_label.place(x=370,y=100)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg4r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/bahujan.jpg")
            self.resized_lock4r = self.lockimg4r.resize((200, 200))
            self.lock_photo4r = ImageTk.PhotoImage(self.resized_lock4r)
            self.img_label = Label(login_win, image=self.lock_photo4r)
            self.img_label.image = self.lock_photo4r  # gola
            self.img_label.place(x=670, y=100)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg5r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/samajvadi.jpg")
            self.resized_lock5r = self.lockimg5r.resize((200, 200))
            self.lock_photo5r = ImageTk.PhotoImage(self.resized_lock5r)
            self.img_label = Label(login_win, image=self.lock_photo5r)
            self.img_label.image = self.lock_photo5r  # gola
            self.img_label.place(x=970, y=100)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg6r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/aam.jpg")
            self.resized_lock6r = self.lockimg6r.resize((200, 200))
            self.lock_photo6r = ImageTk.PhotoImage(self.resized_lock6r)
            self.img_label = Label(login_win, image=self.lock_photo6r)
            self.img_label.image = self.lock_photo6r  # gola
            self.img_label.place(x=1270, y=100)

        except Exception as e:
            print("Background not loaded:", e)
        try:
            self.lockimg7r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/mamta.jpg")
            self.resized_lock7r = self.lockimg7r.resize((200, 200))
            self.lock_photo7r = ImageTk.PhotoImage(self.resized_lock7r)
            self.img_label = Label(login_win, image=self.lock_photo7r)
            self.img_label.image = self.lock_photo7r  # gola
            self.img_label.place(x=60, y=420)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg8r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/shivsena.jpg")
            self.resized_lock8r = self.lockimg8r.resize((200, 200))
            self.lock_photo8r = ImageTk.PhotoImage(self.resized_lock8r)
            self.img_label = Label(login_win, image=self.lock_photo8r)
            self.img_label.image = self.lock_photo8r  # gola
            self.img_label.place(x=360, y=420)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg9r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/communist.jpg")
            self.resized_lock9r = self.lockimg9r.resize((200, 200))
            self.lock_photo9r = ImageTk.PhotoImage(self.resized_lock9r)
            self.img_label = Label(login_win, image=self.lock_photo9r)
            self.img_label.image = self.lock_photo9r  # gola
            self.img_label.place(x=660, y=420)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg10r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/arrow.jpg")
            self.resized_lock10r = self.lockimg10r.resize((200, 200))
            self.lock_photo10r = ImageTk.PhotoImage(self.resized_lock10r)
            self.img_label = Label(login_win, image=self.lock_photo10r)
            self.img_label.image = self.lock_photo10r  # gola
            self.img_label.place(x=960, y=420)

        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg11r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/rld.jpg")
            self.resized_lock11r = self.lockimg11r.resize((200, 200))
            self.lock_photo11r = ImageTk.PhotoImage(self.resized_lock11r)
            self.img_label = Label(login_win, image=self.lock_photo11r)
            self.img_label.image = self.lock_photo11r  # gola
            self.img_label.place(x=1260, y=420)

        except Exception as e:
            print("Background not loaded:", e)
        ############## bjp button #################
        Button(login_win, text="click for bjp", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=10, pady=5, bd=2,relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("bjp")).place(x=80, y=330)
        ############### congress button #################
        Button(login_win, text="click for congress", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2,relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("congress")).place(x=370, y=330)
        #################### bahujan button #########
        Button(login_win, text="click for bahujan", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8, pady=3,bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("bahujan")).place(x=685, y=330)
        ###################### samajvadi button ######
        Button(login_win, text="click for samajvadi", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("samajvadi")).place(x=970, y=330)
        ###################### aam admi party button ########
        Button(login_win, text="click for Aam admi", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("aam amdmi party")).place(x=1270, y=330)
        ###################### mamta west bengal party button ########
        Button(login_win, text="click for TMC", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("TMC")).place(x=80, y=650)
        ###################### shiv sena button ############
        Button(login_win, text="click for shiv sena", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("shiv sena")).place(x=365, y=650)
        ###################### cpi button ############
        Button(login_win, text="click for CPIM", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("CPIM")).place(x=685, y=650)
        ###################### arrow vala ka button ########
        Button(login_win, text="click for janta dal", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("shiv sena")).place(x=970, y=650)
        ###################### button of RLD ########
        Button(login_win, text="click for RLD", font=("Arial", 14, "bold"), bg="#f44336", fg="black", padx=8,pady=3, bd=2, relief=SOLID, activebackground="#45a049", cursor="hand2",command=lambda:self.page("RLD")).place(x=1285, y=650)
        ######################
        login_win.mainloop()

class StudentRegistrationApp:
    def __init__(self, master):
        self.master = master
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}")
        master.resizable(True, False)
        master.title("Candidate Registration")
        # Background
        try:
            self.bg_img = Image.open("C:/Users/hp/OneDrive/Desktop/blue.jpg")
            self.bg_img_resized = ImageTk.PhotoImage(self.bg_img.resize((1640,1000)))
            self.bg_label = Label(master, image=self.bg_img_resized)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_label.image=self.bg_img_resized
        except Exception as e:
            print("Background not loaded:", e)

        try:
            self.lockimg1r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/label.jpg")
            self.resized_lock1r = self.lockimg1r.resize((350,70))
            self.lock_photo1r = ImageTk.PhotoImage(self.resized_lock1r)
            self.img_label = Label(master, image=self.lock_photo1r)
            self.img_label.image = self.lock_photo1r # gola
            self.img_label.place(x=580, y=0)

        except Exception as e:
            print("image load Error !",e)

        try:
            self.lockimg2r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/cast.jpg")
            self.resized_lock2r = self.lockimg2r.resize((220,200))
            self.lock_photo2r = ImageTk.PhotoImage(self.resized_lock2r)
            self.img_label = Label(master, image=self.lock_photo2r)
            self.img_label.image = self.lock_photo2r  # gola
            self.img_label.place(x=0, y=90)
        except Exception as e:
            print("image load Error !", e)

        try:
            self.lockimg3r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/passport.jpg")
            self.resized_lock3r = self.lockimg3r.resize((220,200))
            self.lock_photo3r = ImageTk.PhotoImage(self.resized_lock3r)
            self.img_label = Label(master, image=self.lock_photo3r)
            self.img_label.place(x=200, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg4r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/tick.jpg")
            self.resized_lock4r = self.lockimg4r.resize((220,200))
            self.lock_photo4r = ImageTk.PhotoImage(self.resized_lock4r)
            self.img_label = Label(master, image=self.lock_photo4r)
            self.img_label.image = self.lock_photo4r  # gola
            self.img_label.place(x=400, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg5r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/member.jpg")
            self.resized_lock5r = self.lockimg5r.resize((250,200))
            self.lock_photo5r = ImageTk.PhotoImage(self.resized_lock5r)
            self.img_label = Label(master, image=self.lock_photo5r)
            self.img_label.image = self.lock_photo5r  # gola
            self.img_label.place(x=800, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg6r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/stamb.jpg")
            self.resized_lock6r = self.lockimg6r.resize((220,200))
            self.lock_photo6r = ImageTk.PhotoImage(self.resized_lock6r)
            self.img_label = Label(master, image=self.lock_photo6r)
            self.img_label.image =self.lock_photo6r  # gola
            self.img_label.place(x=600, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg7r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/register.jpg")
            self.resized_lock7r = self.lockimg7r.resize((220,200))
            self.lock_photo7r = ImageTk.PhotoImage(self.resized_lock7r)
            self.img_label = Label(master, image=self.lock_photo7r)
            self.img_label.image =self.lock_photo7r  # gola
            self.img_label.place(x=1050, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg8r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/helpline.jpg")
            self.resized_lock8r =self.lockimg8r.resize((260,200))
            self.lock_photo8r = ImageTk.PhotoImage(self.resized_lock8r)
            self.img_label = Label(master, image=self.lock_photo8r)
            self.img_label.image = self.lock_photo8r  # gola
            self.img_label.place(x=1265, y=90)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg9r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/calender.jpg")
            self.resized_lock9r = self.lockimg9r.resize((200, 200))
            self.lock_photo9r = ImageTk.PhotoImage(self.resized_lock9r)
            self.img_label = Label(master, image=self.lock_photo9r)
            self.img_label.image =self.lock_photo9r  # gola
            self.img_label.place(x=15, y=340)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg10r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/calender.jpg")
            self.resized_lock10r = self.lockimg10r.resize((200, 200))
            self.lock_photo10r = ImageTk.PhotoImage(self.resized_lock10r)
            self.img_label = Label(master, image=self.lock_photo10r)
            self.img_label.image =self.lock_photo10r  # gola
            self.img_label.place(x=1315, y=340)


        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg11r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/fill.jpg")
            self.resized_lock11r = self.lockimg11r.resize((60,60))
            self.lock_photo11r = ImageTk.PhotoImage(self.resized_lock11r)
            self.img_label = Label(master, image=self.lock_photo11r)
            self.img_label.image = self.lock_photo11r  # gola
            self.img_label.place(x=490, y=8)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg12r = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/identity.jpg")
            self.resized_lock12r = self.lockimg12r.resize((60, 60))
            self.lock_photo12r = ImageTk.PhotoImage(self.resized_lock12r)
            self.img_label = Label(master, image=self.lock_photo12r)
            self.img_label.image = self.lock_photo12r  # gola
            self.img_label.place(x=950, y=8)
        except Exception as e:
            print("image load Error !", e)
        try:
            self.lockimg13r = Image.open("C:/Users/hp/Downloads/Screenshot_2025-07-29-18-18-08-61_680d03679600f7af0b4c700c6b270fe7-removebg-preview.png")
            self.resized_lock13r = self.lockimg13r.resize((60, 60))
            self.lock_photo13r = ImageTk.PhotoImage(self.resized_lock13r)
            self.img_label = Label(master, image=self.lock_photo13r)
            self.img_label.image = self.lock_photo13r  # gola
            self.img_label.place(x=470, y=660)

        except Exception as e:
            print("image load error !",e)


        # frame 1
        Label(master,text="Name",font=("Arial", 18, "bold"),fg="black",bg="white",bd=2,relief=SOLID,padx=10, pady=5).place(x=300, y=320, anchor="center")
        # frame 2
        Label(master, text="Age", font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=890, y=300)
        # frame3
        Label(master, text="D-O-B",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=300, y=400, anchor="center")
        # frame4
        Label(master, text="Adhar-Number",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=875, y=400, anchor="center")
        # frame 5
        Label(master, text="sex",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=305, y=475, anchor="center")
        # frame 6
        Label(master, text="Country",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=905, y=475, anchor="center")
        # frame 7
        Label(master, text="District",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=290, y=560, anchor="center")
        # frame 8
        Label(master, text="Pin-Code",font=("Arial",18,"bold"), fg="black", bg="white",bd=2,relief=SOLID,padx=10,pady=5).place(x=900, y=560, anchor="center")
        # frame 9
        self.name_entry = Entry(master, font="10", bd=4,relief=SOLID)
        self.name_entry.place(x=400, y=300)
        # Entry2
        self.age = Entry(master, font="7", bd=4,relief=SOLID)
        self.age.place(x=1030, y=300)
        # Entry3
        self.dob_entry = Entry(master, font="10", bd=4,relief=SOLID)
        self.dob_entry.place(x=400, y=380)
        # Entry4
        self.adhar = Entry(master, font="10", bd=4,relief=SOLID)
        self.adhar.place(x=1030, y=380)

        # Entry5
        # Black border Frame (outer box)
        border_frame = Frame(master,bd=0,bg="black")
        border_frame.place(x=400, y=450, width=255, height=44) # combobox ka border black karna ka liya frame bananna pda
                                                                # beacuse relief function kam nahi karta combobox mai
        # Combobox inside the border frame
        self.sex_combo = Combobox(border_frame,values=["Male", "Female", "Other"],font=("Arial", 15, "bold"), state="readonly") # read only sa khali select karenga type nhi kar payenga
        self.sex_combo.place(x=2, y=2, width=250, height=40)
        # Entry 6
        self.country = Entry(master, font="10", bd=4,relief=SOLID)
        self.country.place(x=1030, y=457)
        # Entry 7
        self.district = Entry(master, font="10", bd=4,relief=SOLID)
        self.district.place(x=400, y=540)
        # Entry 8
        self.pincode = Entry(master, font="10", bd=4,relief=SOLID)
        self.pincode.place(x=1030, y=540)
        def clear1():
                self.name_entry.delete(0, END)
                self.age.delete(0, END)
                self.dob_entry.delete(0, END)
                self.adhar.delete(0, END)
                self.country.delete(0, END)
                self.district.delete(0, END)
                self.pincode.delete(0, END)
                self.sex_combo.set("")

        def opens():
            import mysql.connector as m
            db = m.connect(host="localhost", user="sensative_information", password="sensative_information", database="voting")
            mycursor=db.cursor()
            nam=self.name_entry.get()
            ag=self.age.get()
            dob=self.dob_entry.get()
            adr=self.adhar.get()
            county=self.country.get()
            dist=self.district.get()
            pin=self.pincode.get()
            choose=self.sex_combo.get()
            if nam and ag and dob and adr and county and dist and pin and choose:
                s="insert into candidate_registration (candidate_name,Age,D_O_B,Adhar_number,country,district,pin_code,sex)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(nam,ag,dob,adr,county,dist,pin,choose)
                x=mycursor.execute(s,data)
                db.commit()
                print("registration data sucessfully transfer on database")
                voting_voters()

            else:
                messagebox.showerror("Error","all fiels are required to fill \n at the time of registration \n so click log in button \n without click OTP")


        ############## submit button #################
        Button(master,text="Submit",font=("Arial", 14, "bold"),  bg="#4CAF50",  fg="black",  padx=20,  pady=10,  bd=3,  relief=SOLID,activebackground="#45a049", cursor="hand2",command=opens).place(x=600, y=660)
        ############### clear button #################
        Button(master, text="Clear",font=("Arial", 14, "bold"),  bg="#f44336",  fg="black",  padx=20,  pady=10,  bd=3,  relief=SOLID,  activebackground="#45a049", cursor="hand2",command=clear1).place(x=780, y=660)

class page1():

  def clear_fields(self):
        result = messagebox.askyesno("Confirm", "Do you want to deleted your log in details")
        if result:
            self.adhar.delete(0, END)
            self.email_name.delete(0, END)
            self.password_name.delete(0, END)
            self.otp_name.delete(0,END)
            messagebox.showinfo("Deleted", "Your login details have been deleted!")
        else:
            pass

  def generate_otp(self):

      self.email = self.email_name.get()

     # if not email:
        #  messagebox.showerror("Error", "Email field cannot be empty!")
         # return None

      if ("@" not in self.email) or ("gmail" not in self.email and "yahoo" not in self.email):
          messagebox.showerror("Invalid Email", "Please enter a valid Gmail or Yahoo email.")
          return None
      else:
          pass

      otp = str(random.randint(100000, 999999))
      self.generated_otp = otp
      return otp

  # Step 2: Send OTP to user's email
  def send_email(self,receiver_email, otp):
        sender_email = "sensative_information"  # Your Gmail address
        sender_password = "sensative_information"  # Your 16-digit app password (NO spaces)

        subject = "Your OTP Code"
        body = f"Dear User,\n\nYour OTP is: {otp}\n\nThis OTP is valid for 5 minutes."

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            print(f"\n✅ OTP sent successfully to: {receiver_email}")
        except Exception as e:
            print("\n❌ Failed to send OTP:", e)

    # Step 3: Run OTP flow
  def main(self):
      self.otp = self.generate_otp()

      if not self.otp:
          return  # Stop if OTP generation failed due to invalid email

      print(self.otp)
      self.send_email(self.email, self.otp)
      messagebox.showinfo("Success", "Your OTP has been sent successfully to your E-mail")

  def login(self):
        import mysql.connector as m
        db = m.connect(host="localhost", user="sensative_information", password="sensative_information", database="voting")
        mycursor = db.cursor()
        uname = self.adhar.get()
        pwd = self.password_name.get()
        ot=self.otp_name.get()
        if uname and self.email and pwd and ot:
              if self.otp == ot:
                print("login sucessfully")
                Result = messagebox.showinfo("Thanks for completion","Thanks for sucessfully completing your Authentication process")
                l = []
                l.append([uname, self.email, pwd,ot])
                print(l)
                z = "insert into voting_privacy(username,E_mail,Password,OTP)values(%s,%s,%s,%s)"
                data = (uname, self.email, pwd,ot)
                mycursor.execute(z, data)
                # login_win.destroy()
                db.commit()
                print("data transfer sucessfully")
                open_registration_form()
                # open_registration_form()
                self.adhar.delete(0, END)
                self.email_name.delete(0, END)
                self.password_name.delete(0, END)
                self.otp_name.delete(0, END)
              else:
                print("login failed")
                messagebox.showerror("failed", "incorrect OTP")

        else:
            messagebox.showerror("Login Failed", "All fields are required to fill")

  def show_login(self):
    login_win = tk.Tk()
    login_win.title("Virtual Voting Authentication page")
    screen_width = login_win.winfo_screenwidth()
    screen_height = login_win.winfo_screenheight()
    login_win.geometry(f"{screen_width}x{screen_height}")
    login_win.resizable(True, True)

    try:
        original_img = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/auth.jpg")
        resized = original_img.resize((1640, 1000))
        bg_img = ImageTk.PhotoImage(resized)
        bg_label = Label(login_win, image=bg_img)
        bg_label.image = bg_img
        bg_label.place(x=0, y=0, relheight=1, relwidth=1)
    except Exception as e:
        print("Login background error:", e)

    Label(login_win, text="Virtual Voting Candidate Authentication", fg="black", bg="yellow", font=("Helvetica", 25)).pack()

    try:
        auth_img = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/election.jpg")
        resized_auth = auth_img.resize((200,200))
        auth_photo = ImageTk.PhotoImage(resized_auth)
        img_label = Label(login_win, image=auth_photo)
        img_label.image = auth_photo
        img_label.place(x=0, y=60)  # shakal

        lockimg = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/flag.jpg")
        resized_lock = lockimg.resize((220,200))
        lock_photo = ImageTk.PhotoImage(resized_lock)
        img_label = Label(login_win, image=lock_photo)
        img_label.image = lock_photo
        img_label.place(x=850, y=60)  # lock

        lockimg2 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/login.jpg")
        resized_lock2 = lockimg2.resize((80, 80))
        lock_photo2 = ImageTk.PhotoImage(resized_lock2)
        img_label = Label(login_win, image=lock_photo2)
        img_label.image = lock_photo2
        img_label.place(x=430, y=570)

        lockimg3 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/india.jpg")
        resized_lock3 = lockimg3.resize((200, 200))
        lock_photo3 = ImageTk.PhotoImage(resized_lock3)
        img_label = Label(login_win, image=lock_photo3)
        img_label.image = lock_photo3  # gola
        img_label.place(x=200, y=60)

        lockimg4 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/voting.jpg")
        resized_lock4 = lockimg4.resize((200, 200))
        lock_photo4 = ImageTk.PhotoImage(resized_lock4)
        img_label = Label(login_win, image=lock_photo4)
        img_label.image = lock_photo4  # gola
        img_label.place(x=400, y=60)

        lockimg5 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/indians.jpg")
        resized_lock5 = lockimg5.resize((250, 200))
        lock_photo5 = ImageTk.PhotoImage(resized_lock5)
        img_label = Label(login_win, image=lock_photo5)
        img_label.image = lock_photo5  # gola
        img_label.place(x=600, y=60)

        lockimg6 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/electrol.jpg")
        resized_lock6 = lockimg6.resize((220, 200))
        lock_photo6 = ImageTk.PhotoImage(resized_lock6)
        img_label = Label(login_win, image=lock_photo6)
        img_label.image = lock_photo6  # gola
        img_label.place(x=1070, y=60)

        lockimg7 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/voters.jpg")
        resized_lock7 = lockimg7.resize((240, 200))
        lock_photo7 = ImageTk.PhotoImage(resized_lock7)
        img_label = Label(login_win, image=lock_photo7)
        img_label.image = lock_photo7  # gola
        img_label.place(x=1282, y=60)

        lockimg8 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/result.jpg")
        resized_lock8  = lockimg8.resize((430,370))
        lock_photo8 = ImageTk.PhotoImage(resized_lock8)
        img_label = Label(login_win, image=lock_photo8)
        img_label.image = lock_photo8  # gola
        img_label.place(x=1000, y=300)

        lockimg9 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/compare.jpg")
        resized_lock9 = lockimg9.resize((350, 350))
        lock_photo9 = ImageTk.PhotoImage(resized_lock9)
        img_label = Label(login_win, image=lock_photo9)
        img_label.image = lock_photo9  # gola
        img_label.place(x=10, y=300)

        lockimg10 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/indianflag.jpg")
        resized_lock10 = lockimg10.resize((40, 40))
        lock_photo10 = ImageTk.PhotoImage(resized_lock10)
        img_label = Label(login_win, image=lock_photo10)
        img_label.image = lock_photo10  # gola
        img_label.place(x=440, y=0)

        lockimg11 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/govote.jpg")
        resized_lock11 = lockimg11.resize((40,40))
        lock_photo11 = ImageTk.PhotoImage(resized_lock11)
        img_label = Label(login_win, image=lock_photo11)
        img_label.image = lock_photo11  # gola
        img_label.place(x=1050, y=0)

        lockimg12 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/finger.jpg")
        resized_lock12 = lockimg12.resize((80,80))
        lock_photo12 = ImageTk.PhotoImage(resized_lock12)
        img_label = Label(login_win, image=lock_photo12)
        img_label.image = lock_photo12  # gola
        img_label.place(x=20, y=300)

        lockimg13 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/bahujan.jpg")
        resized_lock13 = lockimg13.resize((50, 50))
        lock_photo13 = ImageTk.PhotoImage(resized_lock13)
        img_label = Label(login_win, image=lock_photo13)
        img_label.image = lock_photo13  # gola
        img_label.place(x=1330, y=300)

        lockimg14 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/bjp.jpg")
        resized_lock14 = lockimg14.resize((50, 50))
        lock_photo14 = ImageTk.PhotoImage(resized_lock14)
        img_label = Label(login_win, image=lock_photo14)
        img_label.image = lock_photo14  # gola
        img_label.place(x=1380, y=300)

        lockimg15 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/congress.jpg")
        resized_lock15 = lockimg15.resize((50, 50))
        lock_photo15 = ImageTk.PhotoImage(resized_lock15)
        img_label = Label(login_win, image=lock_photo15)
        img_label.image = lock_photo15  # gola
        img_label.place(x=1280, y=300)

        lockimg16 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/samajvadi.jpg")
        resized_lock16 = lockimg16.resize((50, 50))
        lock_photo16 = ImageTk.PhotoImage(resized_lock16)
        img_label = Label(login_win, image=lock_photo16)
        img_label.image = lock_photo16  # gola
        img_label.place(x=1230, y=300)

        lockimg17 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/aam.jpg")
        resized_lock17 = lockimg17.resize((35,50))
        lock_photo17 = ImageTk.PhotoImage(resized_lock17)
        img_label = Label(login_win, image=lock_photo17)
        img_label.image = lock_photo17  # gola
        img_label.place(x=1195, y=300)

        lockimg18 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/shivsena.jpg")
        resized_lock18 = lockimg18.resize((55,55))
        lock_photo18 = ImageTk.PhotoImage(resized_lock18)
        img_label = Label(login_win, image=lock_photo18)
        img_label.image = lock_photo18  # gola
        img_label.place(x=1000, y=300)

        lockimg19 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/mamta.jpg")
        resized_lock19 = lockimg19.resize((53,53))
        lock_photo19 = ImageTk.PhotoImage(resized_lock19)
        img_label = Label(login_win, image=lock_photo19)
        img_label.image = lock_photo19  # gola
        img_label.place(x=1050, y=300)

        lockimg20 = Image.open("C:/Users/hp/OneDrive/Desktop/votingapp/right.jpg")
        resized_lock20 = lockimg20.resize((130,50))
        lock_photo20 = ImageTk.PhotoImage(resized_lock20)
        img_label = Label(login_win, image=lock_photo20)
        img_label.image = lock_photo20  # gola
        img_label.place(x=662, y=260)





    except Exception as e:
        print("Login image error:", e)
    #label 1
    Label(login_win, text="Adhar-Number", font=("Arial", 20), fg="black", bg="White",relief=SOLID).place(x=470,y=340,
                                                                                        anchor="center")
    # label2
    Label(login_win, text="E-mail", font=("Arial", 24), fg="black", bg="white",relief=SOLID).place(x=470,y=400,
                                                                                      anchor="center")
    # label3
    Label(login_win, text="Password", font=("Arial", 24), fg="black", bg="white",relief=SOLID).place(x=470,y=465,anchor="center")
    # label 4
    Label(login_win, text="Enter-OTP", font=("Arial", 24), fg="black", bg="white",relief=SOLID).place(x=470,y=530,anchor="center")
    # Entry 1

    self.email_name = Entry(login_win, font="10", bd=4,relief=SOLID)
    self.email_name.place(x=620, y=380)

    # Entry2
    self.adhar = Entry(login_win, font="10", bd=4,relief=SOLID)
    self.adhar.place(x=620, y=320)
    # Entry3
    self.password_name = Entry(login_win, font="10", bd=4, show="*",relief=SOLID)
    self.password_name.place(x=620, y=440)
    # Entry4 otp
    self.otp_name=Entry(login_win,font="10",bd=4,relief=SOLID)
    self.otp_name.place(x=620,y=512)

    Button(login_win, text="Log In", font="12", bg="#4CAF50", command=self.login, relief=SOLID).place(x=725, y=600)
    Button(login_win, text="Clear", font="12", bg="#f44336", command=self.clear_fields, relief=SOLID).place(x=850, y=600)
    Button(login_win, text="Click OTP", font="12", bg="#ff5733", relief=SOLID, command=self.main).place(x=570, y=600)

    Label(login_win, text="Made by: Naman Singhal", font=("Arial", 24, "bold"), fg="black", bg="white").place(relx=0.6,                                                                                                rely=0.9,
                                                                                                              anchor="se")
    login_win.mainloop()

def thank():
    obj1=thanks()
    obj1.show()

def voting_voters():
    obj2 = voting()
    obj2.page3()


# login
def open_registration_form():
    global reg_win
    reg_win = tk.Toplevel()
    app = StudentRegistrationApp(reg_win)
    reg_win.mainloop()

# -- START THE APP ---
obj=page1()
obj.show_login()


