#Stack implementation using Python

#class definition of stack
class Stack:
  #constructor to initialise the stack
  def __init__(self):
    #initialise an empty list as the underlying ds
    self.stack = []
  #Method to check if stack is empty
  def isempty(self):
    # Returns True if the stack is empty (self.stack is an empty list), False otherwise
    return self.stack ==[]
  #Method to push an element onto the stack
  def Push(self,v):
    #Append the value v t
    self.stack.append(v)
  def pop(self):
    # Initialise the variable v as None
    v = None
    #Check if the stack is not empty
    if not self.isempty():
      # Remove and assign the last element from self.stack to the variable v
      v = self.stack.pop()
    #Return the value v
    return v
  #Method to provide a string representation of the stack
    def __str__(self):
      #Return the string representation of self.stack
      return str(self.stack)
      
# Create an instance of stack class
S = Stack()

# Push four values onto the stack
S.Push(10)
S.Push(20)
S.Push(30)
S.Push(40)

# Pop and print the topmost element from the stack
print(S.Pop())  # Output: 40

# Pop and print the topmost element from the stack
print(S.Pop())  # Output: 30

# Print the string representation of the stack
print(S)  # Output: [10, 20]
    
