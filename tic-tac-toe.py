import array
import numpy
import random
from tkinter import *
from tkinter import messagebox
# Initialize our graphics frame named Tk and the dialog box is titles Tic Tac Toe
tk=Tk()
tk.title("Tic Tac Toe")

# global variables

arryButtons = []
boolAr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
moves = 0
state = 0

def ttt(i):

     global arryButtons
     global boolAr
     global moves

     if state == 0:
         if arryButtons[i]["text"] == " " and (moves % 2 == 0):
              arryButtons[i]["text"] = "X"
              boolAr[i] = 1
              moves+=1
         elif arryButtons[i]["text"] == " " and (moves % 2 == 1):
              arryButtons[i]["text"] = "O"
              boolAr[i] = 2
              moves+=1

         if(moves >= 5):
             if((boolAr[0] == boolAr[1] == boolAr[2]) or (boolAr[0] == boolAr[4] == boolAr[8]) or (boolAr[0] == boolAr[3] == boolAr[6])):
                 win_state(0);

             if((boolAr[1] == boolAr[4] == boolAr[7]) or (boolAr[3] == boolAr[4] == boolAr[5]) or (boolAr[2] == boolAr[4] == boolAr[6]) ):
                 win_state(4);

             if((boolAr[2] == boolAr[5] == boolAr[8]) or (boolAr[6] == boolAr[7] == boolAr[8])):
                 win_state(8);

             if (state == 1):
                messagebox.showinfo("Player X","Winner is X !!!")
             elif(state == 2):
                messagebox.showinfo("Player O","Winner is O !!!")

         if(state == 0 and moves == 9):
                messagebox.showinfo("Draw", "You've scratched the cat!")
                reset_game()
         if (state != 0):
             reset_game()


def win_state(j):
    global state
    if boolAr[j] == 1:
        state = 1
    elif boolAr[j] == 2:
        state = 2

def reset_game():
    if(messagebox.askyesno("Done", "Want to restart?") == True):
        createButtons()
    else:
        tk.destroy()

def createButtons():
    global moves
    global boolAr
    global arryButtons
    global state
    h = 5
    w = 10

    arryButtons = []

    button0 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(0))
    button0.grid(row=1,column=0,sticky = S+N+E+W)
    arryButtons.append(button0)

    button1 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(1))
    button1.grid(row=1,column=1,sticky = S+N+E+W)
    arryButtons.append(button1)

    button2 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(2))
    button2.grid(row=1,column=2,sticky = S+N+E+W)
    arryButtons.append(button2)

    button3 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(3))
    button3.grid(row=2,column=0,sticky = S+N+E+W)
    arryButtons.append(button3)

    button4 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(4))
    button4.grid(row=2,column=1,sticky = S+N+E+W)
    arryButtons.append(button4)

    button5 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(5))
    button5.grid(row=2,column=2,sticky = S+N+E+W)
    arryButtons.append(button5)

    button6 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(6))
    button6.grid(row=3,column=0,sticky = S+N+E+W)
    arryButtons.append(button6)

    button7 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(7))
    button7.grid(row=3,column=1,sticky = S+N+E+W)
    arryButtons.append(button7)

    button8 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='black',height=h,width=w,command=lambda:ttt(8))
    button8.grid(row=3,column=2,sticky = S+N+E+W)
    arryButtons.append(button8)

    # Resetting game state: Necessary to have!
    moves = 0
    boolAr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    state = 0

createButtons()

tk.mainloop()
