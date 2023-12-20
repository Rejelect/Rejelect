class Talaba:
    def __init__(self, ism, familiya, tugilgan_yil):
        self.ism = ism
        self.familiya = familiya
        self.tugilgan_yil = tugilgan_yil
    
    def get_first_name(self):
        return f"Ismi: {self.ism}"

    def get_last_name(self):
        return f"Familiyasi: {self.familiya}"

    def get_fullname(self) -> str:
        return f"Ismi: {self.ism}, familyasi: {self.familiya}"
    
    def get_age(self):
        return f"Tug'ilgan sanasi: {self.tugilgan_yil}"
t = Talaba("Xamidullo", "Muratqulov", "26.08.2004")
t2 = Talaba("Axror", "Akmalov", "08.06.2005")
t3 = Talaba("Kamol", "Anvarov", "28.09.2002")
print(t.get_first_name())
print(t2.get_last_name())   
print(t2.get_age())