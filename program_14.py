'''
Problem:
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false
'''


def count_substring(string, sub_string):
    '''
    Counts the total number of the sub-strings in the given string.
    '''

    cnt = 0
    pos = 0
    while True:
        if string.find(sub_string, pos, len(string)) != -1:
            pos = string.find(sub_string, pos, len(string))
            pos += 1
            cnt += 1
        else:
            break

    return cnt


def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    Kevin = []
    Stuart = []
    score1 = 0
    score2 = 0
    sub_string1 = []
    sub_string2 = []
    
    for i in range(len(s1)):
        if s1[i] in vowels:
            Kevin.append(s1.index(s1[i]))  # This for loop was used to append the indexs of consonants and vowels in Stuart and Kevin resp.
            s1.pop(i)
            s1.insert(i, 2)
        else:
            Stuart.append(s1.index(s1[i]))
            s1.pop(i)
            s1.insert(i, 2)
    
    for i in Kevin:
        Kevin_sub = []
        for j in s2[i:]:  # This 'for' loop creates all the possible sub-strings from the first vowel and the subsequent vowels.
            Kevin_sub.append(j)
            sub_string = ''.join(Kevin_sub)
            if sub_string not in sub_string1:  # To check if the new sub-string is already present or not when 'i' changes.
                sub_string1.append(sub_string)
                score1 += count_substring(string, sub_string1[-1])
    
    for i in Stuart:  #  Similar loop as above.
        Stuart_sub = []
        for j in s2[i:]:
            Stuart_sub.append(j)
            sub_string = ''.join(Stuart_sub)
            if sub_string not in sub_string2:
                sub_string2.append(sub_string)
                score2 += count_substring(string, sub_string2[-1])
    
    if score1 > score2:
        return print('Kevin {}'.format(score1))
    elif score2 > score1:
        return print('Stuart {}'.format(score2))
    else:
        return print('Draw')


s = input()
s1 = list(s)
s2 = list(s)
minion_game(s)

'''
def minion_game(string):
    scores = {'Kevin': 0, 'Stuart': 0}

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            scores['Kevin'] += len(string) - i
        else:
            scores['Stuart'] += len(string) - i

    if scores['Stuart'] == scores['Kevin']:
        print('Draw')
    elif scores['Stuart'] > scores['Kevin']:
        print('Stuart {}'.format(scores['Stuart']))
    else:
        print('Kevin {}'.format(scores['Kevin']))


if __name__ == '__main__':
    s = input()
    minion_game(s)
'''
