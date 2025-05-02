import random

tirada = []

for i in  range(5):
    tirada.append(random.randint(1,6))

print(tirada)


caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))
print(random.choices(caras,k=5))


for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}')