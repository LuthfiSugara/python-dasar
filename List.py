# Mendefinisikan List
mobil = ["Ferari", "Ducaty", "Honda"]
datadiri = ["Desi","Familia", 20, 1999]

# Dengan keyword list
motor = list(("Harley", "Honda", "Vespa"))

print(motor[0])
print(motor[1:2])
print(motor[-1])

motor[0] = "Yamaha"
print(motor)

motor.append("Suzuki")
motor.insert(0, "Ducati")
print(motor)

del motor[0]
print(motor)
motor.remove("Vespa")
print(motor)

join = motor + mobil
print(join)

# loop
print(motor * 3)
