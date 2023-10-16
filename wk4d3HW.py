# Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

# input:   [numerator, denominator]
# output:  [reduced numerator, reduced denominator]
# example: [45, 120] --> [3, 8]

# from fractions import Fraction
# def reduce_fraction(fraction):
#     res = tuple
#     n = fraction[0]
#     d = fraction[1]
#     if d == 1:
#         res = (n,d)
#         return res
#     result = str(Fraction(n,d))
#     if '/' in result:
#         result = result.split('/')
#         n = int(result[0])
#         d = int(result[1])
#         res = (n,d)
#     else:
#        res = (int(result[0]),1)
        
#     return res

##### reduced to basic math functions, eliminiating conditionals and therefore computation time
from fractions import Fraction
def reduce_fraction(fraction):
    result = Fraction(fraction[0],fraction[1])
    return result.numerator, result.denominator

print(reduce_fraction([45,120]))
# # Let us consider this example (array written in general format):

# # ls = [0, 1, 3, 6, 10]

# # Its following parts:

# # ls = [0, 1, 3, 6, 10]
# # ls = [1, 3, 6, 10]
# # ls = [3, 6, 10]
# # ls = [6, 10]
# # ls = [10]
# # ls = []
# # The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# # The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.

# # Other Examples:
# # ls = [1, 2, 3, 4, 5, 6] 
# # parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

# # ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
# # parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
# # Notes
# # Take a look at performance: some lists have thousands of elements.
# # Please ask before translating.
# def parts_sums(ls):
#     result = []
#     current_sum = 0
#     result.append(current_sum)
    
#     # Iterate through the list in reverse order
#     for num in reversed(ls):
#         current_sum += num
#         result.append(current_sum)
    
#     # Reverse the result list to get the correct order
#     return list(reversed(result))


# print(parts_sums([0,1,3,6,10]))

# ##########   Here we have eliminated the append and list reverse operations (-1,-1,-1 - just start out in reverse) 
# # to improve the time complexity
# ##########   space is linear due to the increasing size of <result>
def parts_sums(ls):
    result = [0] * (len(ls) + 1)
    for i in range(len(ls) - 1, -1, -1):
        result[i] = result[i + 1] + ls[i]
    return result

print(parts_sums([0,1,3,6,10]))


# # initial = 2
# # multiplier = 1
# # swings = 1

# # result:
# #   1 head appearead after the swing: 2 - 1 + 1 = 2
# #   Zmey has 2 heads in the end
# # initial = 5
# # multiplier = 10
# # swings = 3

# # result:
# #   10 heads appearead after the first swing: 5 - 1 + 10 = 14
# #   20 heads appearead after the second swing: 14 - 1 + 2 * 10 = 33
# #   60 heads appearead after the third swing: 33 - 1 + 2 * 3 * 10 = 92
# #   Zmey has 92 heads in the end

# #Alyosha Popovich (Russian folk hero) stroke his sharp sword and cut the head of Zmey Gorynych (big Serpent with several heads)! He looked - and lo! - in its place immediately new heads appeared, exactly n. He stroke again, and where the second head was, 2*n heads appeared! The third time it was 2*3*n new heads, and after fourth swing it was 2*3*4*n heads, and so forth. And thus Alyosha decided to call it a day, and instead called a fellow Mage for help. While the Mage agreed, he needs to know the exact number of heads that Zmey Gorynych now has.


# def count_of_heads(initial, n, swings):
#     global result
#     result_str = ''          ### string is empty
#     result = initial -1 + n     ### result = init - 1 + multi
#     if swings == 1:
#         return result
#     elif swings == 2:
#         return result -1 + 2 * n
#     else:
#         x=3
#         result = result - 1 + 2 * n
#         print(f'3rd result: {result}')
#         result_str = f'1 + 2 * {x}'
#         print(f'result string goint into the loop:{result} - {result_str}')
#         for x in range(4,swings+1):
#             result = eval(f'{result}-{result_str}*{n}')
#             result_str+=f' * {x}'


#         result_str+=f' * {n}'
#         print(f'last result string:{result} - {result_str}')
#         result = eval(f"{result}-{result_str}")
#         return result

'''
    this version is considerably more efficient on all fronts as it eliminates the unnecessary conditionals and storage
    and relies strictly on the math
'''
def count_of_heads(i, m, s):
    cnt= 0
    while s:
        cnt+=1
        m*= cnt
        i= i-1+m
        s-= 1
    return i

print(count_of_heads(5,10,3))