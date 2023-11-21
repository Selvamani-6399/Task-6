#Find all triplets in a list with given sum in Python
def SumTriplets(listA, sum):
   trpltcnt = 0
   res = []

   for i in range(0, len(listA) - 1):

      s = set()
      tmp = []

      # Adding first element
      tmp.append(listA[i])

      current_sum = sum - listA[i]

      for j in range(i + 1, len(listA)):

         if (current_sum - listA[j]) in s:
            trpltcnt += 1

            # Adding second element
            tmp.append(listA[j])

            # Adding third element
            tmp.append(current_sum - listA[j])

            # Appending tuple to the final list
            res.append(tuple(tmp))
            tmp.pop(2)
            tmp.pop(1)
         s.add(listA[j])

   return res


listA = [4,2,-3,1,6]

print("Required triplets:\n",SumTriplets(listA,0))