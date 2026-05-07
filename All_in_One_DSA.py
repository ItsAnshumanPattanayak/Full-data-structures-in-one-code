class Data_structure:
  #Linear Search
  def linear_search(self,arr,target):
    size = len(arr)
    for index in range (0 , size):
      if (arr[index] == target):
        return index
    return False

#User_defined
lst= []
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

#creating the calling object for class 
my_searcher = Data_structure()
result = my_searcher.linear_search(lst,target) #calling the function 
print(f"Your target value is in index {result}")
