class lesson:
    grades = {
        "midterm":0, "final":0, "project":0
    }
    percent = {
        "midterm":0.3, "final":0.5, "project":0.2
    }

    def entermid(self, mid):
        self.grades["midterm"] = mid
    def enterfinal(self, final):
        self.grades["final"] = final
    def entermid(self, pro):
        self.grades["project"] = pro

    def lettergrade(self):
        a = ((self.grades["midterm"] * self.percent["midterm"]) + (self.grades["final"] * self.percent["final"]) + (self.grades["project"] * self.percent["project"])) / 3
        if a > 90:
            return "AA"
        elif 70 < a < 90:
            return "BB"
        elif 50 < a < 70:
            return "CC"
        elif 30 < a < 50:
            return "DD"
        else:
            return "FF"
     
    
    def __init__(self, name):
        self.name=name


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
        k.entermid(int(input("Please enter midterm grades...")))
        k.enterfinal(int(input("Please enter final grades...")))
        k.enterproject(int(input("Please enter project grades...")))


def printgrades(st):
    for k in st.takenlesson:
        print("Grades for: " + k.name)
        print(k.name + "midterm: " + k["midterm"])
        print(k.name + "final: " + k["final"])
        print(k.name + "project: " + k["project"])
        print("lettergrade: " + k.lettergrade)

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
            


    







