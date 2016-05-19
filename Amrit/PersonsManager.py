import numpy as N
import Visualizer as V
import Person as PE

class PersonsManager(object):
    sharedManager = None
    
    increasingID = 0
    
    people = []
    posts = []
    
    @staticmethod
    def createManager():
        PersonsManager.sharedManager = PersonsManager()
    
    def addPerson(self):
        person = PE.Person(PE.Position(4, N.random.randint(-2, 2)), ID=self.increasingID)
        print(person.position.x)
        
        self.people.append(person)
        self.increasingID += 1
        
        V.Visualizer.sharedVisualizer.addNode(person)
        
    def getPersonFromID(self, personID):
        for person in self.people:
            if person.ID == personID:
                return person
                
        return None
        
    def startSending(self):
        for person in self.people:
            person.createPost()
        
    def broadcastPost(self, post):
        for person in self.people:
            person.evaluatePost(post)
            
        self.posts.append(post)