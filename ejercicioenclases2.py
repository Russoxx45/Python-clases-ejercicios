s = "oso,perro,10,5,son animales"
s1 = s.split(",")

if s1[0] == (s1[0][::-1]):
    print(s1[0]+" es palindromo")
if s1[1] != (s1[1][::-1]):
    print(s1[1]+"no es palindromo")

print("Tenemos", s1[2], s1[0]+'s.')
print("Tenemos", s1[3], s1[1]+'s.')

print(s1[0], 'y', s1[1], s1[4])
