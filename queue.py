#Implementation of queue

#Class definition for queue
class Queue:
  #constructor to initialise queue
  def __init__(self):
    #initialise an empty list as underlying data str
    self.queue = []
  # Method to check if queue is empty
  def isempty(self):
    #Returns true if queue is empty, otherwise False
    return self.queue = []
  # Method to enqueue (add) an element to queue
  def enqueue(self,v):
    #Append the value v to the end of self.queue lisy
    self.queue.append(v)
  #Method to dequeue(remove and return) the front element from queue
  def dequeue(self):
    #Initialise the variable v as none
    v = None
    # Check if the queue is not empty
    if not self.isempty():
      #Asssign the value at the front of queue to the variable v
      v = self.queue[0]
      #Update the queue by removing the front element (at index 0)
      self.queue = self.queue[1:]
    # Return the value v
    return v
  def __str__(self) #method to provide string rep of queue
    return str(self.queue)
