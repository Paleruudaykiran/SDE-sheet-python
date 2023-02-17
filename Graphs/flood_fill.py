import queue
class Solution:
    def floodFill(self, image, sr, sc, color):
        q = queue.Queue() 
        q.put((sr,sc)) 
        drow = [-1,1,0,0] 
        dcol = [0,0,1,-1]
        stclr = image[sr][sc]
        while not q.empty() :
            r,c = q.get() 
            for i in range(4) :
                nr,nc = r+drow[i],c+dcol[i] 
                if nr>=0 and nr<len(image) and nc>=0 and nc<len(image[0]) and image[nr][nc] != color and image[nr][nc] == stclr:
                    image[nr][nc] = color
                    q.put((nr,nc))
        image[sr][sc] = color
        return image