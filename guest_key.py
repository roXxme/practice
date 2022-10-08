#'''function to reverse string'''
#def cap(revs):
#    rev= list(reversed(revs))
#    i = ""
#    for r in rev:
#        i = i+r
#    print(revs,":",i.capitalize())
#cap("Verse")


#guest= {'John':'A011', 'Kyle':'A009', 'Jake':'BQ02'}
# class which allocate keys to guest
class Guest():   
    guest= {'John':'A011', 'Kyle':'A009', 'Jake':'BQ02'}
    kys = ['A010','A012','A014','BQ01']

    def __init__(self, gname):
        self.name = (gname.lower()).capitalize()
        self.regs = self.name in self.guest
        
    def is_regd(self):
        if self.regs:
            print('Registered')
        else:
            print('Not Registered')
                
    def get_key(self):
        if self.regs:
                print(self.guest[self.name])
        else:
            print('Not registered')

    def reg(self):
        
        if len(self.kys):
            self.guest[self.name] = self.kys[0]
            self.kys.pop(0)
            self.regs = True
        else:
            print('Sorry, no vacant rooms available')

for g_name in ['Josh', 'Hans', 'Evan', 'Kyle', 'Ted', 'Karl', 'Sam']:
    guest = Guest(g_name)
    print(guest.name)
    guest.is_regd()
    if guest.regs:
        guest.get_key()
    else:
        guest.reg()
        guest.get_key()

