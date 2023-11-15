#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
 
def make_shirt(size, message='I love Python!'):
    #Summarize the shirt that's going to be made.
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large')
make_shirt('medium')
make_shirt('small', 'Programmers are amazing.')
