from functions.add import *
from functions.subtract import *
from functions.multiply import *
from functions.divide import *

numbers = [int(i) for i in input('Enter numbers seperated by comma').split(',')]

print ('Sum is %f' % (add(numbers[0], numbers[1])))
print ('Difference is %f' % (subtract(numbers[0], numbers[1])))
print ('Product is %f' % (multiply(numbers[0], numbers[1])))
print ('Division result is %f' % (divide(numbers[0], numbers[1])))