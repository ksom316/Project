import pickle
import datetime

class WeekPlanner:
    def __init__(self):
        self.user_details = {}
        self.user_plans = {}
        self.u_suggestions = {}
        self.result = None
        self.day = [{} for _ in range(7)]

    class User:
        def __init__(self, name, weekday, weekend, plan={}):
            self.__name = name
            self.__plan = plan
            self.__weekday = weekday
            self.__weekend = weekend

        def suggestions(self):
            if self.__weekday==1 and self.__weekend==1:
                temp={} 
                day_1 = {'Day[1]':'/  6:00 - 7:00 : 1.Start the day with a short workout to boost your energy / 8:00 - 11:30: 2.Take an online course or work on a personal project  /  13:00 - 16:00 : 3.Continue with the learning or project  /19:00 - 20:00 : 4. Reflect on your goals and achievements  /'}
                day_2 = {'Day[2]':'/  6:00 - 9:00 : 1.Go for a long hike or nature walk  /  11:00 - 13:00 : 2.Engage in some of your hobbies  /  15:00 - 17:00 : 3.Continue with creative projects.  /  7:00 - Bedtime :Relax with a movie or some music'}
                day_3 = {'Day[3]':'/  6:00 - 7:30 : 1.Start the day with a short workout to boost your energy  /  9:00 - 11:30 : 2.Work on a creative project  /  14:00 - 17:00 : 3.Continue with creative work  /  19:00 - Bedtime : 4.Share your work with family and friends and enjoy your night'}
                day_4 = {'Day[4]':'/  6:00 - 9:00 : 1.Connect with friends and family 10:30 - 13:30 : Volunteer for a local charity  /  15:00 - 17:00 : Attend a social event or meeting  /  19:00 - 20:00 : Relax and unwind'}
                day_5 = {'Day[5]':'/  6:00 - 7:30 : 1.Start with a workout session  /  8:30 - 12:00 : Watch a movie  / Explore online about topics that suit your interest  /  14:00 - 16:00 : Engage in wellness activities  /  19:00 - Bedtime : Enjoy a cozy evening at home'}
                day_6 = {'Day[6]':'/  6:00 - 10:00 :Explore a nearby town or city  /  12:00 - 14:00 : Try new foods at a local restaurants  /  16:00 - 18:00 : Experience local nightlife or cultural events'}
                day_7 = {'Day[7]':'/  6:00 - 8:30 : Plan and organize the upcoming week  /  9:00 - 11:30 : Reflect on accomplishments and set goals  /  13:00 - 16:00 : Relax and prepare for the week ahead'}
                temp=[day_1, day_2, day_3, day_4, day_5, day_6, day_7]
                return temp
            elif self.__weekday==2 and self.__weekend==1 :  
                temp = []
                count = 0
                while count<6:
                    temp.append({str(f'Day[{count+1}]'):'/  Work and attend to professional responsibilites  /'})
                    count+=1
                day_6 = {'Day[6]':'9:00 - 11:00 : Start the day with some exercise\n  12:00 - 14:00 : Work on unfinished projects  /  15:00 - 17:00 : Socialize with friends and family  /  18:00 - 20:00 : Relaxation and engaging in some hobbies'}
                day_7 = {'Day[7]':'/  9:00 - 11:00 : Engage in outdoor activity  /  11:00 - Bedtime : Enjoy the rest of the day  /'}
                temp.append(day_6, day_7)
                return temp
            
            elif self.__weekday==1 and self.__weekend==2:
                day_1 = {'Day[1]':'/  6:00 - 7:00 : 1.Start the day with a short workout to boost your energy  / 8:00 - 11:30: 2.Take an online course or work on a personal project  /  13:00 - 16:00 : 3.Continue with the learning or project  /19:00 - 20:00 : 4. Reflect on your goals and achievements  /'}
                day_2 = {'Day[2]':'/  6:00 - 9:00 : 1.Go for a long hike or nature walk  /  11:00 - 13:00 : 2.Engage in some of your hobbies  /  15:00 - 17:00 : 3.Continue with creative projects.  /  7:00 - Bedtime :Relax with a movie or some music'}
                day_3 = {'Day[3]':'/  6:00 - 7:30 : 1.Start the day with a short workout to boost your energy  /  9:00 - 11:30 : 2.Work on a creative project  /  14:00 - 17:00 : 3.Continue with creative work  /  19:00 - Bedtime : 4.Share your work with family and friends and enjoy your night'}
                day_4 = {'Day[4]':'/  6:00 - 9:00 : 1.Connect with friends and family 10:30 - 13:30 : Volunteer for a local charity  /  15:00 - 17:00 : Attend a social event or meeting  /  19:00 - 20:00 : Relax and unwind'}
                day_5 = {'Day[5]':'/  6:00 - 7:30 : 1.Start with a workout session  /  8:30 - 12:00 : Watch a movie  / Explore online about topics that suit your interest  /  14:00 - 16:00 : Engage in wellness activities  /  19:00 - Bedtime : Enjoy a cozy evening at home'}
                
                temp = [day_1, day_2, day_3, day_4, day_5]
                count = 5
                while count<7:
                    temp.append({str(f'Day[{count+1}]'):{'/  Work and attend to professional responsibilites  /'}})
                    count+=1
                return temp
                
            elif self.__weekday==2 and self.__weekend==2:
              return None

    def save_details(self):
        with open('User_details.dat', 'wb') as file:
            pickle.dump(self.user_details, file)

    def save_plans(self):
        with open('User_plans.dat', 'wb') as file:
            pickle.dump(self.user_plans, file)

    def save_suggestions(self):
        with open('suggestions.dat', 'wb') as file:
            pickle.dump(self.u_suggestions, file)

    def sign_up(self):
        while True:
            name = input("Welcome. Please enter the name you would like to use: ")
            if name in self.user_details:
                print("Sorry, that username already exists.")
            else:
                break

        while True:
            password = input("Please enter your password: ")
            password_ver = input("Please enter your password again: ")
            if password_ver == password:
                print(f"\nWelcome, {name}!")
                self.user_details[name] = password
                self.result = name  # Set the current user
                break
            else:
                print("Sorry. Passwords do not match. ", end="")

    def login(self):
        print("Welcome. ", end="")
        while True:
            name = input("Please enter your username: ")
            if name in self.user_details:
                break
            else:
                print("Sorry, username does not exist. ")

        while True:
            password = input("Please enter your password: ")
            if self.user_details[name] == password:
                print(f"\nWelcome, {name}! \n")
                self.result = name  # Set the current user
                break
            else:
                print("You entered a wrong password. ")

    def welcome(self):
        print("Week planner \n1. Log in \n2. Sign up ")
        while True:
            option = input("Option: ")

            if option.isdigit() == True:
                if option == "1":
                    self.login()
                    break
                elif option == "2":
                    self.sign_up()
                    break
            else:
                print("Please enter the corresponding number.")

    def fill(self, day_num):
        while True:
            num = input(f"How many things do you want to do on Day[{day_num}]: ")
            if num.isdigit():
                break
            else:
                print("Invalid number. ", end="")

        i = 0
        self.day[day_num - 1] = {f"Day[{day_num}]": "/  "}
        while i < int(num):
            i += 1
            start_str = input(f"Enter a starting time for activity[{i}] (format: HH:MM): ")
            stop_str = input(f"Enter an ending time for activity[{i}] (format: HH:MM): ")
            activity = input(f"Input activity[{i}]: ")

            try:
                start = datetime.strptime(start_str, "%H:%M")
                stop = datetime.strptime(stop_str, "%H:%M")
            except ValueError:
                print("Invalid time format. Please use HH:MM format.")
                continue

            self.day[day_num - 1][f"Day[{day_num}]"] += f"{start.strftime('%H:%M')} - {stop.strftime('%H:%M')} : {activity}\n"


    def view_weekplan(self):
        try:
            for plan in self.user_plans[self.result]:
                for key, value in plan.items():
                    print(f"{key}: \n {value}", "\n\n")
        except:
            print("Sorry, you have no week plan.")

    def change_daily_plan(self):
        while True:
            day_num =(input("What day's plan would you like to change: "))
            if day_num.isdigit() and int(day_num)>0 and int(day_num)<8:
                self.fill(day_num)
                return self.day
            else:
                print("Please enter the corresponding day number.")
        

    def create_weekplan(self):
        for day_num in range(1, 8):
            self.fill(day_num)
        return self.day

    def delete(self):
        print("\n\nAre you sure you want to delete your account? \n1. Yes \n2. No")
        while True:
            option = input("Option: ")
            if option == "1":
                del self.user_plans[self.result]
                del self.user_details[self.result]
                try:
                    del self.u_suggestions[self.result]
                except:
                    pass
                self.result = None
                break
            elif option == "2":
                break
            else:
                print("Please enter the corresponding number: ")

        print("Account successfully deleted")

    def change_weekplan(self):
        for day_num in range(1, 8):
            if not self.user_plans[self.result]:
                self.fill(day_num)
            else:
                print(f"Do you want to overwrite the current plan for Day[{day_num}] \n1. Yes \n2. No ")
                option = input("Option: ")
                while option not in ("1", "2"):
                    print("Invalid option.")
                    option = input("Option: ")
                if option == "1":
                    self.fill(day_num)
        return self.day

    def suggestions(self):
        try:
            for plan in self.u_suggestions[self.result]:
                print(plan, "\n\n")
        except:
            print("You don't have any suggestions. Do you want to create one? \n1. Yes \n2. No")
            choice = input("Option: ")
            while choice not in ("1", "2"):
                choice = input("Option: ")
            if choice == "1":
                print("\nAre you busy on weekdays? \n1. Yes \n2. No")
                weekday = input("Option: ")
                print("\nAre you busy on weekends? \n1. Yes \n2. No")
                weekend = input("Option: ")

                user = self.User(self.result, int(weekday), int(weekend), self.user_plans[self.result])
                suggestion = user.suggestions()
                self.u_suggestions[self.result] = suggestion
                if suggestion is None:
                    print("Sorry, there's no suggestion for you because you have a very busy week schedule. Remember to take short breaks.")
                else:
                    print("Here's a week suggestion for you.")
                    for days in suggestion:
                        for key, value in days.items():
                            print(f"{key}: {value}", "\n\n")

                    print("\nWould you like to use this plan? \n1. Yes \n2. No")
                    option = input("Option: ")
                    while option not in ("1", "2"):
                        print("Invalid option.")
                        option = input("Option: ")

                    if option == "1":
                        self.user_plans[self.result] = suggestion
                        print("Week plan successfully changed")

    def run(self):
        try:
            with open('User_details.dat', 'rb') as file:
                self.user_details = pickle.load(file)
        except:
            pass

        try:
            with open('User_plans.dat', 'rb') as file:
                self.user_plans = pickle.load(file)
        except:
            pass

        try:
            with open('suggestions.dat', 'rb') as file:
                self.u_suggestions = pickle.load(file)
        except:
            pass

        self.welcome()

        while self.result:
            print("\nWhat would you like to do? \n1. Create a week plan \n2. Create a plan for a specific day \n3. Change week plan \n4. View week plan \n5. View suggestion \n6. Delete Account \n7. Log out")
            option = input("Option: ")
            if option.isdigit():
                if option == "1":
                    self.user_plans[self.result] = ''
                    if len(self.user_plans[self.result]) == 0:
                        self.user_plans[self.result] = self.create_weekplan()
                        self.save_plans()
                elif option == "2":
                    self.user_plans[self.result] = self.change_daily_plan()
                    self.save_plans()
                elif option == "3":
                    self.user_plans[self.result] = self.change_weekplan()
                    self.save_plans()
                elif option == "4":
                    self.view_weekplan()
                elif option == "5":
                    self.suggestions()
                    self.save_suggestions()
                elif option == "6":
                    self.delete()
                elif option == "7":
                    self.save_details()
                    self.save_plans()
                    self.save_suggestions()
                    self.result = None

if __name__ == "__main__":
    week_planner = WeekPlanner()
    week_planner.run()
