# python learningpython.py
# python learningpython.py
import tkinter  #引入GUI工具包
import random   #引入随机函数
import time     #引入定时器

#创建一个界面和配置界面的一些基本属性
tk = tkinter.Tk()
tk.title('Game')
tk.resizable(0, 0) #表示不能被拉伸
tk.wm_attributes('-topmost', 1) #通知管理器调整布局大小
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()  #使能器件
tk.update() #更新界面


game_startsigal_text=canvas.create_text(430,10,text='DOWN:START',font=('Times',10),state='hidden')
game_endsigal_text=canvas.create_text(430,30,text='UP:END',font=('Times',10),state='hidden')
game_leftsigal_text=canvas.create_text(430,50,text='LEFT:LEFT',font=('Times',10),state='hidden')
game_rightsigal_text=canvas.create_text(430,70,text='RIGHT:RIGHT',font=('Times',10),state='hidden')

game_over_text=canvas.create_text(250,200,text='GAME OVER',font=('Times',30),state='hidden')
game_start_text=canvas.create_text(430,110,text='GAME START',font=('Times',10),state='hidden')
game_score_text=canvas.create_text(430,90,text='SCORE:',font=('Times',10),state='hidden')


#定义木板类
class Paddle:
    def __init__(self,canvas,color): #初始化
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move(self.id,150,380)
        self.started=False
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.canvas.bind_all("<KeyPress-Down>", self.game_start)
        self.canvas.bind_all("<KeyPress-Up>", self.game_stop)
    def turn_left(self,evt): #左转
        self.x=-4
    def turn_right(self,evt): #右转
        self.x=4
    def game_start(self,evt): #开始
        self.started=True
    def game_stop(self,evt): #停止
        self.started = False
    def draw(self):  #画出木板
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=500:
            self.x=0
class Ball():
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.hit_bottom = False
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.y=-3
            score.addscore()
        if pos[0]<=0:
            self.x+=1
        if pos[1]<=0:
            self.y=1
        if pos[2]>=500:
            self.x-=1
        if pos[3]>=self.canvas_height:
            self.y=-1

class Score:
    def __init__(self,canvas,color):
        self.score=0;
        self.canvas=canvas
        canvas.itemconfig(game_score_text, state='normal')
        self.id=canvas.create_text(470,90,text=self.score,fill=color)

        canvas.itemconfig(game_startsigal_text, state='normal')
        canvas.itemconfig(game_endsigal_text, state='normal')
        canvas.itemconfig(game_leftsigal_text, state='normal')
        canvas.itemconfig(game_rightsigal_text, state='normal')
    def addscore(self):
        self.score+=1
        self.canvas.itemconfig(self.id,text=self.score)

paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red')
score=Score(canvas,'black')


while 1:
    if ball.hit_bottom==False and paddle.started==True:
         ball.draw()
         paddle.draw()
         canvas.itemconfig(game_start_text, state='normal')
    if ball.hit_bottom==True:
        canvas.itemconfig(game_over_text, state='normal')
        canvas.itemconfig(game_start_text, state='hidden')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


