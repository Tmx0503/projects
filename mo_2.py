
studs = {"afganisztan", "balazs", "cica"}


stud = input("enter stud name")

if stud in studs:
    print("good job")
else:
    print("delete sys")



grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}") #Az adat előszedése: A valódi munka a {grades[student]} résznél történik. A szögletes zárójel a "keresés" parancs. Ezzel azt mondod a gépnek: "Nyisd ki a grades telefonkönyvet, keresd meg benne a megadott nevet (Sandy), és ne a nevet, hanem a mellé mentett adatot add ide".
else:
    print("dumb")

email = "BroCodegmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
