#def function (arg1, *args=[], **kwargs={}): #arguments and key word arguments
    #pass
# def sum(*args): #args is an iterable object. * is the unpacking operator. 
#                 #args is a tuple. Tuples are not mutable like lists
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# #kwargs accepts named argument, keyword arguments
# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result



# # print(sum(*range(19)))
# # print(sum(1,2,3,4,5,6,1324,123))
# # print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))



# ###recursion
# def factorial(number):
#      # Validate input
#      if not isinstance(number, int):
#          raise TypeError("Sorry. 'number' must be an integer.")
#      if number < 0:
#          raise ValueError("Sorry. 'number' must be zero or positive.")
#      # Calculate the factorial of number
#      def inner_factorial(number):
#          if number <= 1:
#              return 1
#          print(str(number), " * ", str(number-1), ' = ', number * (number-1))
#          return number * inner_factorial(number - 1)
#      return inner_factorial(number)

# # print(factorial(5))


# def recursive_sum(current_number, accumulated_sum):
#     if(current_number > 0):
#         return recursive_sum(current_number-1,accumulated_sum+current_number)
#     else:
#         return accumulated_sum

# # print(recursive_sum(10,10))

# def attach_head(element, input_list):
#     return [element] + input_list

# my_list = [1,2,3,4,5]
# print(*attach_head("jeff", my_list))
# a, *b, c = my_list
# print(*my_list)
# print(a,b,c)

# dict_1 = {"A":1, "B":2,"C":3}
# dict_2 = {"D":4,"D":5}
# merge_dict = {**dict_1, **dict_2}
# print(merge_dict)

# *a,  = "Real python"
# print(type(a))

# my_tuple = (*range(10),)
# print(my_tuple)

# import os

# class testingFunctions():

#     def __index__(self):
#         return 1

#     def __abs__(self):
#         return -10

# a = testingFunctions()
# import pdb; pdb.set_trace()
# print(bin(a))
# print(abs(a))

# print(bool(a))
# print().__doc__

# def uppercase_decorator(function):
#     def wrapper(arg1):
#         print(arg1)
#         return function(arg1).upper()         #invoke function and convert ouptut to uppercase
    
#     return wrapper

# @uppercase_decorator
# def say_hi(test_arg1):
#     print(test_arg1)
#     return "hello there"
    
# print(say_hi("jeff"))


# def tag_decorator_with_arguments(html_tag):
#     def tag_decorator(function):
#         def wrapper(innerHTML):
#             return "<" + html_tag + ">" + function(innerHTML) + "</" + html_tag + ">"
#         return wrapper
#     return tag_decorator
    
# @tag_decorator_with_arguments("div")
# def fill_html_tag(innerHTML):
#     return innerHTML

# print(fill_html_tag("test"))
# list_of_tags = ("body", "document", "div", "h1")


# def tag_function_factory(tag_list):
#     tag_maker = {}
#     for tag in tag_list:
#         tag_maker[tag] = make_html_tag(tag)
#     return tag_maker


# def make_html_tag(tag):
#     def make_tags(content, *args):
#         # print("inside make tags", args)
#         return "<" + tag + class_maker(*args) + ">" + content + "</" + tag + ">"
    
#     return make_tags

# def class_maker(*args):
#     """This function creates a string with all of the html classes concatenated together."""
#     if(not bool(len(args))):
#         return ''
#     class_str = " class="
#     for counter, class_element in enumerate(args):
#         if(counter != 0):
#             class_str += " " + class_element
#         else:
#             class_str += class_element
#     return class_str


# my_list = tag_function_factory(list_of_tags)
# print(my_list['div']("happy birthday", 'container', 'w-70'))


# make_a_div = make_html_tag("div")
# make_a_body = make_html_tag("body")
# print(make_a_body(make_a_div(make_a_div("this is a line.","col"),"container", "w-100", "row")))


from htmlfactory import *


print(TagFactory("div.basic", "test"))
print(SingletonTag("derk"))