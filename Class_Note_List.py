class Student_Notes:

    def __init__(self):
        pass


    def Student_Information(self):
        self.name = str(input("Enter the name: "))
        self.surname = str(input("Enter the surname: "))
        self.note1 = int(input("Enter the Note1: "))
        self.note2 = int(input("Enter the Note2: "))
        self.note3 = int(input("Enter the Note3: "))
      
        with open("Student_Notes.txt", "a", encoding="utf-8") as file: 
            file.write(f"{self.name},{self.surname},{self.note1},{self.note2},{self.note3} \n")
            print("Student added to document.")



    def Average_Calculate(self, satır):
        satır = satır[:-1]
        liste = satır.split(",")
        name = liste[0]
        surname= liste[1]
        note1 = int(liste[2])
        note2 = int(liste[3])
        note3 = int(liste[4])

        TotalNote = note1*(0.3) + note2*(0.3) + note3*(0.4)

        if(TotalNote <= 100 and TotalNote >= 90):
            harf = "AA"
        elif(TotalNote < 90 and TotalNote >= 80):
            harf= "BA"
        elif(TotalNote <80 and TotalNote >= 70):
            harf= "BB"
        elif(TotalNote < 70 and TotalNote >= 60):
            harf= "CB"
        elif(TotalNote < 60 and TotalNote >=50):
            harf ="CC"
        else:
            harf= "FF"

        return name + surname +"--------------->"+ harf+"\n"



    def Information_Reading(self):

        with open("Student_Notes.txt","r",encoding="utf-8") as file:

            for satır in file:
                print(self.Average_Calculate(satır))


    def Save_Notes(self):
        with open("Student_Notes.txt","r",encoding="utf-8") as file:
            liste = []
            for i in file:

                liste.append(self.Average_Calculate(i))


        with open("Results.txt","w",encoding="utf-8") as file2:

            for i in liste:
                file2.write(i)         


    def Saved_Reading(self):
        with open("Results.txt","r",encoding="utf-8") as file3:

            for i in file3:
                print(i)


while(True):
    student = Student_Notes()

    print("""
    ******************************
    1-Note gir 
    2-Notları Oku
    3- Notları kaydet
    4- Kayıtları Oku
    5- Çıkış
    *******************************
    """)

    
    choose = input("Enter the choose:")

    if(choose == "1"):
        student.Student_Information()
    elif(choose =="2"):
        student.Information_Reading()
    elif(choose =="3"):
        student.Save_Notes()
    elif(choose == "4"):
        student.Saved_Reading()
    elif(choose == "5"):
        print("EXİT......")
    else:
        print("Try again, you wrong choose")