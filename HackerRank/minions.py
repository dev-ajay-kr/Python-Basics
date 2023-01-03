def minion_game(string):
    # your code goes here
    s = len(string)
    consonents, vowels = 0,0
    for i in range(s):
       if string[i] in 'AIEOU':
          vowels = vowels + (s-i)
       else :
          consonents = consonents + (s-i)
    if consonents > vowels :
        print('Stuart {}'.format(consonents))
    elif consonents == vowels:
        print('Draw')
    else:
        print('Kevin {}'.format(vowels))
      

if __name__ == '__main__':
    s = input()
    minion_game(s)