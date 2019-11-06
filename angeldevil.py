import yaml

from hexapod import Hexapod_12DOF


class angeldevil():
    def __init__(self):
 
        self.my_hexapod = None
    
        # open config file
        f= open('config_12DOF.yaml')
        my_config = yaml.load(f)
        self.my_hexapod = Hexapod_12DOF(my_config)
        
    def angel_turn(self):
        choice = 0
        while choice != 1 and choice != 2:
            print("---Angels turn---")
            print("1) Do nothing")
            print("2) Go north")
            choice = input(">> ")
            choice = int(choice)
            if(choice == 1):
                print("staying still")
            elif (choice == 2):
                self.go_north()
            
            
        
    def devil_turn(self):
        print("---devils turn---")
        
    def go_north(self):
        print("going north")
        
game = angeldevil()
game.angel_turn()
game.devil_turn()
 