import g2d_pyodide as g2d
from actor import Arena, Actor, Point

class Stats:
    def __init__(self, max_destination):
        self._lives = 3
        self._max_destination = max_destination
        self._destinations = 0
        
    def add_lives(self, value):
        self._lives += value
        
    def remove_lives(self, value):        
        self._lives -= value
        if self._lives < 0:
            self._lives = 0
            
    def add_point_reached(self):
        self._destinations += 1 
        
        
class Frog(Actor):
    def __init__(self, pos:Point, vel, size_x, size_y, sprite_x, sprite_y):
        self._x, self._y  = pos       
        self._vel = vel
        self._size_x = size_x
        self._size_y = size_y
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        self._contact = False
       
        
    def pos(self):
        return (self._x,self._y)
                  
    def move(self, arena):     
               
        if  "ArrowUp" in g2d.current_keys():           
            self._y -= self._vel
        elif "ArrowDown" in g2d.current_keys():
            self._y += self._vel
        elif "ArrowLeft" in g2d.current_keys():
            self._x -= self._vel
        elif "ArrowRight" in g2d.current_keys():
            self._x += self._vel
           
       
                
        for other in arena.collisions():               
            if isinstance(other, CarLeft) or isinstance(other, CarRight):
                self._contact = True
                self.generate_frog()
                statistics.remove_lives(1)
            elif isinstance(other, Destination): 
                self._contact = True
                arena.spawn(Destination((other._x, other._y), 256,256))               
                arena.kill(other)               
                statistics.add_point_reached()
                self._contact = True
                self .generate_frog()           
            elif isinstance(other, Wood):  
                self._contact = True
                self._x += other._vel
            elif isinstance(other, Turtle):
                self._contact = True
                self._x -= other._vel
            else:
                self._contact = False  
                
        
       
                                                     
        if self._x < 0 - self._size_x :
            self._x = 500
        elif self._x > 500 + self._size_x:
            self._x = 0 - self._size_x
                                    
    def size(self):
        return (self._size_x, self._size_y)
          
    def sprite(self):
        current = (0,0)
        
        if   "ArrowUp" in g2d.current_keys():           
                current = (3,4)
        elif "ArrowDown" in g2d.current_keys():
                current = (160,33)
        elif "ArrowLeft" in g2d.current_keys():
                current = (98,4)
        elif "ArrowRight" in g2d.current_keys():
                current = (61,35)
           
        return current  
    
    def generate_frog(self):
        arena.kill(self)
        arena.spawn(Frog((250, 432), 31, 26, 26, 0,0))
                
                   
class CarLeft(Actor):
    def __init__(self, pos: Point, vel, size_x, size_y, sprite_x,sprite_y):       
        self._x,self._y = pos        
        self._vel = vel
        self._size_x = size_x
        self._size_y = size_y
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        
    def pos(self):
        return (self._x,self._y)
    
    def move(self, arena):     
        if self._x < 0 - self._size_x:
            self._x = 500
                            
        self._x -= self._vel
        
    def size(self):
        return (self._size_x, self._size_y)
    
    def sprite(self):
        return (self._sprite_x, self._sprite_y) 
    
class CarRight(Actor):
    def __init__(self, pos: Point, vel, size_x, size_y, sprite_x,sprite_y):       
        self._x,self._y = pos        
        self._vel = vel
        self._size_x = size_x
        self._size_y = size_y
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        
    def pos(self):
        return (self._x,self._y)
    
    def move(self, arena):     
        if self._x > 500 + self._size_x:
            self._x = 0 - self._size_x
                            
        self._x += self._vel
        
    def size(self):
        return (self._size_x, self._size_y)
    
    def sprite(self):
        return (self._sprite_x, self._sprite_y) 
        
                
class Wood(Actor):
    def __init__(self, pos: Point, vel, size_x, size_y, sprite_x, sprite_y):
        self._x, self._y = pos        
        self._vel = vel
        self._size_x = size_x
        self._size_y = size_y
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        
    def pos(self):
        return (self._x,self._y)
    
    def move(self, arena):
        if self._x > 500 + self._size_x:
            self._x = 0 - self._size_x       
        self._x += self._vel
        
    def size(self):
        return (self._size_x, self._size_y)
    
    def sprite(self):
        return (self._sprite_x, self._sprite_y)
        
class Turtle(Actor):
    def __init__(self, pos: Point, vel, size_x, size_y, sprite_x, sprite_y):
        self._start = 500
        self._x, self._y = pos        
        self._vel = vel
        self._size_x = size_x
        self._size_y = size_y
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        
        
    def pos(self):
        return (self._x,self._y)
    
    def move(self, arena):
        if self._x < 0 - self._size_x:
            self._x = 500                    
        self._x -= self._vel
        
    def size(self):
        return (self._size_x, self._size_y)
    
    def sprite(self):
        return (self._sprite_x, self._sprite_y)

class Destination(Actor):
    def __init__(self, pos: Point, sprite_x,sprite_y):
        self._x,self._y = pos
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        
    def pos(self):
        return self._x, self._y
    def move(self, arena):
        pos = self._x,self._y  
        
    def size(self):
        return 35, 40
    
    def sprite(self):
        return (self._sprite_x,self._sprite_y)

def initialization():
    global arena
    arena = Arena((500,500))
    global destinations
    destinations = 4
    global statistics
    statistics = Stats(4)
         
    #genero le macchine nell'arena
    arena.spawn(CarLeft((500, 405), 5, 30,23, 256, 4))
    arena.spawn(CarLeft((650, 405), 5, 30,23, 256, 4))
    arena.spawn(CarLeft((800, 405), 5, 30,23, 256, 4))
    
    arena.spawn(CarRight((200, 368), 7, 35,30, 190, 0))
    arena.spawn(CarRight((350, 368), 7, 35,30, 190, 0))
    arena.spawn(CarRight((450, 368), 7, 35,30, 190, 0))
    arena.spawn(CarRight((600, 368), 7, 35,30, 190, 0))
        
    arena.spawn(CarLeft((350, 335), 3, 30,30, 225, 32))
    arena.spawn(CarLeft((500, 335), 3, 30,30, 225, 32))
    arena.spawn(CarLeft((700, 335), 3, 30,30, 225, 32))
    
    arena.spawn(CarRight((200, 303), 10, 30,30, 287, 0))
    arena.spawn(CarRight((350, 303), 10, 30,30, 287, 0))
    arena.spawn(CarRight((450, 303), 10, 30,30, 287, 0))
    arena.spawn(CarRight((600, 303), 10, 30,30, 287, 0))
    
    arena.spawn(CarLeft((100, 273), 1, 65,30, 191, 67))
    arena.spawn(CarLeft((300, 273), 1, 65,30, 191, 67))
    arena.spawn(CarLeft((450, 273), 1, 65,30, 191, 67))
        
    #genero i tronchi nell'arena
    arena.spawn(Wood((100, 190), 4, 90, 20, 190, 100))
    arena.spawn(Wood((250, 190), 4, 90, 20, 190, 100))
    arena.spawn(Wood((400, 190), 4, 90, 20, 190, 100))
    
    arena.spawn(Wood((20, 160), 1, 90, 20, 190, 100))
    arena.spawn(Wood((300, 160), 1, 90, 20, 190, 100))
    
    arena.spawn(Wood((50, 100), 6, 90, 18, 190, 100))
    arena.spawn(Wood((250, 100), 6, 90, 18, 190, 100))
    arena.spawn(Wood((450, 100), 6, 90, 18, 190, 100))
    
    #genero le tartarughe nell'arena
    arena.spawn(Turtle((100, 217), 2, 90, 20, 190, 130))
    arena.spawn(Turtle((250, 217), 2, 90, 20, 190, 130))
    arena.spawn(Turtle((400, 217), 2, 90, 20, 190, 130))
    
    arena.spawn(Turtle((100, 126), 7,90, 23, 190, 130))
    arena.spawn(Turtle((250, 126), 7,90, 23, 190, 130))
    arena.spawn(Turtle((400, 126), 7,90, 23, 190, 130))
    
    #genero i punti di arrivo dell'arena
    arena.spawn(Destination((50,  50), 229,263))
    arena.spawn(Destination((170, 50), 229,263))
    arena.spawn(Destination((300, 50), 229,263))
    arena.spawn(Destination((420, 50), 229,263))
    arena.spawn(Destination((540, 50), 229,263))
    
    
    arena.spawn(Frog((250, 432), 31, 26, 26, 0,0))
    
def graphics():
    #disegno lo sfondo
    g2d.draw_image("https://tomamic.github.io/images/sprites/frogger-bg.png",(0,0), (0,0) , (500,500))
    g2d.set_color((0,0,0))
    g2d.draw_rect((0,0), (500, 30))
    g2d.draw_rect((0,460), (500, 60))
    g2d.set_color((255,255,255))
    g2d.draw_image("https://tomamic.github.io/images/sprites/frogger.png", (0, 0), (1,255), (220, 40))
    g2d.set_color((255,255,255))
    g2d.draw_text("FILIPPO MONICA", (290, 25), 15)
    for i in range(statistics._lives - 1):
           g2d.draw_image("https://tomamic.github.io/images/sprites/frogger.png", (450 + 25 * i, 475), (67, 5), (25, 25))   
            
    for actor in arena.actors():
        g2d.draw_image("https://tomamic.github.io/images/sprites/frogger.png", actor.pos(), actor.sprite() ,actor.size())
    
    
def main():
    g2d.init_canvas((500, 500))
    initialization()   
    g2d.main_loop(tick, 10)  
       
def tick():
    g2d.clear_canvas()
    
    graphics()
    
   
    if statistics._lives <= 0:
        g2d.alert("GAME OVER! YOU LOSE!")
        g2d.close_canvas()
        
    if statistics._destinations == 4:
        g2d.alert("CONGRATULATIONS! YOU WIN!")
        g2d.close_canvas()
        
    arena.tick()     
           
main()