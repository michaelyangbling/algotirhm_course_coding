# problem :https://www.hackerrank.com/contests/neuf17-pa1/challenges/battle-of-states/problem

"""
Since this is based on adjacent list . This algotirhm get strongly connected components(SCCs)
, convert SCCs into Directed Acyclic Graph, and calculate the maximum of "longest path" ending in each node through topographical sorting. The time and space complexity are both O(m+n)
"""
g=[]
n=int(input())
'''while True:
     g.append(list(map(int, input().split())))  # g is a list of lists
     if len(g[len(g)-1])==0:
         break
'''
while True:
    try:
      g.append(list(map(int, input().split())))  # g is a list of lists
    except EOFError:
      break

#g.pop()     #delete last empty list
graph={}     #graph is a dictionary

for i in range(1,n+1):
    graph[i]=set([])
for j in range(0,len(g)):     # form adjacent list
    graph[g[j][0]].add(g[j][1])

unvisited=set(range(1,n+1))  #set of unvisited nodes
finish=[]  #order of finish time

def DFS1(node):
    global unvisited
    global finish
    unvisited.remove(node)
    for k in graph[node]:
        if k  in unvisited:
            DFS1(k)
    finish.append(node)

while len(unvisited)>0:#   run DFS1  on original graph
    a=unvisited.pop()
    unvisited.add(a)
    DFS1(a)

finish.reverse()    # reverse finish time

rgraph={}     #form reverse graph
for i in range(1,n+1):
    rgraph[i]=set([])
for j in range(0,len(g)):     # form adjacent list
    rgraph[g[j][1]].add(g[j][0])

scc=[]    #list for strongly connected components
compo=set([])   # a strongly connected component
status={}          #record status of node in reverse graph
for i in range(1,n+1):
    status[i]=0          # 0: unvisited   1: visited

def DFS2(node):
    global rgraph
    global status
    global compo
    compo.add(node)
    status[node]=1
    for k in rgraph[node]:
        if status[k]==0:
            DFS2(k)

pivot=0
while pivot<=n-1:     #   run DFS2  on reverse graph
    if status[finish[pivot]]==0:
        compo=set([])
        DFS2(finish[pivot])
        scc.append(compo)
    pivot=pivot+1

whichcompo={}        # record which component a node belongs to
for i in range(0,len(scc)):  # determine which component a node belongs to
        for  j  in scc[i]:
            whichcompo[j]=i

dag={}
for i in range(0,len(scc)):   #form "DAG graph" of SCCs for original graph
    dag[i]=set([])
for i in graph:
    for j in graph[i]:
        a=whichcompo[i];b=whichcompo[j]
        if a!=b:
            dag[a].add(b)
unvisited2=set(range(0,len(dag)))  #set of unvisited nodes
finish2=[]  #order of finish time

def DFS3(node):
    global unvisited2
    global finish2
    unvisited2.remove(node)
    for k in dag[node]:
        if k  in unvisited2:
            DFS3(k)
    finish2.append(node)

while len(unvisited2)>0:   #   run DFS3
    b=unvisited2.pop()
    unvisited2.add(b)
    DFS3(b)
finish2.reverse()

longest={}
for i in finish2:# longest: store current longest path ending in  each node
  longest[i]=0

for i in finish2:   #get longest path ending in  each node
    for j in dag[i]:
        longest[j]=max(longest[i]+1, longest[j])

path=0
for i in longest:
    if longest[i]>path:
        path=longest[i]
print(path+1)