from pyswip import Prolog

prolog = Prolog()

prolog.consult('cybersport.pl')

def greet():
    print('Laboratory work Counter-Strike cybersport teams and players')
    print('Type `help` to show the list of availabilities')


def helpCommand():
    print('---------------')
    print("instructions:")
    print('is there team named <name>')
    print('is there team from <country>')
    print('is <country> strong')
    print('is <team> top tier')
    print('has <team> achievement')
    print('which achievements has <team>')
    print('which teams has <region>')
    print('which teams have diverse achievements')
    print('which teams have achievement <achievement>')
    print('---------------')


def teamsQuery(arr):
    if arr[0] == 'named':
        result = prolog.query(f'team({arr[1]})')
        print("There is " + ("NO " if len(list(result)) == 0 else "") + "team named " + arr[1])
    elif arr[0] == 'from':
        result = prolog.query(f'country(Team, {arr[1]})')
        print("There is " + ("NO " if len(list(result)) == 0 else "") + "team from " + arr[1])


def isThereLangStyle(arr):
    if (arr[0] == 'team'):
        teamsQuery(arr[1:])

def isLangStyle(arr):
    if (arr[1] + arr[2] == 'toptier'):
        result = prolog.query(f'top_tier({arr[0]})')
        print(f"{arr[0]} is " + ("NOT " if len(list(result)) == 0 else "") + "top tier")
    elif (arr[1] == 'strong'):
        result = prolog.query(f'strong_region({arr[0]})')
        print(f"{arr[0]} is " + ("NOT " if len(list(result)) == 0 else "") + "strong")

def hasLangStyle(arr):
    arr1 = ' '.join(arr[1:])
    result = prolog.query(f'achievements({arr[0]}, Achievements), member(\'{arr1}\', Achievements)')
    print(f"{arr[0]} has " + ("NOT " if len(list(result)) == 0 else "") + f"{arr1}")

def whichLangStyle(arr):
    if arr[0] == 'achievements' and arr[1] == 'has':
        result = prolog.query(f'achievements({arr[2]}, X)')
        lst = list(result)
        if (len(lst) == 0):
            print(f"{arr[2]} has no achievements")
        else:
            print(arr[2] + " has " + ', '.join(lst[0]['X']) + " achievements")
    elif arr[0] == 'teams' and arr[1] == 'has':
        result = prolog.query(f'country(X, {arr[2]})')
        lst = list(result)
        if (len(lst) == 0):
            print(f"{arr[2]} has no teams")
        else:
            print(arr[2] + ' has ' + ', '.join(list(map(lambda x: x['X'], lst))))
    elif arr[0] == 'teams' and arr[1] == 'have' and arr[2] + arr[3] == 'diverseachievements':
        result = prolog.query(f'diverse_achievements(X)')
        lst = list(result)
        if (len(lst) == 0):
            print(f"No such teams")
        else:
            print('diverse achievements have ' + ', '.join(list(map(lambda x: x['X'], lst))))
    elif arr[0] == 'teams' and arr[1] == 'have' and arr[2] == 'achievement':
        tostr = ' '.join(arr[3:])
        result = prolog.query(f'achievements(X, Y), member(\'{tostr}\', Y)')
        lst = list(result)
        if len(lst) == 0:
            print("No such teams")
        else:
            print(tostr + ' have ' + ', '.join(list(map(lambda x: x['X'], lst))))

def awaitInput():
    s = input()
    if s == 'help':
        helpCommand()
    arr = s.split()
    try:
        if arr[0] == 'is' and arr[1] == 'there':
            isThereLangStyle(arr[2:])
        elif arr[0] == 'is':
            isLangStyle(arr[1:])
        elif arr[0] == 'has':
            hasLangStyle(arr[1:])
        elif arr[0] == 'which':
            whichLangStyle(arr[1:])
    except:
        print("I don't understand")

if __name__ == '__main__':
    greet()
    while True:
        awaitInput()
