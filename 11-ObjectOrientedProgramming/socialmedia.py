class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print('-'*30)
        print("User timeline:")
        print(self.username)
        i = 1
        for post in self.posts:
            print(f'{i}.{post}')
            i+=1
        print('-'*30)

def main():

    Johndoe = SocialMediaProfile("JohnDoe")
    Johndoe.add_post("Hello world")
    Johndoe.add_post("Had a great day at the park!")
    Johndoe.add_post("What's up, Natalie? How are you?")    
    Johndoe.display_timeline()



if __name__ == "__main__":
    main()
