def check_in ():
  name_1= input('what is your first name? ')
  name_2= input('what is your last name? ')
  
  print( 'Hello'  , name_1  , name_2)
  
  print('Are you an existing patient?')
  existing_patient= input('(Y), (N): ') 
  print(existing_patient)
  if existing_patient.upper() == 'Y':
    print('Welcome back!')
  else:
    print('Welcome to our hospital.')
  print('Thank you.')

def mass ():
  weight= input('Weight: ')
  print(weight)
  units= input('(K)g, (L)bs: ')
  print(units)
  
  if units.upper() == 'K':
    converted= float(weight) * 2.205
    print('Weightin lbs: ' + str(converted))
  else:
    converted= float(weight) // 2.205 
    print('Weight in Kg: ' + str(converted))

def colour (): 
  name= input('What is your name? ')
  colour= input('What is your favourite colour? ')
  print(name, 'likes' ,colour)

def birth_year ():
  birth_year= input('Birth year: ')
  age= 2024 - int(birth_year)
  print(age)

def hot_cold ():
  temp= input('What is the temperature? ')
  if int(temp)>= 25:
    print('It is hot, have an ice cream')
  if int(temp)<=13:
    print('It is cold, have a hot chocolate')
  else:
    print('Have a lovely day')

def down_payment ():
  price= 1000000
  credit_score= input('What is your credit score? ')
  if int(credit_score)>=720:
    down_payment= price * 0.10
    print(f"Down payment: ${down_payment}")
  if int(credit_score)<720:
    down_payment= price * 0.20
    print(f"Down payment: ${down_payment}")
    
def loan ():
  has_high_income= False 
  has_good_credit= True 
  if has_high_income and has_good_credit:
    print('Eligible for loan')
  else:
    print('Not eligible for loan')

def loops ():
  i=1 
  while i <= 5:
    print('*'*i)
    i=1+i

def guessing_game ():
  secret_number=9
  guess_count=0 
  guess_limit=3
  while guess_count < guess_limit:
    guess= int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
      print('Correct, well done! ')
      break
    elif guess != secret_number:
      print(f'Wrong, you have {guess_limit -guess_count} guesses left')
  if guess_limit-guess_count == 0:
      print('You lose, better luck next time!')

def car_game ():
  command= ''
  started = False
  while True:
    command = (input('> ').lower()).strip() #strip is to allow space 
    if command == 'start':
      if started:
          print('Car is already started!')
      else:
        started = True
        print('Car started... ready to go!')
    elif command == 'stop':
      if not started:
        print('Car is already stopped')
      else:
        started = False 
        print('Car stopped')
    elif command == 'help':
      print('''
start - To start the car
stop - To stop the car 
quit - To exit
      ''')
    elif command == 'quit':
      print('Game Terminated')
      break
    else:
      print("Sorry, I didn't understand that")

def f ():
  numbers=[5,2,5,2,2]
  for x_count in numbers:
    output=''
    for count in range(x_count):
      output += 'x'
    print(output)

def l ():
  numbers=[1,1,1,4]
  for x_count in numbers:
    output=''
    for count in range(x_count):
      output += 'x'
    print(output)

def largest_number ():
  numbers=[3,6,2,8,4,10]
  max= numbers[0]
  for number in numbers:
    if number > max:
      max=number 
  print(f'largest number:{max}')

def list_methods ():
  numbers=[5,2,4,7,8,9,5,9,9,10]
  uniques=[]
  for number in numbers:
    if number not in uniques:
      uniques.append(number)
  print(uniques)

def dictionaries ():
  phone= input('Phone: ')
  print(phone)
  digits_mapping= {
    "1": "one",
    "2": "two",
    "3": "three",
    "4":"four"
}
  output= ''
  for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
  print(output)


def emoji_converter(message):
  words = message.split(' ')
  emojis={
    ':)': '😀',
    ':(': '😞',
    }
  output= ''
  for word in words:
    output += emojis.get(word, word) + '  '
  return output


  message= input('> ')
  print(emoji_converter(message))


def square(number):
  return number * number 
  print(square(5))






