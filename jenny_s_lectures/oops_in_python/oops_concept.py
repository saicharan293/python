# self is an object reference that will bind to the object
# which is created during the flow of programs
class Instructor:
    followers=0
    def __init__(self,ins_name,ins_sub):
        self.name=ins_name
        self.sub=ins_sub
        # self.followers=0
        print("creating a new object")
    def display(self,sub):
        print("hi I am",self.name,'and I teach',sub)
    def update_followers(self,follower_name):
        self.followers+=1
ins_1=Instructor('sai','Kurnool')
print(ins_1.name)
ins_1.display('python')
ins_1.update_followers('jenny')
print(ins_1.name,'follower count',ins_1.followers)
ins_2=Instructor('charan','hyderabad')
ins_2.update_followers('kendra')
print(ins_2.name,'followers count',ins_2.followers)