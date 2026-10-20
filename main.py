from datetime import datetime


class ChatBot:
    def __init__(self):
        self.pitanja = {
            "vreme": "Vreme",
            "zdravo": "Zdravo! Kako vam mogu pomoci danas?",
            "kako si": "Odlicno sam, radim nemam bagove :D",
            "ime": "Ja sam Chatbot.",
            "pomoc": "Mozete me pitati o vremenu, mom imenu, kako sam ili reci zdravo.",
            "program": "Napravljen sam u programskom jeziku Python.",
            "cao": "Cao cao"
        }

    def pronadji_odgovor(self, poruka):
        poruka_mala = poruka.lower()

        if "vreme" in poruka_mala:
            trenutno_vreme = datetime.now().strftime("%H:%M:%S")
            trenutni_datum = datetime.now().strftime("%d.%m.%Y.")
            return f"Trenutno vreme je {trenutno_vreme}, a datum je {trenutni_datum}."

        for kljucna_rec, odgovor in self.pitanja.items():
            if kljucna_rec in poruka_mala:
                return odgovor


        return "Izvinite, nisam razumeo vase pitanje. Mozete li pokusati ponovo sa drugim recima?"

    def pokreni(self):
        print("Dobrodosli u Chatbot")
        print("Unesite 'izlaz' za prekid razgovora")

        while True:
            korisnik_unos = input("Postavite pitanje: ")

            if korisnik_unos.lower() == 'izlaz':
                print("Chatbot: Dovidjenja!")
                break


            odgovor = self.pronadji_odgovor(korisnik_unos)
            print(f"Chatbot: {odgovor}\n")

bot = ChatBot()
bot.pokreni()