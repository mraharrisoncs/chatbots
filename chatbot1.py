# Simple Chatbot program – [type your name here]
#let's grab the random functions, we'll need these later
import random

#let's ask for their name
name=input('What is your name?')

#now print a random greeting
print(random.choice(['hello','hi!','howdy!']),name)

#ask their favourite sport
sport=input('What is your favourite sport?')
if sport=='football':
    print('Me too, I support Newcastle United')
elif sport=='rugby':
    print('Hmm, not a fan of rugby myself, I prefer football')
# add an elif statement here if the answer is 'hockey'


else: 
    print('I see you like',sport,name)

# add your own questions and answers below here


# can you change this to say a random goodbye phrase? (see above)
print('bye!')

