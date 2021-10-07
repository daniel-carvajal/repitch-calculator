# Program make a simple calculator



noteToFreq =  {
  "F#3": 185.00,
  "G3": 196.00,
  "G#3": 207.65,
  "A3": 220.00,
  "A#3": 233.08,
  "B3": 246.94,

  "C4": 261.63,
  "C#4" : 277.18,
  "D4" : 293.66,
  "D#4" : 311.13,
  "E4" : 329.63,
  "F4" : 349.23,
  "F#4" :  369.99,
  "G4" : 392.00,
  "G#4" : 415.30,
  "A4" : 440.00,
  "A#4" : 466.16,
  "B4" : 493.88,
  "C5": 523.25,

  "C#5": 554.37,
  "D5": 587.33,
  "D#5": 622.25,
  "E5": 659.25,
  "F5": 698.46,
  "F#5": 739.99,
}

noteOrder = [
"F#3", "G3", "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5","F5","F#5",
 ]


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


# print("Select operation.")
# print("1.Pitch percent calculator")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

while True:
    # Take input from the user
    # choice = str(input("Enter choice(1/2/3/4): "))

    # Check if choice is one of the four options
    # if choice in ('1', '2', '3', '4'):
    # if (origNote+'4') in noteOrder:

    if True:

        # num1 = float(input("Enter Original key: "))
        origNote = (input("Enter Original key (using sharps e.g. 'G#') ")).upper()

        # num2 = float(input("Enter desired pitch amount (in semitones, e.g. '+3'): "))
        # interval = input("Enter desired pitch amount (between -6 and 6, in semitones, e.g. '-3'): ")


        # if True:
        if (origNote+'4') in noteOrder:
            interval = input("Enter desired pitch amount (between -6 and 6, in semitones, e.g. '-3'): ")
            if (int(interval) <= 6 and int(interval) >=-6 ):
            # print(num1, "+", num2, "=", add(num1, num2))
            # print(origKey, ' ' ,interval)
            # print(noteToFreq[origKey+'4'], ' ' ,interval)
                originalFrequency = noteToFreq[origNote+'4']
                index = noteOrder.index(origNote+'4')
                newNoteIndex = int(index) + int(interval)
                newNote = noteOrder[newNoteIndex]

                newNoteFrequency = noteToFreq[newNote]


                print(' ')
                print('----- --- ----- --- ----- --- ----- --- ----- --- ----- --- ----- ')
                print('Original Key: ', origNote+'4')
                print('New Key: ', newNote)
                print('Pitch amount: ', interval, ' semitones')            
                print(' ')
                # print('Original frequency: ', originalFrequency )
                # print('New frequency: ', newNoteFrequency)
                frequencyRatio = divide(newNoteFrequency, originalFrequency )
                print('Frequency ratio:', frequencyRatio  )
                currentTempo = float(input("Enter tempo of sample:  "))
                newTempo = (currentTempo * frequencyRatio )
                print('New tempo: ', newTempo)

            # print('The index of', (origNote+'4'), 'in the list is:', index)
            else:
                print("Invalid Input")

        else:
            print("Invalid Input")

        # elif choice == '2':
        #     print(num1, "-", num2, "=", subtract(num1, num2))

        # elif choice == '3':
        #     print(num1, "*", num2, "=", multiply(num1, num2))

        # elif choice == '4':
        #     print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")