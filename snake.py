from tkinter import *
import random
import copy
from tkinter import messagebox

top = Tk()
kwad = []
dir = ["up", "right", "down", "left"]
snakecolor="red"
bgcolor="grey1"
C = Canvas(top, bg=bgcolor, height=500, width=500, bd=0)
for i in range(50):
    for j in range(50):
        kwad.append(C.create_rectangle(j * 10, i * 10, (j + 1) * 10, (i + 1) * 10, fill=bgcolor, outline=bgcolor))



def respawn():
    for i in range(50):
        for j in range(50):
            C.itemconfig(kwad[i * 50 + j], fill=bgcolor)
    Bug(top)



class Bug:
    def __init__(self, master):
        self.pos = [random.randint(20, 30), random.randint(20, 30)]
        self.master = master
        self.dir = random.choice(dir)
        self.waz = []
        self.waz.append(copy.deepcopy(self.pos))
        self.dlugosc = 1
        self.growing = False
        self.continu = True
        self.queue = []
        C.itemconfig(kwad[self.pos[0] * 50 + self.pos[1]], fill=snakecolor)
        self.master.bind('<Up>', self.turnup)
        self.master.bind('<Down>', self.turndown)
        self.master.bind('<Left>', self.turnleft)
        self.master.bind('<Right>', self.turnright)
        self.move()
        self.seed()

    def move(self):

        if len(self.queue) > 0:
            print(self.queue)
            self.dir = self.queue.pop(0)

        if self.dir == "up":
            if self.pos[0] > 0:
                if C.itemcget(kwad[((self.pos[0] - 1) * 50 + self.pos[1])], "fill") != snakecolor:
                    self.pos[0] -= 1
                else:
                    self.finish()
            else:
                self.finish()
        elif self.dir == "right":
            if self.pos[1] < 49:
                if C.itemcget(kwad[((self.pos[0]) * 50 + self.pos[1] + 1)], "fill") != snakecolor:
                    self.pos[1] += 1
                else:
                    self.finish()
            else:
                self.finish()
        elif self.dir == "down":
            if self.pos[0] < 49:
                if C.itemcget(kwad[((self.pos[0] + 1) * 50 + self.pos[1])], "fill") != snakecolor:
                    self.pos[0] += 1
                else:
                    self.finish()
            else:
                self.finish()
        elif self.dir == "left":
            if self.pos[1] > 0:
                if C.itemcget(kwad[((self.pos[0]) * 50 + self.pos[1] - 1)], "fill") != snakecolor:
                    self.pos[1] -= 1
                else:
                    self.finish()
            else:
                self.finish()

        if C.itemcget(kwad[((self.pos[0]) * 50 + self.pos[1])], "fill") == "purple":
            self.grow()
        C.itemconfig(kwad[self.pos[0] * 50 + self.pos[1]], fill=snakecolor)
        self.waz.append(copy.deepcopy(self.pos))
        if not self.growing:
            C.itemconfig(kwad[self.waz[0][0] * 50 + self.waz[0][1]], fill=bgcolor)
            self.waz.pop(0)
        else:
            self.growing = False
            self.seed()

        if self.continu:
            self.master.after(70, self.move)

    def finish(self):
        messagebox.showinfo("Game Over", "Score: "+str(self.dlugosc))
        self.continu = False

    def turnup(self, event):
        if len(self.queue) > 0:
            if self.queue[len(self.queue) - 1] != "down":
                self.queue.append("up")
        else:
            if self.dir != "down":
                self.queue.append("up")

    def turndown(self, event):
        if len(self.queue) > 0:
            if self.queue[len(self.queue) - 1] != "up":
                self.queue.append("down")
        else:
            if self.dir != "up":
                self.queue.append("down")

    def turnright(self, event):
        if len(self.queue) > 0:
            if self.queue[len(self.queue) - 1] != "left":
                self.queue.append("right")
        else:
            if self.dir != "left":
                self.queue.append("right")

    def turnleft(self, event):
        if len(self.queue) > 0:
            if self.queue[len(self.queue) - 1] != "right":
                self.queue.append("left")
        else:
            if self.dir != "right":
                self.queue.append("left")

    def seed(self):
        pos = [random.randint(0, 49), random.randint(0, 49)]
        if C.itemcget(kwad[((pos[0]) * 50 + pos[1])], "fill") == snakecolor: self.seed()
        C.itemconfig(kwad[pos[0] * 50 + pos[1]], fill="purple")

    def grow(self):
        self.dlugosc += 1
        self.growing = True


frame = Frame(top)
frame.pack()
b = Button(frame, text="Start", command=respawn)
b1 = Button(frame, text="Exit", command=exit)
b.pack()
C.pack()
b1.pack()

top.mainloop()
