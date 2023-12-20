import random


class TubeLinkManager:
    def __init__(self):
        self.links = ["https://www.youtube.com/watch?v=3_R0ls2O4lg","https://www.youtube.com/watch?v=JT-yeDG7DnI","https://www.youtube.com/watch?v=1SskBRA1Naw","https://www.youtube.com/watch?v=rNFZgBrdnww","https://www.youtube.com/watch?v=n847sCViblQ","https://www.youtube.com/watch?v=3B276YO0Obs","https://www.youtube.com/watch?v=3B276YO0Obs","https://www.youtube.com/watch?v=3B276YO0Obs","https://www.youtube.com/watch?v=Wwi69pP9cIQ","https://www.youtube.com/watch?v=tghxpdPKaq4","https://www.youtube.com/watch?v=AXurFzKn3sM","https://www.youtube.com/watch?v=gE9Soduxb0E","https://www.youtube.com/watch?v=AkWUqL03w7Q","https://www.youtube.com/watch?v=QvU0DoEJ5So","https://www.youtube.com/watch?v=WBs06zCsmHU","https://www.youtube.com/watch?v=XOfJCGoDklw&t=2s","https://www.youtube.com/watch?v=rH1Lz26BcqE","https://www.youtube.com/watch?v=MdtyzHAmKRE","https://www.youtube.com/watch?v=xn7L8CC3ONE","https://www.youtube.com/watch?v=DD2Ysc9RKVw","https://www.youtube.com/watch?v=KOtSUdZWg4Y","https://www.youtube.com/watch?v=y4EAwm6LlFE","https://www.youtube.com/watch?v=W9xxzUnucHU","https://www.youtube.com/watch?v=620k5Cww83s","https://www.youtube.com/watch?v=XFCOAuwjxOw","https://www.youtube.com/watch?v=u4Vsb15Cebk","https://www.youtube.com/watch?v=v1wkx1kfRn0"]

    def get_link(self):
        return random.choice(self.links)
