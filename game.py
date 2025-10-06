import time

# Jeopardy game

# List of trivia questions:
scienceTrivia = [
    {
        'question': 'How many protons are in an atom of hydrogen?',
        'answer': 'one',
        'options': ['three', 'one', 'four']
    },
    {
        'question': 'What type of particle is the Higgs-Boson?',
        'answer': 'Boson',
        'options': ['Higgs', 'Boson', 'Bosal']
    },
    {
        'question': 'In which state is the Superconducting Super Collider (SSC) located?',
        'answer': 'Texas',
        'options': ['Texas', 'Georgia', 'New Jersey']
    },
    {
        'question': 'What do platypuses have at the back of their ankles?',
        'answer': 'Venomous gland',
        'options': ['Feet', 'Nothing in particular', 'Venomous gland']
    },
    {
        'question': 'What is the approximate value of $500 from 2021 today?',
        'answer': '$600',
        'options': ['$550', 'werg', '$600']
    }
]

historyTrivia = [
    {
        'question': 'Who was the U.S. president in 2013?',
        'answer': 'Obama',
        'options': ['Bush', 'Trump', 'Obama']
    },
    {
        'question': 'What triggered WWII?',
        'answer': 'Invasion of Poland',
        'options': ['The Great Explosion', 'Bolivian Battle', 'Invasion of Poland']
    },
    {
        'question': 'What replaced the Articles of Confederation?',
        'answer': 'Constitution',
        'options': ['Constitution', 'Bill of Rights', 'Declaration of Independence']
    },
    {
        'question': 'When did the United States enter WWI?',
        'answer': '1917',
        'options': ['1901', '1917', '1933']
    },
    {
        'question': 'When did the Bolshevik Revolution take place?',
        'answer': '1917',
        'options': ['1901', '1933', '1917']
    }
]

tvTrivia = [
    {
        'question': 'What is the show about Dexter Morgan called?',
        'answer': 'Dexter',
        'options': ['Brian', 'Dexter', 'Joe']
    },
    {
        'question': 'Who broke bad in Breaking Bad?',
        'answer': 'Walter White',
        'options': ['James Jesse', 'Jesse Pinkman', 'Walter White']
    },
    {
        'question': 'What is the motto of House Stark from GOT?',
        'answer': 'Winter is Coming',
        'options': ['Winter is Coming', 'Summer will Soon Arrive', 'Fall may Fall']
    },
    {
        'question': 'Which actor played Tony Soprano?',
        'answer': 'James Gandolfini',
        'options': ['Marlon Brando', 'Luigi Prosciutto', 'James Gandolfini']
    },
    {
        'question': 'Who created Curb Your Enthusiasm?',
        'answer': 'Larry David',
        'options': ['Harry Goldberg', 'Larry Goldstein', 'Larry David']
    }
]

geographyTrivia = [
    {
        'question': 'Where is the Burj Khalifa?',
        'answer': 'Dubai',
        'options': ['Saudi Arabia', 'Dubai', 'South Sudan']
    },
    {
        'question': 'In which country is Oslo?',
        'answer': 'Norway',
        'options': ['Sweden', 'Denmark', 'Norway']
    },
    {
        'question': 'In which country is the Stonehenge?',
        'answer': 'United Kingdom',
        'options': ['United Kingdom', 'Ireland', 'Finland']
    },
    {
        'question': 'In which city is the Stonehenge?',
        'answer': 'Salisbury',
        'options': ['Salisbury', 'Bristol', 'Birmingham']
    },
    {
        'question': 'What are the coordinates of Stonehenge?',
        'answer': '51.1789° N, 1.8262° W',
        'options': ['67.6768° N, 4.1415° W', '99.9789° N, 54.9997° W', '51.1789° N, 1.8262° W']
    }
]

pokemonTrivia = [
    {
        'question': 'What type is Pikachu?',
        'answer': 'Electric',
        'options': ['Water', 'Watt', 'Electric']
    },
    {
        'question': 'Which pokemon is canonically god?',
        'answer': 'Arceus',
        'options': ['Dialga', 'Arceus', 'Giratina']
    },
    {
        'question': 'Which pokemon type is useless?',
        'answer': 'Bug',
        'options': ['Bug', 'Bug', 'Bug']
    },
    {
        'question': 'What type is Deoxys?',
        'answer': 'Psychic',
        'options': ['Psychic', 'Normal', 'Dark']
    },
    {
        'question': 'What is the last name of the creator of the pokemon franchise?',
        'answer': 'Tajiri',
        'options': ['Kojima', 'Tajiri', 'Miyamoto']
    }
]

def play_game(seconds):
    while seconds > 0:
        score = 0
        minutes, secs = divmod(seconds, 60)
        timer_display = f"{minutes:02d}:{secs:02d}"
        choice = input('Choose a category between:\nScience, History, TV, Geography, Pokemon\n')
        if (choice == 'Science'):
            choice2 = input('\nChoose a question between 1-5\n')
            if (choice2 == '1'):
                print(scienceTrivia['question'])
                for i, option in enumerate(q['options'], 1):
                    print(f"{i}. {option}")
            
            elif (choice2 == 2):
                4
            
            elif (choice2 == 3):
                4
            
            elif (choice2 == 4):
                4
            
            elif (choice2 == 5):
                4
            
            else:
                print('Not an option')
         
        elif (choice == 'History'):
            4

        elif (choice == 'TV'):
            4

        elif (choice == 'Geography'):
            4
        
        elif (choice == 'Pokemon'):
            4
        
        else:
            print('Not an option')

        print(timer_display)
        time.sleep(1)
        seconds -= 1
        if (score == 25):
            break
    print("\nTIME'S UP!")

def main():
    print("Starting a new Trivia game...")
    name = input("Enter your name: ")
    print(f"Welcome to Jeopardy, {name}!\nIn this game you'll have a limited amount of time to complete all the questions.\nYour total score will be provided at the end.")
    input("\nEnter to start.")
    play_game(300)

main()
