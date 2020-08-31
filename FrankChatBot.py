import re
import random
import smtplib
import os
import time

EMAIL_ADDRESS = 'publicforpython@gmail.com'
EMAIL_PASSWORD = 'Test11111'

class FrankBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop", 'return')
    random_questions = (
        "What would you like to know about Frank Li?",
        'What are something you are really curious about him?',
        'How can I introduce him better?',
        'What else can I tell you about Frank?',
    )

    def __init__(self):
        self.frankabout = {'describe_frank_intent': r'.*\s*is\s?[fF]rank.*',
                'frank_skill_intent': r'.*\s?([fF]rank(.*)?)?\s*skills?.*',
                'frank_like_hobby_intent': r'.*\s*hobb(y|ies).*',
                'frank_like_food_intent': r'.*food.*(likes?)?.*',
                'frank_work_experience': r'.*\s*(work)?.*experiences?.*',
                'frank_background_intent': r'.*\s(background|educations?).*',
                'frank_goal_intent': r'.*\s*(achieve|goals?|dreams?).*',
            }

    def greet(self):
        self.name = input('Hello there, this is Frankbot, what is your names?')
        will_help = input(f'Hi {self.name}, I\'m a Frankbot, a digital assistant for Frank Li. Shall I introduce him to you?')
        if will_help in self.negative_responses:
            print(f'Cool, have a nice day {self.name}!')
            time.sleep(3)
            return
        self.chat()

    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                send_email = input("Do you want to send a message to Frank's email? Reply:y/n")
                if send_email == 'y':
                    self.send_email()
                    time.sleep(3)
                    return True
                elif send_email == 'n':
                    print('Cool, have a wonderful day!')
                    time.sleep(3)
                    return True

    def send_email(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'Message from FrankChatBot'
            body = input('please type you message here:')

            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, 'knightofsacred@gmail.com', msg)
        print('I will let him know this meesage, in the meantime, have a nice day!')

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.frankabout.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_frank_intent':
                return self.describe_frank_intent()
            elif found_match and intent == 'frank_skill_intent':
                return self.frank_skill_intent()
            elif found_match and intent == 'frank_like_hobby_intent':
                return self.frank_like_hobby_intent()
            elif found_match and intent == 'frank_like_food_intent':
                return self.frank_like_food_intent()
            elif found_match and intent == 'frank_work_experience':
                return self.frank_experience()
            elif found_match and intent == 'frank_background_intent':
                return self.frank_background_intent()
            elif found_match and intent == 'frank_goal_intent':
                return self.frank_goal_intent()

        return self.no_match_intent()

    def describe_frank_intent(self):
        responses = ('Frank Li is currently study Electrical Engineering in UCSD, he is interested in computer related fields. He also has a fond interest in jazz saxophone, he created a jazz band (Francology) in his high school and they had 5 total performances in that year!')
        return responses

    def frank_skill_intent(self):
        responses = ('Frank knows python, html and css for programming. In other fields, he also knows Jazz saxophone, digital electronics CAD modeling')
        return responses

    def frank_like_hobby_intent(self):
        response = ('Frank likes to play saxophone, go to gym, programming, watch TV, read books (by the way he is a huge Lord of the Ring fan!), and hangout with his friends.')
        return response

    def frank_like_food_intent(self):
        response = ('Literally, he can almost eat anything you throw at him (of course human consumable food.), his really likes steaks, rice, BBQ, chick-fil-a and noodles!')
        return response

    def frank_experience(self):
        Aspin = 'Frank was able to obtain an internship at UCI during his junior year in high school, he was luckily to be working with ASPIN team where he designed a box that will contain all electrical equipments that would be mounted onto a Unmanned Aerial Vehicle to test out GPS for self-driving configuration.'
        Mcdonalds = 'Franks was able to work part-time in Mcdonalds during his junior year and senior year. His main tasks were to taking orders, making orderes in an adequate manner and offer good customer services. Through two years in Mcdonalds he learned a lot about life, overall he is quite proud of this experience!'
        JazzBand = 'In junior year, Frank was fortunate to be chosen as second Alto in Riverside City College Honor Jazz Band (tribute to Duke Ellington). He quickly leanred a lot about big band performances, learned about big band jazz standards and play Jazz with many talented young Jazz musicians. He was very glad about that experience!'
        ask_again = 'Would you like to know the other two experiences [y/n]?'
        explain = input('Frank has experience in many areas, [1] he has experience in Jazz band, [2] he worked at Mcdonalds [3] and he had an engineering internship, which one would you like to know (type 1 or 2 or 3)?')
        if explain == '1':
            print(Aspin)
            ask = input(ask_again)
            if ask == 'y':
                return self.frank_experience()
            return self.chat()

        elif explain == '2':
            print(Mcdonalds)
            ask = input(ask_again)
            if ask == 'y':
                return self.frank_experience()
            return self.chat()

        elif explain == '3':
            print(JazzBand)
            ask = input(ask_again)
            if ask == 'y':
                return self.frank_experience()
            return self.chat()

        return self.chat()


    def frank_background_intent(self):
        response = ('Frank comes from China, he lived in America for about 6 years now. He was first attended Southlands Christian School in 8th grade then move onto Diamond Bar High School. And now he is currently studying electrical engineering in UC San Diego.')
        return response


    def frank_goal_intent(self):
        response = ('Frank wishes to be able to be proficient at coding through an internship in a tech company, he also wishes to ultimately work at one of the FAANG companies once he graduated from UCSD.')
        return response


    def no_match_intent(self):
        responses = ('Sorry, I am not sure what you mean, can you say that again?', 'Sorry, I do not understand that, can you say that in a different way?' )
        return random.choice(responses)

# Create an instance of FrankBot below:
my_bot = FrankBot()
my_bot.greet()

