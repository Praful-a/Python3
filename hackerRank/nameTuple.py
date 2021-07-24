from collections import namedtuple
Car = namedtuple('Car', 'ID Name')
xyz = Car(ID=1, Name='Hello')
xyz = Car(ID=2, Name="Sumit")
print(xyz)