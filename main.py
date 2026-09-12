# def function(a,b,c):
#     """ this will return the min value of the def1 def2 def3 """
#     def1=abs(a-b)
#     def2=abs(b-c)
#     def3=abs(c-a)
#     return min(def1,def2,def3)
# print(
#     function(1, 10, 100),
#     function(1, 10, 10),
#     function(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
# )
# # help(function)

# print(1,2,3,sep="<")


# #function applied to function

# def multiply_by_5(x):
#     return 5 *x

# def call(fun,arg):
#     return fun(arg)

# def squared_call(fun,arg):
#     return fun(fun(arg))


# print(
#     call(multiply_by_5,3),
#     squared_call(multiply_by_5,4),
#     sep='\n'
# )

# def mod_5(x):
#     return x%5

# print(
#     max(10,300,100),
#     max(10,5,79, key=mod_5),
#     sep="\n"
# )


# x = True
# print(x)
# print(type(x))



# name= "sijal"
# print(type(name))


# def can_run_for_precident(age):
#     return age>=35

# print(can_run_for_precident(50))
# print(can_run_for_precident(30))

# def is_odd(n):
#     return (n%2==1)
# print("is it a odd", is_odd(5))



# def can_run_for_precident(age, is_natural_born_citizen):
#     return (is_natural_born_citizen and age>=35)

# print("he is capable of running on that", can_run_for_precident(40,False))


# def inspect(x):
#     if x==0:
#         print(x,"is zero")
#     elif x>0:
#         print(x," is positive")
#     elif x<0:
#         print(x,"is negative")
#     else:
#         print(x," is unlikely anything i have ever seen")

# print(inspect(10))
# print(bool(2))
# if 0:
#     print(0)
# elif "spam":
#     print("spam")

#     # python treats the non empty string as the true si the result is that spam
    

# def sign(x):
#     if x==0:
#         return 0
#     elif x>0:
#         return 1
#     else:
#         return -1

# print(sign(-6))

# def concise_is_negative(number):
#     return number<0
# print(concise_is_negative(-2))


# # the list


hello= [1,3,5,5]
# print(hello[-1])


# #slicing

# print(hello[0:3])
# print(hello[-3:])

# hello[0]=99
# print(hello)

# length=sorted(hello)
# print(length)



# x=1
# print(x.imag)

# c =12+3j
# print(c.imag)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# planets.append("pluto")
# print(planets)
# planets.pop()
# print(planets)
# print(planets.index("Earth"))
# print("Earth" in planets)


# # touples


# t=(3,4323,8)


# c=0.145
# print(c.as_integer_ratio())

# a = 1
# b = 0
# a, b = b, a
# print(a, b)


# #loops

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end="")

# data=input()
# print(data)

# multiplier=(1,2,3,4,5)
# product=1
# for i in multiplier:
#     produc= i * product

# print(produc)

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    total= product * mult


print(total)


# s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'


# for i in s:
#     if i.isupper():
#         print(i, end=" ")
    
# for i in range(5):
#     print("Doing important work. i =", i)



#while loop
# i=0 

# while i<10:
#     print(i,end=" ")
#     i+=1

# # squares=[n**2 for n in range(4)]
# # print(squares)

# squares=[]

# for n in range(6):
#     squares.append(n**2)

# print(squares)


# list=[5, -1, -2, 0, 3]

# def neg_counter(neg):
#     count=0
#     for i in neg:
#         if i<0:
#             count+=1
#     return count 
# print(neg_counter(list))



# nu=[7,9,12,15,18]
# def has_luckey_number(nums):
#     for num in nums:
#         if num %7 ==0:
#             return True
#         else:
#             return False
# print(has_luckey_number(nu))


# def estimate_average_slot_payout(n_runs):
#     """Run the slot machine n_runs times and return the average net profit per run."""
#     total_payout = 0.0
    
#     # 1. Loop exactly n_runs times
#     for i in range(n_runs):
#         # 2. Track total winnings by calling the hidden slot machine function
#         total_payout += play_slot_machine()
        
#     # 3. Calculate Total Winnings minus the $1 cost for every run
#     total_net_profit = total_payout - n_runs
    
#     # 4. Return the average (Total profit divided by total runs)
#     return total_net_profit / n_runs
# print(estimate_average_slot_payout(1))

# print("my name is sijal ")

# "pluto' is a planet"


# print("""hello world""")



# print("hello")
# print("world") # default is that the \n
# print("hello", end="")
# print("pluto",end=" ") 


# planet="Pluto"
# print(planet[0])


# # slicing
# print(planet[3:])


# print(len(planet))

# # for char in planet:
# #     print(char+'!')
    

# print([char+'! ' for char in planet])


# # print(planet.upper())
# # print(planet.lower())
# # print(planet.index("plan"))

# claim = "Pluto is a planet!"
# print(claim.split())


# print(claim.index("plan"))

# # join



# print('🎃'.join([w.upper() for w in claim]))
# ' 👏 '.join([word.upper() for word in claim])
# print(planet+"we miss you")

# position =9

# print(f"{planet} you always be the  {position} planet to me")



# print( '{}, you will be {} planet to me'.format(planet, position))
# print("{}, you'll always be the {}th planet to me.".format(planet, position))

# pi = 3.14159265
# print('{:.2%}'.format(pi))
# numbers={'one':1, 'two':2}
# print(type(numbers))
# print(numbers['one'])

# numbers['eleven'] = 11
# print(numbers)
planets=["mercury", "venus", "earth"]

print([planet[0].upper() for planet in planets ])
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = [planet[0].upper() for planet in planets]
print(planet_to_initial)

print('Mars' in planets)
# for planet, initial in planets:
#     print('{}, begins with {}'.format(planet,initial))

# Create a dictionary
user = {
    "name": "Alice",
    "role": "Admin",
    "status": "Active"
}

# Get the dictionary items
name=print(list(user.items()))
# print(name[0])

# help(str.isdigit)

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

def word_search(doc_list, keyword):
    indices=[]
    for i, doc in enumerate(doc_list):
        tokens=doc.split()

        normalized = [token.rstrip('.,').lower() for token in tokens]
           # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

print(word_search(doc_list,'car'))