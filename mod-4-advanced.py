'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''
socials = {
    "@bongolpoc":{"first_name":"Joselito",
                "last_name":"Olpoc",
                "following":[
                ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                "last_name":"Gonzales",
                "following":[
                    "@chums","@jobenilagan"
                ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                "last_name":"Ilagan",
                "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                ]
    },
    "@joeilagan":{"first_name":"Joe",
                "last_name":"Ilagan",
                "following":[
                    "@eeebeee","@jobenilagan","@chums"
                ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                "last_name":"Ilagan",
                "following":[
                    "@jobenilagan","@joeilagan"
                ]
    },
}
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''

    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph.get(from_member, {}).get('following', []):
        if from_member in social_graph.get(to_member, {}).get('following', []):
            return "friends"
        return "follower"
    elif from_member in social_graph.get(to_member, {}).get('following', []):
        return "followed by"
    else:
        return "no relationship"

print(relationship_status("@chums", "@jobenilagan", socials)=="followed by")

#2nd problem

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)

    def check_line(line):
        if len(set(line)) == 1 and line[0] != '':
            return line[0]
        return None

    for row in board:
        result = check_line(row)
        if result:
            return result

    for col in range(size):
        column = [board[row][col] for row in range(size)]
        result = check_line(column)
        if result:
            return result

    diagonal1 = [board[i][i] for i in range(size)]
    diagonal2 = [board[i][size - 1 - i] for i in range(size)]
    result = check_line(diagonal1)
    if result:
        return result
    result = check_line(diagonal2)
    if result:
        return result

    return "NO WINNER"

print(tic_tac_toe(board6)=="NO WINNER")

#3rd problem
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     },
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time = 0

    current_stop = first_stop
    while True:
        # Check if the current_stop to second_stop leg exists
        if (current_stop, second_stop) in route_map:
            total_time += route_map[(current_stop, second_stop)]['travel_time_mins']
            break

        # Get the next stop
        next_stop = None
        for leg in route_map:
            if leg[0] == current_stop:
                next_stop = leg[1]
                total_time += route_map[leg]['travel_time_mins']
                break

        if next_stop == first_stop or next_stop is None:
            return "Invalid route or stops"  # Indicates an invalid or unreachable route
        current_stop = next_stop

    return total_time

print(eta('a2', 'b1', legs)==10230)