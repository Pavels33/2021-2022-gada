#1uzd

s = 'hello'
print(s[1])

#2uzd

saraksts = [1,2,[3,4,'hello']]
saraksts[2][2] ='visu labu'
print(saraksts)


#3uzd

teikums = input('Uzraksti teikumu, kur ur vismaz divi vardi kuri sakas ar burtu s')

for vards in teikums . split():
    if vards[0] == 's':
        print(vards)

#4uzd

list = [1,1,1,2,2,2,3,3,3,5,5,5,6,6,6]

def unik_list(list):
    x = []
    for a in list:
         if a not in x:
        x.append()
    return x

print(unik_list(list))    

#5uzd


list= [1,2,3,-4]

def multiply(numbers):
    total = 1
    for x in numbers:
        total *=x
        return total

print(multiply(list))

