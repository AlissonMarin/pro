import random

character= ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
longitud=int(input('Introduce la longitud de tu contraseña'))
contraseña=''
for a in range(longitud):
    contraseña +=random.choice(character)

print('Tu contraseña es:',contraseña)
