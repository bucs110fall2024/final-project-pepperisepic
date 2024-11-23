import rock
import impala
import cloud

class Controller:
  
  def __init__(self):
   
      self.state = "START"
    
  def mainloop(self):
    while True:
        if self.state == "GAME":
           self.gameloop()
        elif self.state = "END":
           self.endloop()
        elif self.state == "START":
           self.startloop()
           
           
           # 2 detect collisions and update models
           enemies = pygame.sprite.spritecollide(self.Impala, self.Rocks, False)
           for enemies in enemies: 
               #handle collision
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
