def personal_information ():
    ''' Will ask for personal information '''

    name = str (raw_input ("Please enter your name: "))          # Ask name.
    age = int (raw_input ("Please enter your age: "))      # Ask age.
    address = str (raw_input ("Please enter your address: "))    # Ask address.

    return name, age, address

def room_number_and_section ():
    ''' Will find what your room number and section. '''

    room_number = 808
    room_section = "A"

    print "From the information above, your room number and section should be:", room_number , room_section

personal_information ()
room_number_and_section ()
