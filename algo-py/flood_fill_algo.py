# Python3 program for above approach
 
# Function to check valid coordinate
def validCoord(x, y, n, m):
    if x < 0 or y < 0:
        return 0
    if x >= n or y >= m:
        return 0
    return 1
 
# Function to run bfs
def bfs(n, m, data, X, Y, color):
   
  # Visiting array
  vis = [[0 for i in range(101)] for j in range(101)]
     
  # Creating queue for bfs
  obj = []
     
  # Pushing pair of {x, y}
  obj.append([X, Y])
     
  # Marking {x, y} as visited
  vis[X][Y] = 1
     
  # Until queue is empty
  while len(obj) > 0:
     
    # Extracting front pair
    coord = obj[0]
    x = coord[0]
    y = coord[1]
    preColor = data[x][y]
   
    data[x][y] = color
       
    # Popping front pair of queue
    obj.pop(0)
   
    # For Upside Pixel or Cell
    if validCoord(x + 1, y, n, m) == 1 and vis[x + 1][y] == 0 and data[x + 1][y] == preColor:
      obj.append([x + 1, y])
      vis[x + 1][y] = 1
       
    # For Downside Pixel or Cell
    if validCoord(x - 1, y, n, m) == 1 and vis[x - 1][y] == 0 and data[x - 1][y] == preColor:
      obj.append([x - 1, y])
      vis[x - 1][y] = 1
       
    # For Right side Pixel or Cell
    if validCoord(x, y + 1, n, m) == 1 and vis[x][y + 1] == 0 and data[x][y + 1] == preColor:
      obj.append([x, y + 1])
      vis[x][y + 1] = 1
       
    # For Left side Pixel or Cell
    if validCoord(x, y - 1, n, m) == 1 and vis[x][y - 1] == 0 and data[x][y - 1] == preColor:
      obj.append([x, y - 1])
      vis[x][y - 1] = 1
     
  # Printing The Changed Matrix Of Pixels
  for i in range(n):
    for j in range(m):
      print(data[i][j], end = " ")
    print()
  print()
 
n = 8
m = 8
 
data = [
  [ 1, 1, 1, 1, 1, 1, 1, 1 ],
  [ 1, 1, 1, 1, 1, 1, 0, 0 ],
  [ 1, 0, 0, 1, 1, 0, 1, 1 ],
  [ 1, 2, 2, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 2, 2, 0 ],
  [ 1, 1, 1, 1, 1, 2, 1, 1 ],
  [ 1, 1, 1, 1, 1, 2, 2, 1 ],
]
 
x, y, color = 0, 0, 7
 
# Function Call
bfs(n, m, data, x, y, color)