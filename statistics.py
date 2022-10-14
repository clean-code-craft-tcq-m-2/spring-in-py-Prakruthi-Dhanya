import statistics

def calculateStats(numbers):
  avg=sum(numbers)/len(numbers)
  max=max(numbers)
  min=min(numbers)
  return avg,max,min
