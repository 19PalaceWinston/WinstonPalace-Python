#Removes Vowels
def deVowel(str):
   vowel = ["a","e","i","o","u","y"]
   for z in range(len(str)):
       for y in range(len(vowel)):
           if str[z] == vowel[y]:
              str[z] = ""
   return str

#Multiplies a list by a number
def mathStuff(num, a):
    for x in range(len(num)):
        num[x] = num[x]*a
    return num

#deVowel Start
str = list(input("Type "))
newStr = deVowel(str)
z = ""
#Makes list a string
for x in range(len(newStr)):
    z = z + newStr[x]
print(z)
#mathStuff Start
num = [1, 2, 3, 4]
a = 7
print(mathStuff(num,a))
