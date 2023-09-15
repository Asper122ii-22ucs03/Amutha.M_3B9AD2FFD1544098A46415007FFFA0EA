#define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")
#define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The Batsam is Batting.")
#define the derived class bowler
class Bowler(player):
    def play(self):
        print("The Bowler is Bowling.") 
#create objects of batsman and bowler classes 
batsman=Batsman()
bowler=Bowler()
#call tha play() method for each object 
batsman.play()
bowler.play()