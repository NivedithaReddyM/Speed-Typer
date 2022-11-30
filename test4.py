from tkinter import*
from tkinter import messagebox
from timeit import default_timer as timer
import random
from words import words1,words2,words3
a=[]

file=open("test.txt",'w')
file.write("Welcome"+'\n')
file=open("test.txt",'r')


import pyttsx3
file=open("test.txt")
read=file.readlines()
speaker=pyttsx3.init()
speaker.say(read[0])
speaker.runAndWait()

root=Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
# calculate position x, y
x = (ws/2) - (500/2)    
y = (hs/2) - (500/2)
root.geometry("1525x780+0+0")
root.configure(bg="light blue")


"""w=Tk()
w.geometry('500x400')


w.mainloop()"""






window=Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
# calculate position x, y
x = (ws/2) - (500/2)    
y = (hs/2) - (500/2)
window.geometry("1525x780+0+0")
window.configure(bg="light blue")

window.withdraw()




hs_file=open('highscore.txt','r+')
x=0

def lev():
    r=Tk()
    ws = r.winfo_screenwidth()
    hs = r.winfo_screenheight()
    # calculate position x, y
    z= (ws/2) - (500/2)    
    y = (hs/2) - (500/2)
    r.geometry("1525x780+0+0")
    
    r.configure(bg="Navajowhite2")

    def tips():
        import webbrowser as wb
        wb.open_new(r'C:\Users\MYPC\Documents\EE project-2\tips.pptx')
    


    def level1():
        global x
        if x==0:
            root.withdraw()
            x=x+1
        window.deiconify()
        def check_result():
            j=error=0
            count=0
            answer=entry.get("1.0",'end-1c')
            end=timer()
            time_taken=end-start
            time_taken=int(time_taken)
            

            #len diff
            if len(words1[word1])>=len(answer):
                error=len(words1[word1])-len(answer)
                for i in answer:   
                    if i == words1[word1][j]:
                        count+=1
                    else:

                       
                        a.append(i)
                        
                        
                
                        
                        error+=1
                    j+=1
                
            elif len(words1[word1])<=len(answer1):
                error=len(answer)-len(words1[word1])
                for i in words1[word1]:
                    if i==answer[j]:
                        count+=1
                    else:
                        error+=1
                        
                        
                    j+=1
                

            accuracy=(count*100)/len(words1[word1])
            accuracy=int(accuracy)
            
            wpm=len(answer)/4
            
            wpm=int(wpm/(time_taken/60))
            hs_file.seek(0)
            line=int(hs_file.readline())
            if wpm>line:
                hs_file.seek(0)
                hs_file.write(str(wpm))
                #result="Amazing! Your new highscore is: "+str(wpm)+" WPM"
                #messagebox.showinfo("Score",result)
                
                w=Tk()
                ws = root.winfo_screenwidth()
                hs = root.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (500/2)    
                y = (hs/2) - (500/2)
                w.geometry("1525x780+0+0")
                w.configure(bg="light blue")
                w.title("Result")
                
                
                e="you have typed the letter {} wrong\n".format(a) 
                b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                
                w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                w2.place(x=640,y=0)

                w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                w1.place(x=380,y=290)
                

                b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                file=open("test.txt",'a')
                file.write(b)
                file=open("test.txt",'r')
                print(file.read())

                file=open("score.txt","w+")
                file.write(str(wpm))
                file.write("\n")
                file.write(str(accuracy))
                file.close()

                

               

                import pyttsx3
                file=open("test.txt")
                read=file.readlines()
                speaker=pyttsx3.init()
                speaker.say(read[1])
                speaker.runAndWait()

                file=open("score.txt","r")
                s=file.readlines()
                if(int(s[0])>=25 and int(s[1])==100):
                       
                    messagebox.showinfo("information","eligible for 2nd level")
                        
                else:
                    messagebox.showinfo("information","Not eligible for 2nd level")
  

                
                    


                
            else:
                #result="Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"
                #messagebox.showinfo("Details:\n",result)

                e="you have typed the letter {} wrong\n".format(a) 
                b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                

                w=Tk()
                ws = root.winfo_screenwidth()
                hs = root.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (500/2)    
                y = (hs/2) - (500/2)
                w.geometry("1525x780+0+0")
                w.configure(bg="light blue")
                w.title("Result")
                w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                w2.place(x=640,y=0)

                w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                w1.place(x=380,y=290)
                

                b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                file=open("test.txt",'a')
                file.write(b)
                file=open("test.txt",'r')
                print(file.read())

                file=open("score.txt","w+")
                file.write(str(wpm))
                file.write("\n")
                file.write(str(accuracy))
                file.close()

                import pyttsx3
                file=open("test.txt")
                read=file.readlines()
                speaker=pyttsx3.init()
                speaker.say(read[1])
                speaker.runAndWait()
                
                file=open("score.txt","r")
                s=file.readlines()
                if(int(s[0])>=25 and int(s[1])==100):
                       
                    messagebox.showinfo("information","eligible for 2nd level")
                        
                else:
                    messagebox.showinfo("information","Not eligible for 2ndd level")
                     


                
        """words=["Whatever you are be a good one.","Don't stop when you're tired.","Stop when you're done.","Make each day your master piece"]"""
        word1=random.randint(0,(len(words1)-1))

        def finish():
            hs_file.close()
            window.destroy()
            root.destroy()

        """words1=["Do your best","Never give up"]
        word1=random.randint(0,(len(words1)-1))"""


        

        x2=Label(window,text=words1[word1],font=('calibri', 21, 'bold'),height=5,width=99,bd=5,relief=SUNKEN,bg="white",wraplength=1000)
        x2.place(x=15,y=10)

        x3=Button(window,text="SUBMIT",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=check_result)
        x3.place(x=630,y=586)

        entry=Text(window,font=('calibri', 21, 'bold'),width=106,bd=5,relief=SUNKEN,bg="white")
        entry.place(x=15,y=240,height=300)

        b2=Button(window,text="DONE",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=finish)
        b2.place(x=510,y=680)

        b3=Button(window,text="ANOTHER ONE",font=('calibri', 21, 'bold'),width=12,bd=5,relief=SUNKEN,bg="white",command=level1)
        b3.place(x=730,y=680)

        start=timer()

        r.withdraw()         
        window.mainloop()

        


            
    def level2():
        file=open("score.txt","r")
        z=file.readlines()
            
        if (int(z[0])<35 or int(z[1])!=100):
            messagebox.showinfo("information","not eligible for 2nd level")  
  
            
        
        else:
            
        
            global x
            if x==0:
                root.withdraw()
                x=x+1
            window.deiconify()
            def check_result():
                j=error=0
                count=0
                answer=entry.get("1.0",'end-1c')
                end=timer()
                time_taken=end-start
                time_taken=int(time_taken)
                

                #len diff
                if len(words2[word2])>=len(answer):
                    error=len(words2[word2])-len(answer)
                    for i in answer:   
                        if i == words2[word2][j]:
                            count+=1
                        else:

                           
                            a.append(i)
                            
                            
                    
                            
                            error+=1
                        j+=1
                    
                elif len(words2[word2])<=len(answer):
                    error=len(answer)-len(words2[word2])
                    for i in words2[word2]:
                        if i==answer[j]:
                            count+=1
                        else:
                            error+=1
                            
                            
                        j+=1
                    

                accuracy=(count*100)/len(words2[word2])
                accuracy=int(accuracy)
                
                wpm=len(answer)/4
                
                wpm=int(wpm/(time_taken/60))
                hs_file.seek(0)
                line=int(hs_file.readline())
                if wpm>line:
                    hs_file.seek(0)
                    hs_file.write(str(wpm))
                    #result="Amazing! Your new highscore is: "+str(wpm)+" WPM"
                    #messagebox.showinfo("Score",result)
                    
                    
                    

                    w=Tk()
                    ws = root.winfo_screenwidth()
                    hs = root.winfo_screenheight()
                    # calculate position x, y
                    x = (ws/2) - (500/2)    
                    y = (hs/2) - (500/2)
                    w.geometry("1525x780+0+0")
                    w.configure(bg="light blue")
                    w.title("Result")
                    
                    e="you have typed the letter {} wrong\n".format(a) 
                    b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                    w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                    w2.place(x=640,y=0)

                    w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                    w1.place(x=380,y=290)
                
                    b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                    file=open("test.txt",'a')
                    file.write(b)
                    file=open("test.txt",'r')
                    print(file.read())

                    file1=open("score1.txt","w+")
                    file1.write(str(wpm))
                    file1.write("\n")
                    file1.write(str(accuracy))
                    file1.close()

                    import pyttsx3
                    file=open("test.txt")
                    read=file.readlines()
                    speaker=pyttsx3.init()
                    speaker.say(read[1])
                    speaker.runAndWait()

                    file=open("score1.txt","r")
                    s=file.readlines()
                    if(int(s[0])>=40 and int(s[1])==100):
                       
                        messagebox.showinfo("information","eligible for 3rd level")
                        
                    else:
                        messagebox.showinfo("information","Not eligible for 3rd level")
                     
      

                


                    
                else:
                    #result="Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"
                    #messagebox.showinfo("Details:\n",result)

                    e="you have typed the letter {} wrong\n".format(a) 
                    b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                    

                    w=Tk()
                    ws = root.winfo_screenwidth()
                    hs = root.winfo_screenheight()
                    # calculate position x, y
                    x = (ws/2) - (500/2)    
                    y = (hs/2) - (500/2)
                    w.geometry("1525x780+0+0")
                    w.configure(bg="light blue")
                    w.title("Result")

                    w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                    w2.place(x=640,y=0)

                    w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                    w1.place(x=380,y=290)
                
                    

                    b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                    file=open("test.txt",'a')
                    file.write(b)
                    file=open("test.txt",'r')
                    print(file.read())

                    file1=open("score1.txt","w+")
                    file1.write(str(wpm))
                    file1.write("\n")
                    file1.write(str(accuracy))
                    file1.close()

                    import pyttsx3
                    file=open("test.txt")
                    read=file.readlines()
                    speaker=pyttsx3.init()
                    speaker.say(read[1])
                    speaker.runAndWait()

                    file=open("score1.txt","r")
                    s=file.readlines()
                    if(int(s[0])>=40 and int(s[1])==100):
                       
                        messagebox.showinfo("information","eligible for 3rd level")
                        
                    else:
                        messagebox.showinfo("information","Not eligible for 3rd level")
                     

      

                
                                

            def finish():
                hs_file.close()
                window.destroy()
                root.destroy()
                
            

            """words1=["Do your best","Never give up"]"""
            word2=random.randint(0,(len(words2)-1))


                

            x2=Label(window,text=words2[word2],font=('calibri', 21, 'bold'),height=5,width=99,bd=5,relief=SUNKEN,bg="white",wraplength=1400)
            x2.place(x=15,y=10)

            x3=Button(window,text="SUBMIT",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=check_result)
            x3.place(x=630,y=586)

            entry=Text(window,font=('calibri', 21, 'bold'),width=106,bd=5,relief=SUNKEN,bg="white")
            entry.place(x=15,y=240,height=300)

            b2=Button(window,text="DONE",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=finish)
            b2.place(x=510,y=680)

            b3=Button(window,text="ANOTHER ONE",font=('calibri', 21, 'bold'),width=12,bd=5,relief=SUNKEN,bg="white",command=level2)
            b3.place(x=730,y=680)

            start=timer()

        r.withdraw()         
        window.mainloop()



             
    def level3():
        file=open("score1.txt","r")
        y=file.readlines()
            
        if (int(y[0])<40 or int(y[1])!=100):
            messagebox.showinfo("information","not eligible for 3rd level")  
  
            
        
        else:
            
        
            global x
            if x==0:
                root.withdraw()
                x=x+1
            window.deiconify()
            def check_result():
                j=error=0
                count=0
                answer=entry.get("1.0",'end-1c')
                end=timer()
                time_taken=end-start
                time_taken=int(time_taken)
                

                #len diff
                if len(words3[word3])>=len(answer):
                    error=len(words3[word3])-len(answer)
                    for i in answer:   
                        if i == words3[word3][j]:
                            count+=1
                        else:

                           
                            a.append(i)
                            
                            
                    
                            
                            error+=1
                        j+=1
                    
                elif len(words3[word3])<=len(answer):
                    error=len(answer)-len(words3[word3])
                    for i in words3[word3]:
                        if i==answer[j]:
                            count+=1
                        else:
                            error+=1
                            
                            
                        j+=1
                    

                accuracy=(count*100)/len(words3[word3])
                accuracy=int(accuracy)
                
                wpm=len(answer)/4
                
                wpm=int(wpm/(time_taken/60))
                hs_file.seek(0)
                line=int(hs_file.readline())
                if wpm>line:
                    hs_file.seek(0)
                    hs_file.write(str(wpm))
                    #result="Amazing! Your new highscore is: "+str(wpm)+" WPM"
                    #messagebox.showinfo("Score",result)
                    
                    
                    

                    w=Tk()
                    ws = root.winfo_screenwidth()
                    hs = root.winfo_screenheight()
                    # calculate position x, y
                    x = (ws/2) - (500/2)    
                    y = (hs/2) - (500/2)
                    w.geometry("1525x780+0+0")
                    w.configure(bg="light blue")
                    w.title("Result")
                    
                    e="you have typed the letter {} wrong\n".format(a) 
                    b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                    w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                    w2.place(x=640,y=0)

                    w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                    w1.place(x=380,y=290)
                

                    b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                    file=open("test.txt",'a')
                    file.write(b)
                    file=open("test.txt",'r')
                    print(file.read())

                    
                    import pyttsx3
                    file=open("test.txt")
                    read=file.readlines()
                    speaker=pyttsx3.init()
                    speaker.say(read[1])
                    speaker.runAndWait()

                    

                


                    
                else:
                    #result="Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"
                    #messagebox.showinfo("Details:\n",result)

                    e="you have typed the letter {} wrong\n".format(a) 
                    b=e+"Your score is: "+str(wpm)+" WPM\nTime taken is: "+str(time_taken)+" seconds\nAccuracy is: "+str(accuracy)+" %\nBetter Luck next time!"

                    

                    w=Tk()
                    ws = root.winfo_screenwidth()
                    hs = root.winfo_screenheight()
                    # calculate position x, y
                    x = (ws/2) - (500/2)    
                    y = (hs/2) - (500/2)
                    w.geometry("1525x780+0+0")
                    w.configure(bg="light blue")
                    w.title("Result")

                    w2=Label(w,text='Result',width=10,height=1,font=('calibri', 21, 'bold'),bg="white")
                    w2.place(x=640,y=0)

                    w1=Label(w,text=b,font=('calibri', 21, 'bold'),width=50,height=7,bd=5,relief=SUNKEN,bg="white")
                    w1.place(x=380,y=290)
                
                    

                    b="Your score is: "+str(wpm)+" WPM and Time taken is: "+str(time_taken)+" seconds and Accuracy is: "+str(accuracy)+" %  Better Luck next time!"
                    file=open("test.txt",'a')
                    file.write(b)
                    file=open("test.txt",'r')
                    print(file.read())

                    

                    import pyttsx3
                    file=open("test.txt")
                    read=file.readlines()
                    speaker=pyttsx3.init()
                    speaker.say(read[1])
                    speaker.runAndWait()

                   
                
                                

            def finish():
                hs_file.close()
                window.destroy()
                root.destroy()
                
            

            """words2=["Success is not final","No pain no gain"]"""
            word3=random.randint(0,(len(words3)-1))


                

            x2=Label(window,text=words3[word3],font=('calibri', 15, 'bold'),height=7,width=130,bd=5,relief=SUNKEN,bg="white",wraplength=1000)
            x2.place(x=15,y=10)

            x3=Button(window,text="SUBMIT",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=check_result)
            x3.place(x=600,y=550)

            entry=Text(window,font=('calibri', 21, 'bold'),width=106,bd=5,relief=SUNKEN,bg="white")
            entry.place(x=15,y=240,height=300)

            b2=Button(window,text="DONE",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=finish)
            b2.place(x=540,y=630)

            b3=Button(window,text="ANOTHER ONE",font=('calibri', 21, 'bold'),width=12,bd=5,relief=SUNKEN,bg="white",command=level3)
            b3.place(x=680,y=630)

            start=timer()

        r.withdraw()         
        window.mainloop()

        

        

    r1=Button(r,text="level1",font="times 20",bg="#fc2828",command=level1)
    r1.place(x=(ws/2)-50,y=300)

    r2=Button(r,text="leve12",font="times 20",bg="#fc2828",command=level2)
    r2.place(x=(ws/2)-50,y=400)

    r3=Button(r,text="level3",font="times 20",bg="#fc2828",command=level3)
    r3.place(x=(ws/2)-50,y=500)

    r4=Button(r,text="TIPS",font="times 20",bg="#fc2828",command=tips)
    r4.place(x=(ws/2)-50,y=200)
    
    root.withdraw()
    r.mainloop()






x1=Label(root,text="WELCOME TO SPEED TYPING",font=('calibri', 21, 'bold'),width=25,bd=5,relief=SUNKEN,)
x1.place(x=550,y=50)

x2=Label(root,text="Let's test your typing speed",font=('calibri', 21, 'bold'), width=40,bd=8,relief=SUNKEN,bg="white",fg="black",)
x2.place(x=440,y=150)

b1=Button(root,text="Go!",font=('calibri', 21, 'bold'),width=10,bd=5,relief=SUNKEN,bg="white",command=lev)
b1.place(x=650,y=260)

hs_text=Label(root,text="Highscore",font=('calibri', 21, 'bold'),width=16,bd=5,relief=SUNKEN,)
hs_text.place(x=620,y=400)

hs=int(hs_file.readline())
hs_val=Label(root,text=str(hs)+" WPM",font=('calibri', 21, 'bold'),width=16,bd=5,relief=SUNKEN,)

hs_val.place(x=620,y=480)


root.mainloop() 


  
