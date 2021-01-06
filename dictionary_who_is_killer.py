# Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

# {'James': ['Jacob', 'Bill', 'Lucas'],
#  'Johnny': ['David', 'Kyle', 'Lucas'],
#  'Peter': ['Lucy', 'Kyle']}

# and also a list of the names of the dead people:
# ['Lucas', 'Bill']

# return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

def killer(suspect_info, dead):