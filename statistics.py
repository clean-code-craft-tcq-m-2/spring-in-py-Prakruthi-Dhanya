import statistics

def calculateStats(numbers):
  avg=sum(numbers)/len(numbers)
  maximum=max(numbers)
  minimum=min(numbers)
  return avg,maximum,minimum
