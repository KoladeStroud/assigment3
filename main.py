
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score
    def change_name(self,newName):
        self.newName= newName
        print("Name: " + newName)
        
    def change_age(self,newAge):
        self.newAge = newAge
        print("Age: " + str(newAge))
        
    def add_track(self,newTracks):
        self.newTracks= newTracks
        print("Track: " + newTracks)
        
    def get_score(self):
        
        print("Score :" + str(self.score))
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods



Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

