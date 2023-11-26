# #!/usr/bin/env python3

# def happy_new_year(count):
#  while count >=0:
#     print(count)
#     if count == 0:
#        print('Happy')
#     count -=1

# happy_new_year(10)

# def square_integers(int_list):
#     squred = [i * i for i in int_list]
#     print(squred)
# square_integers([1, 2, 3, 4, 5])

def fizzbuzz(a):
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print('fizzbuzz')        
        elif i%5==0:
            print('buzz')
        elif i%3==0:
            print('fizz')
        else:
            print(i)
  
    

fizzbuzz(100)