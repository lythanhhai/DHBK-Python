class User():
    def __init__(self, id, name):
        self.id = id 
        self.name = name
        self.followers = 0
        self.following = 0

    def Print(self):
        print(f"Hello {self.id} {self.name} have {self.followers}") 

    def Following(self, user):
        user.followers += 1
        user.following += 1

user1 = User("001", "LTH")
user2 = User("002", "LTH1")

user1.Following(user2)
print(str(user1.followers))
print(str(user1.following))
print(str(user2.followers))
print(str(user2.following))
user1.Print()