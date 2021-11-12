count=100
name="Jane"
pair=10.12

print (count)
print (name)

print (pair)

a=b=c=1
print(a)
print (b)
print(c)

d,e,f=1,2,"John"
print(d,e,f)

var1=1
var2=2
var3=3
#del var2
print(var1,var2,var3)

str = 'Hello World!'

print(str)      # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print ( str[2:])     # Prints string starting from 3rd character
print (str * 2  )    # Prints string two times
print (str + "TEST") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print( list)          # Prints complete list
print (list[0] )      # Prints first element of the list
print (list[1:3] )    # Prints elements starting from 2nd till 3rd 
print (list[2:]  )    # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist )# Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print ( tuple)          # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:] )          # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print  (dict['one'])      # Prints value for 'one' key
print  (dict[2])          # Prints value for 2 key
print (tinydict )       # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values