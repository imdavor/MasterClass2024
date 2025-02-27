# 224. Matching dates
import re

text = "Today is 11-27-2018. PyCon starts 3-13-2013."
pattern = r"\d{1,2}-\d{2}-\d{4}"
dates = re.findall(pattern, text)

print(dates)


# 223. Checking Validity of Emails
"""import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = input("Enter your email address: ")
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
"""

# 221. Matching Email Addresses
"""import re

text = "Please contact us at: support@datacamp.com"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
# 1. support -- [A-Za-z0-9._%+-]+ najmanje 1 ili više znakova od A do Z, a do Z, 0 do 9, ., _, %, +, -
# 2. @[A-Za-z0-9.-]+ -- iza znaka @ i +(mora biti najmanje 1 alfanumeric) 
# 3. \. mora biti točka
# 4. [A-Za-z]{2,} -- iza točke mora biti slovo od A do Z, a do Z, 2 do ili više znakova

matches = re.findall(pattern, text)
print(matches)"""


# 220. Matching Phone Numbers Part 1
# 221. Matching Phone Numbers Part 2
""""import re

text = "Please contact us at +91 (123) 456-7890 or via email joe@gmaul.com"
#pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"
# 1. \+ = izbjegni plus znak ali ? on je opcija da ga ima
# 2. onda iza ide broj od [0-9] pa koristimo shorthand \d
# 3. za country code imamo 3 broja pa ide {1,3}
# 4. iza pozivnog broja može ići space, točka ili minus, [-.\s]
# 5. onda ide \(?\d{1,3}\)? za (123)
# 6. iza (123) može ići space, točka ili minus, dodajemo ? --- [-.\s]?
# 7. 800 -- \d{1,3} pošto idu od jednog do tri broja čekiramo broj \d i brojeve od 1 do 3
# 8. iza 800 može ići space, točka ili minus, dodajemo ? --- [-.\s]?
# 9. 555-1234 -- \d{1,4} pošto idu od jednog do tri broja čekiramo broj \d i brojeve od 1 do 4


matches = re.findall(pattern, text)
print(matches)"""

# 219. Combining Shorthands & Metacharacters

"""import re

text = "Heloooo Pythooon is aweeesoomee!"
pattern = r"\\w*o+\\w*"  # bilo koji alfanum + opcionalni *. o+ = o mora biti jedanput ili više puta
matches = re.findall(pattern, text)
print(matches)"""

# 218. S Shorthand
"""import re

text = "The variabla name \t is my_var123! \n"
pattern = r"\\S+"  # whitespace, tabs, space znakovi u textu; \\S je kontra; S+ daje skupne kontra
matches = re.findall(pattern, text)
print(matches)"""

# 217. W Shorthand
""""import re

text = "The variabla name is my_var123! \n"
# pattern = r"\\w"  # svi znakovi u textu
pattern = r"\\W"  # koji nisu alfanumerički znakovi u textu
matches = re.findall(pattern, text)
print(matches)
"""
# 216. Shorthand For Numeric Characters
"""import re

text = "The cat and the dog set on the mat at 9 AM"
# pattern = r"[0-9]"  # koristimo [] i traži bilo koji znak iz bracketa u textu
# ili
# pattern = r"\\d"  # dođe isto kao  r"[0-9]"
# pattern = r"\\D" # svi znakovi koji nisu brojevi

matches = re.findall(pattern, text)
print(matches)"""

# 215. Finding Vowels
"""import re

text = "The cat and the dog set on the mat"
pattern = r"[aeiou]"  # koristimo [] i traži bilo koje slovo iz bracketa u textu

matches = re.findall(pattern, text)
print(matches)
"""
# 214. Character Class & Find All
"""import re

text = "The cat and the dog set on the mat"
pattern = r"[abc]"  # koristimo [] i traži bilo koje slovo iz bracketa u textu

matches = re.findall(pattern, text)
print(matches)
"""
# 213. Find All
"""import re

text = "Some sentence the words from the sentencens"
pattern = r"the"  # traži pattern the

matches = re.findall(pattern, text)
print(matches)
"""
# 212. Character Class
"""import re

string = ""
pattern = r"[Pp]ython"  # python, Python
# ili r"[a-z]" range sve između a i z mala slova
# ili r"[a-zA-Z]" range sve između a i z velika i mala slova
# ili r"[0-9]" range sve između 0 i 9


if re.match(pattern, string):
    print("Match Found")
else:
    print("Match NOT Found")
"""
# 211. Caret Metacharacter ( ^ )
"""import re

string = "385 123 456"
pattern = r"^385"  # brojevi/stringovi moraju početi sa 385

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match NOT Found")
"""
# 209. Optional Metacharacter
# 210. Optional Metacharacter Example
# "a-?b" crtica je opcionalna
""""
import re

string = "paython file"
pattern = r"paython-?file"

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match NOT Found")
"""
# 207. Wildcard Metacharacter ( a.b ) = bilo koji znak između a i b

# Match acb, accb
# Non Match ab, acab
"""
import re

string = "abbc"
pattern = r"a..c"  # znači: pattern mora biti točno: . jedan znak,  .. dva znaka

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match NOT Found")
"""
# 203. Plus Metacharacter
# 204. Plus Metacharacter Example
# 205. Curly Braces Metacharacter


# pattern = r"ab{3}c"  # match: abbbc #no-match: ab = b pattern točno tri puta
# pattern = r"ab{3,}c"  # match: abc abbc abbbbc #no-match: ab = b pattern najmanje tri ili više puta

"""import re

string = "abbc"
pattern = r"ab{2}c"  # znači: pattern mora biti: a barem jednom. b mora se pojaviti barem 1 # r = raw string

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match NOT Found")
"""
"""
import re

string = "abc"
pattern = r"ab+c"  # znači: pattern mora biti: a barem jednom. b mora se pojaviti barem 1 # r = raw string

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match Found")"""
# 202. Star Metacharacter
"""import re

string = "abc"
pattern = "ab*c"  # znači: pattern mora biti: a i c. b=0 ili koliko hoćeš b između a i c

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match Found")
"""
# 201. Metacharacter In Regular Expression --- * , + , {} , . , ? , ^

# 200. Match & Search
"""
import re  # regular expressions

string = "bca"
pattern = "a"

if re.search(pattern, string):  # search za razliku od matcha(koji gleda od početka stringa) gleda kroz cijeli string i
    # traži podudarnost
    print("Match Found")
else:
    print("Match Found")"""

# 198. Introduction To Regular Expressions
# 199. Writing Our First Regular Expression

"""import re  # regular expressions

string = "abc"
pattern = "a"

if re.match(pattern, string):
    print("Match Found")
else:
    print("Match Found")
    """
