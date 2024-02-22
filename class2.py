name: str = 'Mohammad Abbas'
# print(type(name), name)
fname: str = "Aftab Ahmed"
age: int = 19
education: str = "Intermediate"
# card: str = " PIAIC Student Card\nStudent Name: " + name + "\nAge: " + str(age)
# card: str = f"PIAIC Student Card\nStudent Name: {name} \nFather Name: {fname} \nAge: {age} \nEducation: {education}"
card: str = f"""
 PIAIC Student Card
Student Name: %s 
Father Name: %s 
Age: %d 
Education: %s
""" %(name, fname, age, education)
print(card)

# Jinja Style
"""
student name {{name}}
"""

print([i for i in dir(str) if"__" not in i])

a = 5
b = 8
print("Formated value a = {} and b = {}".format(a,b))

card1: str = """
 PIAIC Student Card
Student Name: {1} 
Father Name: {0} 
Age: {3} 
Education: {2}
""".format(fname, name, education, age)
            # 0     1       2       3
print(card1)

card2: str = """
 PIAIC Student Card
Student Name: {b} 
Father Name: {a} 
Age: {d} 
Education: {c}
""".format(a=fname, b=name, c=education, d=age)
print(card2)

student_code : str = """
print("My name is Mohammad Abbas")
a: int = 3
b: int = 2
print(a+b)
"""
exec(student_code)

x: list[str] = [i for i in dir(str) if"__" not in i]
print(x)
print(len(x))

# String methods
print(name.capitalize())
print(name.casefold())
print(name.lower())
myName: str = "      Mohammad Abbas     "
print(myName)
print(myName.lstrip())
print(myName.rstrip())
print(myName.strip())

import re
# Regular Expression
name1: str = "      Aftab   Ahmed     "
print(name1)
# name2: str = re.sub(' {2,100}',' ',name1)
name2: str = re.sub(' {2,100}',' ',name1).strip()
print(name2)

var: str = "cOdiNG"
print(var)
print(var.title())

nostarch_url: str = 'https://nostarch.com'
new: str = nostarch_url.removeprefix('https://')
print(nostarch_url)
print(new)