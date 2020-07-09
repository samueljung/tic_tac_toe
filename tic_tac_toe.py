from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Welcome to Tic-Tac-Toe!")
# root.geometry("600x750")

# pictures resized for use
temp_pic = Image.open("tic_tac_toe_board.png")
my_pic = temp_pic.resize((600,600), Image.ANTIALIAS)
board_pic = ImageTk.PhotoImage(my_pic)

temppic1 = Image.open("circle.png")
mypic1 = temppic1.resize((100,100), Image.ANTIALIAS)
circle_pic = ImageTk.PhotoImage(mypic1)

temppic2 = Image.open("cross.png")
mypic2 = temppic2.resize((100,100), Image.ANTIALIAS)
cross_pic = ImageTk.PhotoImage(mypic2)


# global variables
counter = 0
bool_temp = True
bool_temp2 = True
bool_winner = False
board_list = [" "," "," "," "," "," "," "," "," "]


def replay():
    global counter
    global board_list
    global bool_temp
    global bool_temp2
    global bool_winner
    root.nametowidget(main_frame).destroy()
    root.nametowidget(bottom_frame).destroy()
    counter = 0
    board_list = [" "," "," "," "," "," "," "," "," "]
    bool_winner = False
    if bool_temp2 is False:
        bool_temp = False
    else:
        bool_temp = True
    create_board()

def replay_options():
    global counter
    global bottom_frame
    global bool_winner
    
    #bottom_frame for replay option will pop up when board is full or someone won
    bottom_frame = Frame(root)
    bottom_frame.pack(pady = 20)
    label2 = Label(bottom_frame, text = "Oi there mate replay?")
    label2.grid(row = 1, column = 0, columnspan = 2)
    if bool_winner == True:
        label = Label(bottom_frame, text= "Oi we have a winner!")
        label.grid(row = 0, column = 0, columnspan = 2)
        
    bool_winner = False

    button_replay = Button(bottom_frame, text = "YES", command = replay)
    button_replay.grid(row = 2, column = 0)
    button_quit = Button(bottom_frame, text = "NO", command = root.destroy)
    button_quit.grid(row = 2, column = 1)
        
    


def check_winner_circle():
    mark = "O"
    if board_list[0] == mark and board_list[1] == mark and board_list[2] == mark:
        return True
    elif board_list[3] == mark and board_list[4] == mark and board_list[5] == mark:
        return True
    elif board_list[6] == mark and board_list[7] == mark and board_list[8] == mark:
        return True
    elif board_list[0] == mark and board_list[3] == mark and board_list[6] == mark:
        return True
    elif board_list[1] == mark and board_list[4] == mark and board_list[7] == mark:
        return True
    elif board_list[2] == mark and board_list[5] == mark and board_list[8] == mark:
        return True
    elif board_list[0] == mark and board_list[4] == mark and board_list[8] == mark:
        return True
    elif board_list[2] == mark and board_list[4] == mark and board_list[6] == mark:
        return True
    else:
        return False

def check_winner_cross():
    mark = "X"
    if board_list[0] == mark and board_list[1] == mark and board_list[2] == mark:
        return True
    elif board_list[3] == mark and board_list[4] == mark and board_list[5] == mark:
        return True
    elif board_list[6] == mark and board_list[7] == mark and board_list[8] == mark:
        return True
    elif board_list[0] == mark and board_list[3] == mark and board_list[6] == mark:
        return True
    elif board_list[1] == mark and board_list[4] == mark and board_list[7] == mark:
        return True
    elif board_list[2] == mark and board_list[5] == mark and board_list[8] == mark:
        return True
    elif board_list[0] == mark and board_list[4] == mark and board_list[8] == mark:
        return True
    elif board_list[2] == mark and board_list[4] == mark and board_list[6] == mark:
        return True
    else:
        return False
    
def populate_board(event):
    global counter
    global bool_temp
    global bool_winner
    counter += 1
    if counter == 9 and bool_temp is False:
        parent_name = event.widget.winfo_parent()
        index_number = int(parent_name[-1])
        board_list[index_number] = "O"
        parent_widget = event.widget._nametowidget(parent_name)
        root.nametowidget(event.widget).destroy()
        label = Label(parent_widget, image = circle_pic)
        label.pack(padx = 29, pady = 29)
        if check_winner_circle() == True or check_winner_cross() == True:
            bool_winner = True
        #replay
        replay_options()
    elif counter == 9 and bool_temp is True:
        parent_name = event.widget.winfo_parent()
        index_number = int(parent_name[-1])
        board_list[index_number] = "X"
        parent_widget = event.widget._nametowidget(parent_name)
        root.nametowidget(event.widget).destroy()
        label = Label(parent_widget, image = cross_pic)
        label.pack(padx = 29, pady = 29)
        if check_winner_circle() == True or check_winner_cross() == True:
            bool_winner = True
        #replay
        replay_options()
    elif counter < 9 and bool_temp is True:
        parent_name1 = event.widget.winfo_parent()
        index_number1 = int(parent_name1[-1])
        board_list[index_number1] = "X"
        parent_widget1 = event.widget._nametowidget(parent_name1)
        root.nametowidget(event.widget).destroy()
        label = Label(parent_widget1, image = cross_pic)
        label.pack(padx = 29, pady = 29)
        if check_winner_circle() == True or check_winner_cross() == True:
            bool_winner = True
            replay_options()
        bool_temp = False
    elif counter < 9 and bool_temp is False:
        parent_name2 = event.widget.winfo_parent()
        index_number2 = int(parent_name2[-1])
        board_list[index_number2] = "O"
        parent_widget2 = event.widget._nametowidget(parent_name2)
        root.nametowidget(event.widget).destroy()
        label = Label(parent_widget2, image = circle_pic)
        label.pack(padx = 29, pady = 29)
        if check_winner_circle() == True or check_winner_cross() == True:
            bool_winner = True
            replay_options()
        bool_temp = True
    
def choose_mark(event):
    global bool_temp
    global bool_temp2
    temp_string = str(event.widget)
    if temp_string == ".!labelframe.circle_button":
        bool_temp = False
        bool_temp2 = False
        create_board()
    else:
        bool_temp = True
        bool_temp2 = True
        create_board()

    
def create_board():
    global main_frame
    global bottom_frame
    global counter
    # get rid of home_button for the first time
    if home_frame.winfo_exists() == 1:
        root.nametowidget(home_frame).destroy()
    #if you want to replay the game clear the frames
    
    #create main_frame where board and button grid is
    main_frame = Frame(root)
    main_frame.pack()
    #create board
    canvas = Canvas(main_frame, width = 600, height = 600, bg = "gray")
    canvas.pack()
    canvas.create_image(3,3, anchor = "nw", image = board_pic)
    #create button windows
    test_frame0 = Frame(main_frame, name = "test_frame0")
    test_frame0.pack()
    testbutton0 = Button(test_frame0, padx = 80, pady = 71)
    testbutton0.grid(row = 0, column = 0)
    testbutton0.bind("<Button-1>", populate_board)
    canvas.create_window(5,6,anchor = "nw", window = test_frame0)

    test_frame1 = Frame(main_frame, name = "test_frame1")
    test_frame1.pack()
    testbutton1 = Button(test_frame1, padx = 78, pady = 71)
    testbutton1.grid(row = 0, column = 0)
    testbutton1.bind("<Button-1>", populate_board)
    canvas.create_window(221,6,anchor = "nw", window = test_frame1)

    test_frame2 = Frame(main_frame, name = "test_frame2")
    test_frame2.pack()
    testbutton2 = Button(test_frame2, padx = 80, pady = 71)
    testbutton2.grid(row = 0, column = 0)
    testbutton2.bind("<Button-1>", populate_board)
    canvas.create_window(436,6,anchor = "nw", window = test_frame2)

    test_frame3 = Frame(main_frame, name = "test_frame3")
    test_frame3.pack()
    testbutton3 = Button(test_frame3, padx = 80, pady = 71)
    testbutton3.grid(row = 0, column = 0)
    testbutton3.bind("<Button-1>", populate_board)
    canvas.create_window(5,220,anchor = "nw", window = test_frame3)

    test_frame4 = Frame(main_frame, name = "test_frame4")
    test_frame4.pack()
    testbutton4 = Button(test_frame4, padx = 78, pady = 71)
    testbutton4.grid(row =0, column = 0)
    testbutton4.bind("<Button-1>", populate_board)
    canvas.create_window(221,220,anchor = "nw", window = test_frame4)

    test_frame5 = Frame(main_frame, name = "test_frame5")
    test_frame5.pack()
    testbutton5 = Button(test_frame5, padx = 80, pady = 71)
    testbutton5.grid(row = 0, column = 0)
    testbutton5.bind("<Button-1>", populate_board)
    canvas.create_window(436,220,anchor = "nw", window = test_frame5)

    test_frame6 = Frame(main_frame, name = "test_frame6")
    test_frame6.pack()
    testbutton6 = Button(test_frame6, padx = 80, pady = 71)
    testbutton6.grid(row = 0, column = 0)
    testbutton6.bind("<Button-1>", populate_board)
    canvas.create_window(5,435,anchor = "nw", window = test_frame6)

    test_frame7 = Frame(main_frame, name = "test_frame7")
    test_frame7.pack()
    testbutton7 = Button(test_frame7, padx = 78, pady = 71)
    testbutton7.grid(row = 0, column = 0)
    testbutton7.bind("<Button-1>", populate_board)
    canvas.create_window(221,435,anchor = "nw", window = test_frame7)

    test_frame8 = Frame(main_frame, name = "test_frame8")
    test_frame8.pack()
    testbutton8 = Button(test_frame8, padx = 80, pady = 71)
    testbutton8.grid(row = 0, column = 0)
    testbutton8.bind("<Button-1>", populate_board)
    canvas.create_window(436,435,anchor = "nw", window = test_frame8)


home_frame = LabelFrame(root, text = "Oi there mate welcome", pady = 20, padx = 20)
home_frame.pack(padx = 100, pady = 50)


button_circle = Button(home_frame, text = "O", padx = 15, pady = 5, name = "circle_button")
button_circle.grid(row = 0, column = 0, padx = 10)
button_circle.bind("<Button-1>", choose_mark)


button_cross = Button(home_frame, text = "X", padx = 15, pady = 5, name = "cross_button")
button_cross.grid(row = 0, column = 1)
button_cross.bind("<Button-1>", choose_mark)

root.mainloop()