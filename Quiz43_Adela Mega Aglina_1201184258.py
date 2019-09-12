ListGPA = [2.1, 2.5, 4, 3]

def Hadiah (GPA):
    Bonus = 500000
    Hadiah = GPA * Bonus
    return Hadiah

for GPA in ListGPA:
    if GPA > 2.5:
        print('Hadiah : Rp ', Hadiah (GPA))
    else:
        print('Maaf')