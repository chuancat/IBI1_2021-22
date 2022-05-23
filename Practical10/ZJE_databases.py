class Staff(object):
    def __init__(self,fn,ln,l,r):
       # set attributes
       self.firstname=fn
       self.lastname=ln
       self.location=l
       self.role=r
    def databases(self):
       name=self.firstname+' '+self.lastname
       print('full name:',name +',' + 'location:',self.location + ',' + 'role:',self.role)
example=Staff('Robert','Young','Edinburgh','faculty')
example.databases()
