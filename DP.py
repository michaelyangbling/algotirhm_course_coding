#https://www.hackerrank.com/contests/neuf17-pa2/challenges/the-gold-rush/problem
# this algorithm uses dynamic programming to store calculated max gold from position 0 to position i
#we can just take the max gold from last position to get the final result
#Thus, time complexity is O(n^2), space complexity is O(n)

def dist(x1,y1,x2,y2): #calculate distance
  return ((x1-x2)**2+(y1-y2)**2)**0.5


def max_gold():
  num = int((input()))
  gold = {}  #the gold map is stored in dict
  for i in range(0,num):
    gold[i]=list(map(int, input().split()))  # [ x_coord, y_coord, Gi]
  if num==1:
      return gold[0][2]
  if num==2:
      return gold[0][2]+gold[1][2]-dist(gold[0][0],gold[0][1],gold[1][0],gold[1][1])
  maxgold=[0]  #max gold excluding first and last gold
  for i in range(1,num-1):
      max=gold[i][2]-dist(gold[0][0],gold[0][1],gold[i][0],gold[i][1])
      for j in range(1,i):
          another=maxgold[j]+gold[i][2]-dist(gold[j][0],gold[j][1],gold[i][0],gold[i][1])
          if another>max:
              max=another
      maxgold.append(max)
  max=-dist(gold[0][0],gold[0][1],gold[num-1][0],gold[num-1][1])
  for j in range(1, num-1): # calulate for last gold location
      another=maxgold[j] - dist(gold[j][0], gold[j][1], gold[num-1][0], gold[num-1][1])
      if another > max:
          max = another
  return max+gold[num-1][2]+gold[0][2]
print(round(max_gold(),6))