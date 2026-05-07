class Data_structure:

  #Linear Search
  def linear_search(self,arr,target):
    size = len(arr)
    for index in range (0 , size):
      if (arr[index] == target):
        return index
    return False
  
  # Binary Search
  def binary_search (self, arr , target):
    size = len(arr)
    start = 0
    end = size-1

    while (start <= end):
      mid = (start + end) // 2

      if (arr[mid] == target):
        return mid
      
      elif (arr[mid] < target):
        start = mid+1

      elif (arr[mid] > target):
        end = mid -1

    return False



#User_defined
lst= []
print('''\nLinear search (unsorted array allowed)\n
        \nBinary Search (Array must be sorted)\n
        
        ''')
while True:


  action = input("\nInserting elements [Y/n]: ")

  if (action == 'Y'):
    user = int(input("Enter the number of elements: "))
    lst.append(user)
    print(f"Current list : {lst}") 
  elif (action == 'n'):
    print(f"Your final list is : {lst}")
    print("type 'end' to finish")
  elif (action == 'end'):
    break
  else :
    print ("\nInvalid action\n")
target = int(input("\nEnter your target value: ")) 

# #creating the calling object for class 
# my_searcher = Data_structure()
# result = my_searcher.linear_search(lst,target) #calling the function 
# print(f"Your target value is in index {result}")

# Choosing operations 
while True:

  operation = input ('''\nWhat you want to do with List/Array\n
                    1. Linear Search
                    2. Binary Search
                    3. exit (e)
                    ''')

  if (operation == '1'):
    my_linear = Data_structure()
    result_linear = my_linear.linear_search(lst,target) #calling the function 
    print(f"Your target value is in index {result_linear}")

  elif (operation == '2'):
    my_binary = Data_structure()
    result_binary = my_binary.binary_search(lst , target)
    print(f"Your target value is in index {result_binary}")

  elif (operation == 'e'):
    break

  else : 
    print ("\nInavlid Action\n")
