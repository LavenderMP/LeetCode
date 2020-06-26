# def groupThePeople(gSizes):
#   val_result = []
#   idx_result = []
#   for i, size in enumerate(gSizes):
#     if len(val_result) == 0:
#       val_result.append([size])
#       idx_result.append([i])
#     else:
#       for j, group in enumerate(val_result):
#         if size in group and len(group) < size:
#           flaged = True
#           group.append(size)
#           idx_result[j].append(i)
#           break
#         else:
#           flaged = False
#       if not flaged:
#         val_result.append([size])
#         idx_result.append([i])
#   return idx_result

class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    adict = dict()
    result = []
    for i, size in enumerate(groupSizes):
      if size not in adict:
        adict[size] = [[i]]
        if len(adict[size]) == size:  # handle group of 1
          result.append(adict[size].pop())
          adict[size].append([])
      elif size in adict and len(adict[size][-1]) < size:
        adict[size][-1].append(i)
        if len(adict[size][-1]) == size:
          result.append(adict[size].pop())
          adict[size].append([])
      else:
        adict[size].append([i])
    return result

  class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
      adict = dict()
      result = []
      for i, size in enumerate(groupSizes):
        if size not in adict:
          adict[size] = [[i]]
        elif size in adict and len(adict[size][-1]) < size:
          adict[size][-1].append(i)
        else:
          adict[size].append([i])
      print(adict)
      for vals in adict.values():
        for val in vals:
          result.append(val)
      return result

groupSizes = [3,3,3,3,3,1,3]

print(groupThePeople(groupSizes))