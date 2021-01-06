# Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

# {'James': ['Jacob', 'Bill', 'Lucas'],
#  'Johnny': ['David', 'Kyle', 'Lucas'],
#  'Peter': ['Lucy', 'Kyle']}

# and also a list of the names of the dead people:
# ['Lucas', 'Bill']

# return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

def killer(suspect_info, dead):
    # assumptions: suspect is always in the suspect_info. there is only one killer.

    # for each victim in the dead list
    for victim in dead:
        # if the suspects list is down to one person, that person is the killer
        if len(suspect_info) == 1:
            return list(suspect_info.keys())[0]
        # for each suspect in the dictionary, see if they saw the victim that day
        remaining_suspects = list(suspect_info.items())
        for suspect, people_seen in remaining_suspects:
            # if the suspect did not see victim, suspect can be removed from dictionary altogether
            if victim not in people_seen:
                del suspect_info[suspect]
            # else, suspect remains in dictionary and move on to the next suspect
    
    # after going through all victims, there should be one suspect left in dictionary
    return list(suspect_info.keys())[0]