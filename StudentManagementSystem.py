class lesson:
    def inputgrades(self, m, f, p):
        self.grades["midterm"]=m
        self.grades["final"]=f
        self.grades["project"]=p

    def lettergrade(self):
        a = ((self.grades["midterm"] * self.percent["midterm"]) + (self.grades["final"] * self.percent["final"]) + (self.grades["project"] * self.percent["project"]))
        if a > 90:
            return "AA"
        elif 70 < a and a < 90:
            return "BB"
        elif 50 < a and a < 70:
            return "CC"
        elif 30 < a and a < 50:
            return "DD"
        else:
            return "FF"
     
    
    def __init__(self, name):
        self.name=name
        self.grades = {"midterm":0, "final":0, "project":0}
        self.percent = {"midterm":0.3, "final":0.5, "project":0.2}


class student:
    name = ""
    surname = ""
    takenlesson = []
    
    def __init__(self, name, surname,course):
        self.name=name
        self.surname=surname
        self.takenlesson=course

def enter(st):
    for k in st.takenlesson:
        print("Enter grades for: " + k.name)
        k.inputgrades(int(input("midterm: ")),int(input("final: ")),int(input("project: ")))


def printgrades(st1):
    for m in st1.takenlesson:
        print("Grades for: " + m.name)
        print("lettergrade: " +str(m.lettergrade()))

def main():
    ogr = [student("Bora","KIŞ",[lesson("Biology"),lesson("Mathematics"),lesson("Physics"),lesson("Art"),lesson("Chemistry")]),student("Muhammed Galip","ULUDAĞ",[lesson("Biology"),lesson("Mathematics"),lesson("Physics"),lesson("Art"),lesson("Chemistry")])]
    for i in range(3):
        inputname = input("Please enter your name: ")
        inputsurname = input("Please enter your surname: ")
        for j in ogr:
            if j.name == inputname and j.surname == inputsurname:
                print("Welcome!")
                enter(j)
                printgrades(j)
    print("Please try again.")


if __name__ == "__main__":
    main()

