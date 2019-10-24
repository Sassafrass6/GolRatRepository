import numpy as np
from time import sleep
import sys

if sys.version_info[0] < 3:
  from Tkinter import *
else:
  from tkinter import *    

class GR_Anim ( object ):
  def __init__ ( self, w=800, ca=0., da=1.618, r=375, dr=.25, dt=.01 ):

    self.r = r
    self.dt = dt
    self.da = da*2*np.pi
    self.dr = dr
    self.dotR = 3
    self.center = w//2

    self.ca = ca
    self.cr = 2*self.dotR

    self.root = Tk()
    self.root.title('Evolving Golden Ratio')
    self.canvas = Canvas(self.root, width=w, height=w)

    x1 = self.center - r
    x2 = self.center + r 
    self.canvas.create_oval(x1,x1,x2,x2,outline='black',fill='')

    self.cur_pos = self.get_coords()
    self.objs = self.fill_region(self.cur_pos)
    self.canvas.pack()
    
    self.root.after(0, self.animation)
    self.root.mainloop()

  def animation ( self ):
    try:
      while True:
        self.da += 0.0001
        new_pos = self.get_coords()
        dPos = new_pos - self.cur_pos
        self.cur_pos = new_pos
        for i in range(len(self.objs)):
          self.canvas.move(self.objs[i],dPos[i,0],dPos[i,1])
        self.canvas.update()
        sleep(self.dt)
        continue

      while True:
        continue
    except Exception as e:
      print(e)
      quit()

  def place_circle ( self, cx, cy, r, o='', f='black' ):
    x1 = self.center + cx - r
    x2 = self.center + cy - r
    y1 = self.center + cx + r
    y2 = self.center + cy + r
    return self.canvas.create_oval(x1,x2,y1,y2,outline=o,fill=f)

  def fill_region ( self, pos ):
    return [self.place_circle(p[0], p[1], self.dotR) for p in pos]

  def get_coords ( self ):
    pos = []
    c = self.cr
    a = self.ca
    while c < self.r:
      cx = c * np.cos(a)
      cy = c * np.sin(a)
      c += self.dr
      a += self.da
      pos.append([cx,cy])
    return np.array(pos)

if __name__ == '__main__':
  argc = len(sys.argv)
  if argc == 1:
    GR_Anim()
  if argc == 2:
    try:
      GR_Anim(da=float(sys.argv[1]))
    except:
      raise ValueError('Bad Float')
  else:
    print('Usage:\n\tpython GR_Anim.py\n\tpython GR_Anim.py {winding number}')
    quit()
