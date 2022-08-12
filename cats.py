class Cat:
                    
   animal ='Cat'
                   
   def __init__(self, breed, color):
                     self.breed = breed
                     self.color = color
                
tom = Cat("bengal", "brown")
lothal = Cat('ragdoll','white')
                 
print('tom details')
print('tom is a ',tom.animal)
print('breed:',tom.breed)
print('color:',tom.color)
                
print('\nlothal details')
print('lothal is a ',lothal.animal)
print('breed:',lothal.breed)
print('color:',lothal.color)

print("\nAccesting class variable using class name")
print(Cat.animal)