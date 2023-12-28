class PassException(Exception):
    def __init__(self,arg):
        self.msg=arg

class FailException(Exception):
    def __init__(self,arg):
        self.msg=arg

class ValueError(Exception):
   def __init__(self,arg):
         self.msg=arg
try:
    marks=int(input("enter you total marks: "))
except ValueError:
    print("please enter the vaild number")
if marks>=70:
    raise PassException("congrats you cleared this semester ")
elif marks <70:
    raise FailException("sorry better luck next time")