def checkvowel (n):
    match n:
        case "a" : return "this is a vowel"
        case "e" : return "this is a vowel"
        case "i" : return "this is a vowel"
        case "o" : return "this is a vowel"
        case "u" : return "this is a vowel"
        case _: return "simple Alphabet"
        
		
print(checkvowel("a"))
print(checkvowel("e"))
print(checkvowel("b"))

words = [1,2,3,4,5,6,7]
for pi in words:
    print(pi)
    
food = ["Rice", "Beans", "Fufu", "Garri"]
fruits = ["Orange", "Apple", "Mango" ,"Pineaple"]
for x in food:
    for y in fruits:
        print(x, ":", y)
        
i = 0
while i < 6:
    print(i)
    i += 1
    

    s = 0
while s < 10:
    print("s:", s)
    
    if s == 5:
        print("Breaking...")
        break
    s += 1
    
print("end")

for letter in "python":
    if letter == 'y':
        continue
print("Current Letter:", letter)