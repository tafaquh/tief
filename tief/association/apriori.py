from .calc import support, itemFreq
import itertools
import numpy as np
import pandas as pd

dataset = []

def getSupportwithFilter(dataset, min_sup = 0.5):
  result = []
  for data in dataset:
    supp = support(data) if isinstance(data, list) else support([data])
    if supp >= min_sup:
      result.append([data, itemFreq(data), supp])
  return result

def getCombination(arr, k):
  return list(map(list, itertools.combinations(arr, k)))

def getUnique(arr):
  return list(set(x for l in arr for x in l))

def apriori(data, min_support=0.5):
  global dataset
  dataset = getUnique(data)
  all_support = []

  data_filtered = np.array(getSupportwithFilter(dataset, min_support))[:,0]

  for i in range(1,4):
    #Get Combination
    combi = getCombination(data_filtered, i)
    all_support.extend(getSupportwithFilter(combi, min_support))
  return pd.DataFrame(all_support, columns=['ItemSet', 'Count', 'Support'])