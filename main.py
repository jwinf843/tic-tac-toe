our_string = "This problem is for James"

def vowel_puller(a_string):
    vowels = 'aeiou'
    
    first = ''
    second = '' 
    
    for letter in a_string:
        if letter in vowels:
            first += letter
        else:
            second += letter
            
    return first + second


assert vowel_puller(our_string) == "ioeioaeThs prblm s fr Jms"
print('Passing initial test')