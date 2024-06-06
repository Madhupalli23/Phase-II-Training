

graph={
    'A':['B','C'],
    'B':['C'],
    'C':['A','B']
    
    
}
def BFS(start,graph):
    visited=[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
     
        for i in graph[ele]:
            if i not in  visited:
                q.append(i)
                visited.append(i)
    return visited
                
            
        
    
   
res= BFS('B',graph)
print(res)