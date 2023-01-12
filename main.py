import tkinter as tk
import time

class MainPage(tk.Frame):
    '''
    MainPage class creates an object of the Main Page of The Turtle Game
    '''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, bg="white", height=770, width=1200)
        
        self.bg = tk.PhotoImage(file = './image/start.png')
        self.canvas.create_image(20,30, image=self.bg, anchor="nw")
        self.canvas.pack(fill='both', expand=True)
        
        self.level_label = tk.Label(self, text="Turtle Game", bg='white', font=('Comic Sans MS', 40))
        self.level_label.place(x=100, y=550)
          
        self.switch_window_button = tk.Button(self, text="Start Game", font=('Comic Sans MS', 24), command=lambda: controller.show_frame(Game))
        self.switch_window_button.place(x=900, y=500)
             
        self.instruction_button = tk.Button(self, text="Instructions",font=('Comic Sans MS', 24), command=lambda: controller.show_frame(Instructions))
        self.instruction_button.place(x=900, y=590)
          
class Instructions(tk.Frame):
    '''
    Instructions class creates an object of the Instructions Page of The Turtle Game
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.canvas = tk.Canvas(self, bg="white", height=770, width=1200)
        
        self.bg = tk.PhotoImage(file='./image/instructions.png')
        self.canvas.create_image(20,30, image=self.bg, anchor="nw")
        self.canvas.pack(fill='both', expand=True)
        
        self.switch_window_button = tk.Button(self, text="Start Game", font=('Comic Sans MS', 24), command=lambda: controller.show_frame(Game))
        self.switch_window_button.place(x=730, y=580)
        
class Repeat():
    '''
    Repeat class contains functions that are reused in the Game class
    '''
    def __init__(self):
        pass
    
    def check_movevalidity(self):
        '''

        Returns
        -------
        Boolean
            Function checks if a move is valid as there is a limit on the number of moves.
            Function also prevents input of moves when the turtle is in motion.

        '''
        if self.count == self.number_moves:
            self.warning = self.canvas.create_text(600, 510, text="Too many moves, Press 'Go'", fill="grey", font=('Comic Sans MS', 24), anchor='n')
            self.canvas.update()
            time.sleep(self.warning_speed)
            self.canvas.delete(self.warning)
            return True
        return self.turtle_moving
    
    def create_commonbuttons(self):
        '''
        
        Function creates a set of common buttons on the Canvas,
        used for the game - Forward, Rotate Right, Rotate Left and Dance.
        
        '''
        #initialization of common buttons - Forward, Rotate Right, Rotate Left, Dance
        self.forward_button = tk.Button(self, text="Forward",font=('Comic Sans MS', 15), command=lambda: self.record_move('Forward'))
        self.forward_button.place(x=1050, y=700)
        
        self.rotateright_button = tk.Button(self, text="Rotate Right",font=('Comic Sans MS', 15), command=lambda: self.record_move('Rotate Right'))
        self.rotateright_button.place(x=900, y=700)
        
        self.rotateleft_button = tk.Button(self, text="Rotate Left",font=('Comic Sans MS', 15), command=lambda: self.record_move('Rotate Left'))
        self.rotateleft_button.place(x=760, y=700)
        
        self.dance_button = tk.Button(self, text="Dance",font=('Comic Sans MS', 15), command=lambda: self.dance())
        self.dance_button.place(x=675, y=700)
        
    def create_labelandbutton(self,level_num):
        '''
        
        Function creates a set of buttons and labels on the Canvas,
        used for the game - Go, Restart and Move Label.
        
        '''
        self.go_button = tk.Button(self, text="Go",font=('Comic Sans MS', 15), command=lambda: self.go())
        self.go_button.place(x=520, y=700)

        self.restart_button = tk.Button(self, text="Restart",font=('Comic Sans MS', 15), command=lambda: self.stage(level_num))
        self.restart_button.place(x=575, y=700)

        self.help_label = tk.Label(self, text = "Current Moves: {}".format(self.generateshow_move()), bg="white", font=('Comic Sans MS', 10))
        self.help_label.place(x=20, y=4)
        
    def destroy_labelandbutton(self):
        '''

        Function destroys a set of buttons and labels 
        that are created after the outcome of each attempt.

        '''
        self.complete_top_button.destroy()
        self.restart_button_bottom.destroy()
        self.restart_button.destroy()
        self.movecount_label.destroy()
        self.help_label.destroy()
    
    def destroy_movebutton(self):
        '''

        Function destroys the common set of buttons used for the game.

        '''
        self.forward_button.destroy()
        self.rotateleft_button.destroy()
        self.rotateright_button.destroy()
        self.dance_button.destroy()
    
    def download_photos(self):
        '''

        Function downloads the full set of images 
        used within the game as background and characters.

        '''
        self.bglevel1 = tk.PhotoImage(file='./image/level1.png')
        self.bglevel2 = tk.PhotoImage(file='./image/level2.png')
        self.bglevel3 = tk.PhotoImage(file='./image/level3.png')
        self.bglevel4 = tk.PhotoImage(file='./image/level4.png')
        self.bgloop = tk.PhotoImage(file='./image/loopinstructions.png')
        self.bgexample = tk.PhotoImage(file='./image/example.png')
        
        self.seaturtle0 = tk.PhotoImage(file='./image/turtle0.png')
        self.seaturtle90 = tk.PhotoImage(file='./image/turtle90.png')
        self.seaturtle180 = tk.PhotoImage(file='./image/turtle180.png')
        self.seaturtle270 = tk.PhotoImage(file='./image/turtle270.png')
        self.jellyfish_photo = tk.PhotoImage(file='./image/jellyfish.png')

class Game(tk.Frame, Repeat):
    '''
    Game class contains the full program of the game including its various levels.
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.canvas = tk.Canvas(self, bg="white", height=770, width=1200)
        
        self.download_photos()
        
        self.background_dict = {'Level 1':self.bglevel1, 'Level 2':self.bglevel2, 'Level 3':self.bglevel3,
                                'Level 4':self.bglevel4, 'Example':self.bgexample}
        self.levelgrid_dict = {'Level 1':(10,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
                               'Level 2':(11,[[0,'X',0,0,0],[0,0,0,'X',0],[0,0,0,0,0],[0,0,0,'X',0]]),
                               'Level 3':(6,[[0,'X',0,0,0],[0,0,0,0,0],[0,0,'J',0,0],[0,0,0,'X',0]]),
                               'Level 4':(6,[[0,0,'X',0,0],[0,'X',0,0,0],['X',0,0,0,0],[0,0,0,0,0]]),
                               'Example':(5,[['B','B',0,0,0],['B','B',0,0,0],['B','B',0,0,0],['B','B',0,0,0]])}
        
        self.hint_speed = 2
        self.warning_speed = 1
        self.turtle_dance_speed = 0.4
        self.turtle_movement_speed = 0.8
        
        self.start = (3,0)
        self.end = (0, 4)
        
        #self.turtle_moving = False
        self.create_commonbuttons()
        
        self.go_button = tk.Button(self)
        self.restart_button = tk.Button(self)
        self.level_label = tk.Label(self)
        self.movecount_label = tk.Label(self)
        self.help_label = tk.Label(self)
        
        self.stage('Level 1')
        
        
    def stage(self, level_num):
        '''

        Parameters
        ----------
        level_num : String ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Example')
            The parameter taken in is used to obtain the stage grid and constraints
            from the dictionaries created at the initialisation function.
            level_num is assigned as the key within the dictionaries.

        Function will create the backgrounds, characters, buttons and labels
        at their respective initial position that will facilitate the game.

        '''
        self.canvas.delete('all')
        self.canvas.create_image(20,30, image=self.background_dict[level_num], anchor="nw")
        self.canvas.pack(fill='both', expand=True)
        self.jellyfish = self.canvas.create_image(1030, 53, image=self.jellyfish_photo, anchor="nw")
        
        if level_num == 'Example':
            self.seaturtle = self.canvas.create_image(498, 537, image=self.seaturtle0, anchor="nw")
            self.turtle_position = {'row' : 3, 'column' : 2}
        else:
            self.seaturtle = self.canvas.create_image(35, 519, image=self.seaturtle0, anchor="nw")
            self.turtle_position = {'row' : self.start[0], 'column' : self.start[1]}
        
        if level_num == 'Level 3':
            self.jellyfish_extra = self.canvas.create_image(565, 380, image=self.jellyfish_photo, anchor="nw")
            self.jellyfish_position = (2,2)

        self.turtle_moving = False
        self.level = level_num
        self.move = []
        self.count = 0
        self.turtle_status = "Did not reach the end"
        self.turtle_direction = 0
        
        self.number_moves = self.levelgrid_dict[level_num][0]
        self.level_grid = self.levelgrid_dict[level_num][1]
        
        self.go_button.destroy()
        self.restart_button.destroy()
        self.help_label.destroy()
        
        self.create_labelandbutton(level_num)
        
        self.movecount_label.destroy()
        self.movecount_label = tk.Label(self, text="Moves: {} / {}".format(self.count, self.number_moves), bg="white", font=('Times New Roman', 40))
        self.movecount_label.place(x=100, y=690)
        
        self.level_label.destroy()
        self.level_label = tk.Label(self, text=level_num,bg="white",font=('Comic Sans MS', 15))
        self.level_label.place(x=20, y=690)
        
        if level_num == 'Level 3' or level_num == 'Level 4':
            self.hint_button.destroy()
            self.hint_button = tk.Button(self, text="Hint",font=('Comic Sans MS', 15), command=lambda: self.hint(self.level))
            self.hint_button.place(x=450, y=700)
    
    def dance(self):
        '''

        Function simulates the dancing of the Turtle character
        inspired by the actual dancing of robotics tools used for children.

        '''
        if self.turtle_moving:
            return 
        self.canvas.delete(self.seaturtle)
        self.seaturtle = self.canvas.create_image(35 + (self.turtle_position['column'] * 230), 30 + (self.turtle_position['row'] * 163), image = self.seaturtle0, anchor="nw")
        self.canvas.update()
        time.sleep(self.turtle_dance_speed)
        self.canvas.delete(self.seaturtle)
        self.seaturtle = self.canvas.create_image(78 + (self.turtle_position['column'] * 230), 10 + (self.turtle_position['row'] * 163), image = self.seaturtle90, anchor="nw")
        self.canvas.update()
        time.sleep(self.turtle_dance_speed)
        self.canvas.delete(self.seaturtle)
        self.seaturtle = self.canvas.create_image(35 + (self.turtle_position['column'] * 230), 50 + (self.turtle_position['row'] * 163), image = self.seaturtle180, anchor="nw")
        self.canvas.update()
        time.sleep(self.turtle_dance_speed)
        self.canvas.delete(self.seaturtle)
        self.seaturtle = self.canvas.create_image(50 + (self.turtle_position['column'] * 230), 10 + (self.turtle_position['row'] * 163), image = self.seaturtle270, anchor="nw")
        self.canvas.update()
        time.sleep(self.turtle_dance_speed)
        self.canvas.delete(self.seaturtle)
        self.seaturtle = self.canvas.create_image(35 + (self.turtle_position['column'] * 230), 30 + (self.turtle_position['row'] * 163), image = self.seaturtle0, anchor="nw")
        self.canvas.update()
    
    def record_move(self, move):
        '''

        Parameters
        ----------
        move : String
            The parameter taken in is used to store the move input by the player.
            
        Upon clicking onto movement buttons - Forward, Rotate Right and Rotate Left,
        the function is called and the movement is stored in a list and the various 
        labels will be updated to display the input by the player.

        '''
        if self.check_movevalidity():
            return
        self.count = self.count + 1
        self.move.append(move)
        self.movecount_label.config(text="Moves: {} / {}".format(self.count, self.number_moves))
        self.help_label.config(text = "Current Moves: {}".format(self.generateshow_move()))
    
    def change_turtle_position(self,movement):
        '''

        Parameters
        ----------
        movement : String
            The parameter is taken in to update the position and direction of the Turtle

        Returns
        -------
        boolean
            True will result in a delay of the program to simulate a slow moving Turtle.
            False will prevent any delays hence program will run smoothly.
            
        Function is called upon the use of the 'Go' Button which help players to visualise
        the movements that they have input into the Turtle.

        '''
        if movement == 'None':
            return False
        
        elif movement == 'Forward':
            if self.turtle_direction == 0:
                self.turtle_position['row'] -= 1
            elif self.turtle_direction == 90:
                self.turtle_position['column'] += 1
            elif self.turtle_direction == 180:
                self.turtle_position['row'] += 1
            elif self.turtle_direction == 270:
                self.turtle_position['column'] -= 1
                
        elif movement == 'Rotate Left':
            self.turtle_direction -= 90
            self.turtle_direction %= 360
            
            #turtle to turn on the spot without duplicating
            self.canvas.delete(self.seaturtle)
            
        elif movement == 'Rotate Right': 
            self.turtle_direction += 90
            self.turtle_direction %= 360
            
            #turtle to turn on the spot without duplicating
            self.canvas.delete(self.seaturtle)
            
        return True
        
    def print_turtle(self):
        '''

        Function displays the Turtle character in its specific position and direction.

        '''
        if self.turtle_direction == 0:
            self.canvas.delete(self.seaturtle)
            self.seaturtle = self.canvas.create_image(35 + (self.turtle_position['column'] * 230), 30 + (self.turtle_position['row'] * 163), image = self.seaturtle0, anchor="nw")
            self.canvas.update()
        elif self.turtle_direction == 90:
            self.canvas.delete(self.seaturtle)
            self.seaturtle = self.canvas.create_image(78 + (self.turtle_position['column'] * 230), 10 + (self.turtle_position['row'] * 163), image = self.seaturtle90, anchor="nw")
            self.canvas.update()
        elif self.turtle_direction == 180:
            self.canvas.delete(self.seaturtle)
            self.seaturtle = self.canvas.create_image(35 + (self.turtle_position['column'] * 230), 50 + (self.turtle_position['row'] * 163), image = self.seaturtle180, anchor="nw")
            self.canvas.update()
        elif self.turtle_direction == 270:
            self.canvas.delete(self.seaturtle)
            self.seaturtle = self.canvas.create_image(50 + (self.turtle_position['column'] * 230), 10 + (self.turtle_position['row'] * 163), image = self.seaturtle270, anchor="nw")
            self.canvas.update()
        
    
    def endscreen_restart_level(self, stage):
        '''

        Parameters
        ----------
        stage : String
            The parameter is taken in to ensure that if the restart button is clicked
            the correct stage will be replayed.

        '''
        if self.level == 'Example':
            self.restart_button = tk.Button(self)
        self.destroy_labelandbutton()
        stage(self.level)
        
        
    def next_level(self):
        '''

        The function facilitates the change of stages upon successfully completing the stage.

        '''
        self.destroy_labelandbutton()
        
        if self.level == 'Level 1':
            self.stage('Level 2')
        elif self.level == 'Example':
            self.hint_button = tk.Button(self)
            self.stage('Level 3')
        elif self.level == 'Level 3':
            self.hint_button.destroy()
            self.hint_button = tk.Button(self)
            self.stage('Level 4')
    
    def hint(self, level):
        '''

        Parameters
        ----------
        level : String ('Level 3', 'Level 4')
            The parameters taken in will dictate the hint provided to the player.

        The function will display the hint in the form of a text created on the canvas 
        which aims to help players understand the concept of looping and how it can help 
        them complete the stage despite the constraints.

        '''
        self.hint_dict = {'Level 3':"In this level, the first 5 moves will be repeated TWO times",
                          'Level 4':"In this level, the first 4 moves will be repeated THREE times"}
        self.hint_button.destroy()
        self.level_hint = self.canvas.create_text(35, 760, text=self.hint_dict[level], fill="black", font=('Comic Sans MS', 14), anchor='nw')
        self.canvas.update()
        time.sleep(self.hint_speed)
        self.canvas.delete(self.level_hint)
    
        self.hint_button = tk.Button(self, text="Hint",font=('Comic Sans MS', 15), command=lambda: self.hint(level))
        self.hint_button.place(x=450, y=700)
    

    def generateshow_move(self):
        '''

        The functions is used to generate the moves of the players for them to view their
        past move inputs.

        '''
        if len(self.move) != self.number_moves:
            self.hold_move = self.move + ['None'] * (self.number_moves - len(self.move))
        else:
            self.hold_move = self.move
            
        if self.level == 'Level 3':
            self.show_move = self.hold_move[0:-1] * 2 + [self.hold_move[-1]]
        elif self.level == 'Level 4':
            self.show_move = self.hold_move[0:-2] * 3 + self.hold_move[-2:]
        elif self.level == 'Example':
            self.show_move = self.hold_move[0:-1] * 2 + [self.hold_move[-1]]
        else: 
            self.show_move = self.hold_move
            
        return self.show_move

    
    def go(self):
        '''

        The function facilitates the motion of the Turtle based on the move input by players.
        The function checks to ensure that the Turtle did not leave the grid or encountered
        any of the obstacles placed on each stage.
        The function checks if the Turtle has successfully completed the stage.

        '''
        self.restart_button.destroy()
        self.go_button.destroy()
        
        self.destroy_movebutton()
        
        self.move = self.generateshow_move()
        self.turtle_moving = True
        
        for move in self.move:
            if self.change_turtle_position(move):
                time.sleep(self.turtle_movement_speed)
                
            if self.level == 'Level 3':
                if self.turtle_position['row'] == self.jellyfish_position[0] and self.turtle_position['column'] == self.jellyfish_position[1]:
                    self.canvas.delete(self.jellyfish_extra)
                
            if self.turtle_position['row'] == self.end[0] and self.turtle_position['column'] == self.end[1]:
                self.canvas.delete(self.jellyfish)
                self.turtle_status = 'Completed'
                break
            
            #check turtle position
            if self.turtle_position['row'] < 0 or self.turtle_position['row'] > 3:
                self.turtle_status = 'Out of Bounds'
                break
            elif self.level == 'Example' and (self.turtle_position['column'] < 2 or self.turtle_position['column'] > 4):
                self.turtle_status = 'Out of Bounds'
                break
            
            elif self.level != 'Example' and (self.turtle_position['column'] < 0 or self.turtle_position['column'] > 4):
                self.turtle_status = 'Out of Bounds'
                break
            elif self.level_grid[self.turtle_position['row']][self.turtle_position['column']] == 'X':
                self.turtle_status = 'Encountered an Obstacle'
                break
            self.print_turtle()
            
        self.print_turtle()
        
        self.create_commonbuttons()
        self.check_level(self.stage) #input function as argument with variables
    
    def check_level(self, restart_level):
        '''

        Parameters
        ----------
        restart_level : String (Stage Level)
            The parameter will ensure the correct stage if restarted and 
            the correct next stage.
            
        The function displays the outcome of the attempt, whether the player has failed or
        successfully complete the stage. Function will facilitate the advancement of players
        onto the next stage.

        '''
        self.restart_button_bottom = tk.Button(self, text="Restart",font=('Comic Sans MS', 15), command=lambda: self.endscreen_restart_level(restart_level))
        self.restart_button_bottom.place(x=575, y=700)
        
        if self.turtle_status != 'Completed':
            self.failed = tk.PhotoImage(file = './image/failed.png')
            self.canvas.create_image(400, 150, image = self.failed, anchor='nw')
            self.canvas.create_text(600, 510, text="Outcome: {}".format(self.turtle_status), fill="red", font=('Comic Sans MS', 36), anchor='n')
            
            #restart button
            self.complete_top_button = tk.Button(self, text="Restart",font=('Comic Sans MS', 20), command=lambda: self.endscreen_restart_level(restart_level))
            self.complete_top_button.place(x=600, y=580, anchor='n')
            
        else:
            self.completed = tk.PhotoImage(file = './image/completed.png')
            self.canvas.create_image(400, 150, image = self.completed, anchor='nw')
            self.canvas.create_text(600, 510, text="Outcome: {}".format(self.turtle_status), fill="blue", font=('Comic Sans MS', 36), anchor='n')
            
            if self.level == 'Level 2':
                #next level button
                self.complete_top_button = tk.Button(self, text="Next Level",font=('Comic Sans MS', 20), command=lambda: self.loopinstructions())
                self.complete_top_button.place(x=600, y=580, anchor='n')
                
            elif self.level == 'Level 4':
                #next level button
                self.complete_top_button = tk.Button(self, text="Complete Game",font=('Comic Sans MS', 20), command=lambda: self.controller.show_frame(CompletionScreen))
                self.complete_top_button.place(x=600, y=580, anchor='n')
                
            else:
                #next level button
                self.complete_top_button = tk.Button(self, text="Next Level",font=('Comic Sans MS', 20), command=lambda: self.next_level())
                self.complete_top_button.place(x=600, y=580, anchor='n')
    
    '''
    The loop functions are a separate set of functions used for the looping example stage.
    '''
    def loopinstructions(self):
        self.level_label.destroy()
        
        self.destroy_movebutton()
        self.destroy_labelandbutton()
        
        self.canvas.create_image(20,30, image = self.bgloop, anchor="nw")
        self.canvas.pack(fill = 'both', expand = True)
        self.next_button = tk.Button(self, text="Example", font=('Comic Sans MS', 20), command=lambda: self.loopexample())
        self.next_button.place(x=980, y=580, anchor='n')
        
    def loopexample(self):
        self.next_button.destroy()
        self.canvas.create_image(20,30, image = self.bgexample, anchor="nw")
        self.canvas.pack(fill = 'both', expand = True)
        self.jellyfish = self.canvas.create_image(1020, 53, image = self.jellyfish_photo, anchor="nw")
        self.seaturtle = self.canvas.create_image(498, 537, image = self.seaturtle0, anchor="nw")
        self.attempt_button = tk.Button(self, text="Let's Try",font=('Comic Sans MS', 20), command=lambda: self.looptest())
        self.attempt_button.place(x=250, y=580, anchor='n')
        
    def looptest(self):
        self.attempt_button.destroy()
        self.create_commonbuttons()
        self.create_labelandbutton('Example')
        self.stage('Example')
    
    
class CompletionScreen(tk.Frame):
    '''
    CompletionScreen class creates an object of the Completion Page of The Turtle Game
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, bg="white", height=770, width=1200)
        
        self.bg = tk.PhotoImage(file='./image/end.png')
        self.canvas.create_image(20,30, image=self.bg, anchor="nw")
        self.canvas.pack(fill='both', expand=True)
        
        self.label = tk.Label(self, text="\t   Good job! \nYou saved the turtles! ", bg='white', font=('Times New Roman', 40))
        self.label.place(x=700, y=365)
    
        self.switch_window_button = tk.Button(self, text="Return to menu", font=('Comic Sans MS', 24), command=lambda: controller.show_frame(MainPage))
        self.switch_window_button.place(x=900, y=600)
        
class Application(tk.Tk):
    '''
    Application class helps to faciliate the various screens for the game
    '''
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.window = tk.Frame(self)
        self.window.pack()
    
        self.window.grid_rowconfigure(0, minsize=750)
        self.window.grid_columnconfigure(0, minsize=1000)
    
        self.show_frame(MainPage)

    def show_frame(self, page):
        frame = page(self.window, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

app = Application()
app.mainloop()
