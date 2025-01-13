# lambda function ->
    # lambda arguments: expression\
        
addition = lambda a,b: a+b
print(addition(5,7))

even = lambda a: 'even' if a%2 == 0 else 'odd'
print(even(7))
        
def lamda_function(a, b):
    return a+b

print(lamda_function(5,7)) 


numbers = list(range(1, 5))
square_list = list(map(lambda x: x**2, numbers))
print(square_list)

number1 = list(range(1, 5))
number2 = list(range(5, 10))
new_list = list(map(lambda x,y: x+y, number1, number2))
print(new_list)

numbers = list(range(1, 21))
even_list = list(filter(lambda x: x%2==0, numbers))
print(even_list)

print([x for x in numbers if x%2 == 0], [x for x in numbers if x%2 != 0])

people = [
    {"name": "Shimul", "age": 25},
    {"name": "Sohan", "age": 15}
]

filt = list(filter(lambda person: person["age"] > 15, people))
print(filt)