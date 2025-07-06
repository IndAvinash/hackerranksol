def minion_game(string):
    Stuart = 0
    Kevin = 0
    vowel = "AEIOU"
    
    
    for i,l in enumerate(string,0):
       score = len(string)-i
       if(l in vowel):
           Kevin+= score
       else:
           Stuart+=score
           
    if(Kevin!=Stuart):
        if(Kevin>Stuart):
            print(f"Kevin {Kevin}")
        else:
            print(f"Stuart {Stuart}")
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)