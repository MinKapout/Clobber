import time

class Pion:

    def __init__(self, id, imgCase):
        self.id = str(id)+"-"+str(time.time())
        self.imgCase = imgCase

    def getImgCase(self):
        return self.imgCase

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str("u"+self.id)

