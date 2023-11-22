
numbers = []


#1-2
def get_float():
        
    for item in range(3):
        
        try:
            # numbers = []
            number = float(input('Insert a number: '))
            numbers.append(number)
        except ValueError:
            print('***YOUR VALUE IS NOT CORRECT TRY AGAIN***')
            get_float()
          
    return numbers

get_float()   

print(numbers)

# #1-3
largest_number = max(numbers)
print(f'The biggest number is {largest_number}')



   