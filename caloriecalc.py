class calorieCalc:
    def __init__(self):
        pass
        self.weight = float
        self.height = float
        self.age = float
        self.gender = str
        self.multiply = float

    def info(self):
        w = input("How much do you weigh in pounds?: ")
        hf = input("How tall are you? \nFeet: ")
        hi = input("Inches: ")
        a = input("How old are you?: ")
        g = input("Gender(male or female): ")
        af = input("""\na. Sedentary(little or no exercise, deskjob)
        \nb. Lightly active (light exercise/ sports 1-3 days/week)
        \nc. Moderately active (moderate exercise/ sports 6-7 days/week)
        \nd. Very active (hard exercise every day, or exercising 2 times a day
        \ne. Extra active (hard exercise 2 or more times a day)
        \nHow active are you every week?: """)
        
        vars = ["a", "b", "c", "d", "e"]
        if af not in vars:
            input("Please type option 'a', 'b', 'c', 'd', or 'e'")


        self.weight = float(w) * 0.453
        self.height = float(((float(hf) * 12.0) + float(hi))) * 2.54
        self.age = float(a)
        self.gender = g
        if af == "a":
            self.multiply = 1.2
        elif af == "b":
            self.multiply = 1.375
        elif af == "c":
            self.multiply = 1.55
        elif af == "d":
            self.multiply = 1.725
        elif af == "e":
            self.multiply = 1.9

    def bmr(self):
        bmr = float
        if self.gender == "male":
            bmr = ((10.0*self.weight) + (6.25*self.height) - (5*self.age) + 5) * self.multiply
        elif self.gender == "female":
            bmr = ((10.0*self.weight) + (6.25*self.height) - (5*self.age) - 161) * self.multiply
        bmr = round(bmr)
        print(f"""\nIf you want want to maintain your weight you should intake {bmr} calories per day
        \nIf you want to lose .5 pounds a week you should intake {bmr - 250} calories per day
        \nIf you want to lose 1 pound a week you should intake {bmr - 500} calories per day
        \nIf you want to lose 2 pounds a week you should intake {bmr - 1000} calories per day.""")

if __name__ == '__main__':
    calories_ = calorieCalc()
    calories_.info()
    calories_.bmr()
