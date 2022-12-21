class user:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
    def __repr__(self):
        return "user(username : '{}' , name : '{}' ,email: '{}')".format(self.username,self.name,self.email)
user1=user("chandu11feb","chandu","chandu11feb@gmail.com")
print(user1)
class userdatabase:
    def __init__(self):
        self.users=[]
    def insert(self,user):
        i=0
        while i<len(self.users):
            if self.users[i].username>user.username:
                break
            i+=1
        self.users.insert(i,user)
        return "Inserted Successfully"
    def find (self,username):
        i=0
        while i < len(self.users):
            if self.users[i].username==username:
                return self.users[i]
            i+=1
    def update(self,user):
        target=self.find(user.username)
        target.name=user.name
        target.email=user.email
        return "Updated Successfully"
    def listall(self):
        print(*self.users,sep="\n")
        return self.users
chandu= user("chandu11feb","chandu","chandu11feb@gmail.com")
jaya=user("jayaroyal","jaya krishna","jayakrishna@gmail.com")
jash=user("jashtags","jashwanth","jash0123@gmail.com")
database=userdatabase()
print(database.insert(chandu))
print(database.listall())
print(database.insert(jaya))
print(database.insert(jash))
print(database.find("jashtags"))
print(database.listall())
print(database.update(user("jashtags","jash tanukonda","jash112321313@gmail.com")))
print(database.listall())