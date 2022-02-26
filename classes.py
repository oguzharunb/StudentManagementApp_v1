import repo as rp


class Student():
    def __init__(self,name,branch):
        self.Name = name
        self.Branch = branch
        self.ID = rp.Idcounter
        rp.Idcounter += 1
