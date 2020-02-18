class student:
    def __init__(self, name, age, __class):
        self.name = name
        self.age = age
        self.__class = __class
    def av_score(self,sc1, sc2, sc3):
        avscore = ((sc1+sc2+sc3)/3)
        return avscore
        
John = student("John", "21", "Pink")
print(John.av_score(21, 54, 10))

print(getattr(John, "age"))