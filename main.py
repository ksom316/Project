import pickle
import datetime
import sys
import time

class WeekPlanner:
    def __init__(self):
        self.user_details = {}
        self.user_plans = {}
        self.u_suggestions = {}
        self.result = None
        self.day =  [{} for _ in range(7)]
    class User:
        def __init__(self, weekday, weekend):
            self.__weekday = weekday
            self.__weekend = weekend

        def suggestions(self):
            if self.__weekday==2 and self.__weekend==2:
                #USER SUGGESTIONS
                temp=[] 
                day_1 = {'Day[1]':' \n6:00 - 7:00 : 1.Start the day with a short workout to boost your energy \n8:00 - 11:30: 2.Take an online course or work on a personal project \n13:00 - 16:00 : 3.Continue with the learning or project  \n19:00 - 20:00 : 4. Reflect on your goals and achievements'}
                day_2 = {'Day[2]':' \n6:00 - 9:00 : 1.Go for a long hike or nature walk  \n11:00 - 13:00 : 2.Engage in some of your hobbies  \n15:00 - 17:00 : 3.Continue with creative projects.  \n7:00 - Bedtime :Relax with a movie or some music'}
                day_3 = {'Day[3]':' \n6:00 - 7:30 : 1.Start the day with a short workout to boost your energy  \n9:00 - 11:30 : 2.Work on a creative project  \n14:00 - 17:00 : 3.Continue with creative work  \n19:00 - Bedtime : 4.Share your work with family and friends and enjoy your night'}
                day_4 = {'Day[4]':' \n6:00 - 9:00 : 1.Connect with friends and family \n10:30 - 13:30 : 2.Volunteer for a local charity  \n15:00 - 17:00 : 3.Attend a social event or meeting  \n19:00 - 20:00 : 4.Relax and unwind'}
                day_5 = {'Day[5]':' \n6:00 - 7:30 : 1.Start with a workout session  \n8:30 - 12:00 : Watch a movie  / Explore online about topics that suit your interest  \n14:00 - 16:00 : Engage in wellness activities  \n19:00 - Bedtime : Enjoy a cozy evening at home'}
                day_6 = {'Day[6]':' \n6:00 - 10:00 :Explore a nearby town or city   \n12:00 - 14:00 : Try new foods at a local restaurants  \n16:00 - 18:00 : Experience local nightlife or cultural events'}
                day_7 = {'Day[7]':' \n6:00 - 8:30 : Plan and organize the upcoming week  \n9:00 - 11:30 : Reflect on accomplishments and set goals  \n13:00 - 16:00 : Relax and prepare for the week ahead'}
                temp=[day_1, day_2, day_3, day_4, day_5, day_6, day_7]
                return temp
            elif self.__weekday==1 and self.__weekend==2 :  
                temp = []
                count = 0
                while count<5:
                    temp.append({str(f'Day[{count+1}]'):'\nWork and attend to professional responsibilites\n'})
                    count+=1
                day_6 = {'Day[6]':'\n9:00 - 11:00 : Start the day with some exercise \n12:00 - 14:00 : Work on unfinished projects  \n15:00 - 17:00 : Socialize with friends and family  \n18:00 - 20:00 : Relaxation and engaging in some hobbies'}
                day_7 = {'Day[7]':'\n9:00 - 11:00 : Engage in outdoor activity  \n11:00 - Bedtime : Enjoy the rest of the day'}
                temp.append(day_6)
                temp.append(day_7)
                return temp
            
            elif self.__weekday==2 and self.__weekend==1:
                day_1 = {'Day[1]':'\n6:00 - 7:00 : 1.Start the day with a short workout to boost your energy  \n8:00 - 11:30: 2.Take an online course or work on a personal project  \n13:00 - 16:00 : 3.Continue with the learning or project  \n19:00 - 20:00 : 4. Reflect on your goals and achievements'}
                day_2 = {'Day[2]':'\n6:00 - 9:00 : 1.Go for a long hike or nature walk  \n11:00 - 13:00 : 2.Engage in some of your hobbies  \n15:00 - 17:00 : 3.Continue with creative projects.  \n7:00 - Bedtime :Relax with a movie or some music'}
                day_3 = {'Day[3]':'\n6:00 - 7:30 : 1.Start the day with a short workout to boost your energy  \n9:00 - 11:30 : 2.Work on a creative project  \n14:00 - 17:00 : 3.Continue with creative work  \n19:00 - Bedtime : 4.Share your work with family and friends and enjoy your night'}
                day_4 = {'Day[4]':'\n6:00 - 9:00 : 1.Connect with friends and family \n10:30 - 13:30 : Volunteer for a local charity  \n15:00 - 17:00 : Attend a social event or meeting  \n19:00 - 20:00 : Relax and unwind'}
                day_5 = {'Day[5]':'\n6:00 - 7:30 : 1.Start with a workout session  \n8:30 - 12:00 : Watch a movie  / Explore online about topics that suit your interest  \n14:00 - 16:00 : Engage in wellness activities  \n19:00 - Bedtime : Enjoy a cozy evening at home'}
                
                temp = [day_1, day_2, day_3, day_4, day_5]
                count = 5
                while count<7:
                    temp.append({str(f'Day[{count+1}]'):'\nWork and attend to professional responsibilites\n'})
                    count+=1
                return temp
                
            elif self.__weekday==1 and self.__weekend==1:
              return None
# FUNCTIONS FOR SAVING THE USER'S DETAILS
    def save_details(self):
        with open('User_details.dat', 'wb') as file:
            pickle.dump(self.user_details, file)

    def save_plans(self):
        with open('User_plans.dat', 'wb') as file:
            pickle.dump(self.user_plans, file)

    def save_suggestions(self):
        with open('suggestions.dat', 'wb') as file:
            pickle.dump(self.u_suggestions, file)
# SIGN UP FUNCTION
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
                self.save_details()
                self.result = name  # Set the current user
                break
            else:
                print("Sorry. Passwords do not match. ", end="")
# LOGIN FUNCTION
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
# WELCOME FUNCTION(COMBINATION OF LOG IN ANDD SIGN UP FUNCTIONS)
    def welcome(self):
        print('''             
                                       _                _                             
                                      | |              | |                            
                    __      _____  ___| | __      _ __ | | __ _ _ __  _ __   ___ _ __ 
                    \ \ /\ / / _ \/ _ \ |/ /     | '_ \| |/ _` | '_ \| '_ \ / _ \ '__|
                     \ V  V /  __/  __/   <      | |_) | | (_| | | | | | | |  __/ |   
                      \_/\_/ \___|\___|_|\_\     | .__/|_|\__,_|_| |_|_| |_|\___|_|   
                                                 | |                                  
                                                 |_|                                  ''')
        print("1. LOG IN \n2. SIGN UP ")
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
                    print("Please enter 1 or 2")
            else:
                print("Please enter the corresponding number.")
# VIEW  A SPECIFIC DAY'S PLAN FUNCTION         
    def view_day(self):
      while True:
       print("What day's plan will you like to view?")
       option = input("Option: ")
       if option.isdigit() and int(option)<8 and int(option)>0:
          try: 
           print(self.user_plans[self.result][int(option)-1][f"Day[{option}]"])
           break
          except:
           print(f"Sorry you have no plan for Day[{option}]")
           break
       else:
           print("Enter a valid day number.\n")
# FUNCTION FOR VIEWING THE PLAN OF THE CURRENT DAY
    def today(self):
        try:
            plan = self.user_plans[self.result][(datetime.datetime.today().isoweekday())-1][f"Day[{(datetime.datetime.today().isoweekday())}]"]
            if plan == "":
                print("Sorry. You have no plan for today")
            else:
                print(plan)
        except:
            print("Sorry. You have no plan for today. ")
# FUNCTION FOR MANAGING THE PLAN OF A DAY   
    def fill(self, day_num):
        while True:
            num = input(f"How many things do you want to do on Day[{day_num}]: ")
            if num.isdigit():
                num = int(num)
                break
            else:
                print("Invalid number. ", end="")

        i = 0
        self.day[int(day_num) - 1][f"Day[{day_num}]"] = " " 
        if num>0:
         for i in range(1, num + 1):
            while True:
                try:
                    start_str = datetime.datetime.strptime(input(f"Enter a starting time for activity[{i}] (format: HH:MM): "), "%H:%M")
                    stop_str = datetime.datetime.strptime(input(f"Enter an ending time for activity[{i}] (format: HH:MM): "), "%H:%M")
                    if start_str>stop_str:
                        print("Ending time cannot be before starting time", "\n")
                        continue
                    activity = input(f"Input activity[{i}]: ")
                    print("")
                    self.day[int(day_num) - 1][f"Day[{day_num}]"] += f" {start_str.strftime('%H:%M')} - {stop_str.strftime('%H:%M')} : {activity}\n"
                    break
                except ValueError:
                    print("Invalid time format. Please use HH:MM format.")
                    continue
        else:
           self.day[int(day_num) - 1][f"Day[{day_num}]"] = " " 
# FUNCTION FOR VIEWING WEEK PLAN
    def view_weekplan(self):
        try:
            count=0
            sum=0
            while count < 7:
                sum += len(self.user_plans[self.result][count][f"Day[{count+1}]"])
                count += 1
            if sum > 7:
                for plan in self.user_plans[self.result]:
                    for key, value in plan.items():
                        print(f"{key}: \n {value}", "\n")
            else:
                print("Sorry, you have no week plan. ")
        except:
            print("Sorry, you have no week plan ")
 
# FUNCTION FOR CHANGING A PLAN FOR A SPECIFIC DAY
    def change_daily_plan(self):
        while True:
            day_num =(input("What day would you like to create a plan for : "))
            if day_num.isdigit() and int(day_num)>0 and int(day_num)<8:
                self.fill(day_num)
                return self.day
            else:
                print("Please enter the corresponding day number.")
# LOADS THE SAVED DETAILS OF VARIOUS USERS
    def load(self):
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
# LOADING BAR
    def loading(self, iterations, total, length=50):
        progress = iterations / total
        arrow = '=' * int(length * progress)
        spaces = ' ' * (length - len(arrow))
        sys.stdout.write(f"\r[{arrow }{spaces}] {int(progress * 100)}%")
        sys.stdout.flush()        
# EXIT FUNCTION
    def exit(self):
        for _ in range(3):
            for frame in ["|", "/", "-", "\\"]:
                sys.stdout.write("\rExiting the program " + frame)
                sys.stdout.flush()
                time.sleep(0.2)
        print("\nGoodbye! Have a great a day! ")
        
# FUNCTION FOR CREATING A WEEK PLAN
    def create_weekplan(self):
        for day_num in range(1, 8):
            self.fill(day_num)
        for i in range (100):
                    self.loading(i+1, 100)
                    time.sleep(0.01)
        print("")
        print("New weekplan created successfully\n")
        return self.day
# FUNCTION FOR DELETING USER ACCOUNT AND OTHER DETAILS
    def delete(self):
        print("\n\nAre you sure you want to delete your account? \n1. Yes \n2. No")
        while True:
            option = input("Option: ")
            if option == "1":
                del self.user_details[self.result]
                try:
                     del self.user_plans[self.result]
                except:
                    pass
                try:
                    del self.u_suggestions[self.result]
                except:
                    pass
                self.result = None
                for i in range (100):
                 self.loading(i+1, 100)
                 time.sleep(0.01)
                print("")
                print("Account successfully deleted")
                break
            elif option == "2":
                break
            else:
                print("Please enter the corresponding number: ")
# FUNCTION FOR ERASING ALL PLANS OF THE USER
    def clear(self):
        print("\n\nAre you sure you want to erase all plans and suggestions? \n1. Yes \n2. No")
        while True:
            option = input("Option: ")
            if option == "1":
                try:
                 del self.user_plans[self.result]
                except:
                    pass
                try:
                    del self.u_suggestions[self.result]
                except:
                    pass
                for i in range (100):
                 self.loading(i+1, 100)
                 time.sleep(0.01)
                print("")
                print("All existing plans and suggestions have been deleted successfully. You currently have no week plan. ")
                break
            elif option == "2":
                break
            else:
                print("Please enter the corresponding number: ")
                
# FUNCTION FOR CHANGING THE CURRENT WEEKPLAN
    def change_weekplan(self):
        try:
            count=0
            sum=0
            while count < 7:
                sum += len(self.user_plans[self.result][count][f"Day[{count+1}]"])
                count += 1
                if sum > 7:
                    for day_num in range(1, 8):
                        if self.user_plans[self.result][day_num-1]:
                            self.fill(day_num)
                    for i in range (100):
                     self.loading(i+1, 100)
                     time.sleep(0.01)
                    print("")
                    print("New weekplan created successfully\n")
                    return self.day
                else:
                    print("You don't have any weekplan")
                    return self.day
        except:
            print("You don't have any weekplan")
# FUNCTION FOR CREATING A WEEK PLAN SUGGESTION FOR THE CURRENT USER  
    def suggestions(self):
        try:
            for plan in self.u_suggestions[self.result]:
                for key, value in plan.items(): 
                 print(f"{key}: {value}", "\n\n")
        except:
            print("\nYou don't have any suggestions. Do you want to create one? \n1. Yes \n2. No")
            choice = input("Option: ")
            while choice not in ("1", "2"):
                choice = input("Option: ")
            if choice == "1":
                print("\nAre you busy on weekdays? \n1. Yes \n2. No")
                weekday = input("Option: ")
                print("\nAre you busy on weekends? \n1. Yes \n2. No")
                weekend = input("Option: ")

                user = self.User(int(weekday), int(weekend))
                self.save_suggestions()
                suggestion = user.suggestions()
                self.u_suggestions[self.result] = suggestion
                for i in range (100):
                 self.loading(i+1, 100)
                 time.sleep(0.01)
                print("")
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
                        for i in range (100):
                          self.loading(i+1, 100)
                          time.sleep(0.01)
                          print("")
                          print("Week plan successfully changed")
                    elif option == "2":
                        pass
# USER OPTIONS
    def options(self):
            while self.result:
                print("\nWhat would you like to do? \n1. Create a week plan \n2. Manage a plan for a specific day \n3. Change week plan \n4. View week plan \n5. View suggestion \n6. View today's plan \n7. View a specific day's plan \n8. Clear all plans and suggestions \n9. Delete account \n10. Exit ")
                option = input("Option: ")
                if option.isdigit():
                    if option == "1":
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
                        self.today()
                    elif option == "7":
                       self.view_day()
                    elif option == "8":
                        self.clear()
                        self.save_plans()
                        self.save_suggestions()
                    elif option == "9":
                        self.delete()
                        self.save_details()
                        self.save_plans()
                        self.save_suggestions()
                        self.result = None  
                    elif option == "10":
                        self.save_details()
                        self.save_plans()
                        self.save_suggestions()
                        self.result = None      
                    else:
                        print("Enter a number that corresponds to one of the options. ")
                else: 
                    print("Please enter a number. ")
            self.exit()   
            return self  
# FUNCTION FOR RUNNING THE PROGRAM 
    def run(self):
        self.load()
        self.welcome()  
        for i in range (100):
                self.loading(i+1, 100)
                time.sleep(0.01)
        print("")               
        self.options()
# MAIN FUNCTION
if __name__ == "__main__":
    week_planner = WeekPlanner()
    week_planner.run()
