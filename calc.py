import numpy as np,sys

#BALANCING
def balancing(b,m,n):return np.column_stack((b,np.matrix([[0 for j in range(m-n)] for i in range(m)]))) if m>n else np.row_stack((b,np.matrix([[0 for j in range(n)] for i in range(n-m)]))) if n>m else b
#MAXIMUM PROFIT
def max_profit(b):return np.max(b)-b
#ROW_COL_ALLOCATION
def r_c_all(b,c,d,m,y):
    print(m)
    for i in range(m):
        e=0
        for j in range(m):
            if y==0:a,a1=i,j
            else:a,a1=j,i
            if b[a,a1]==0 and [a,a1] not in d:e+=1
        if e==1:
            for j in range(m):
                if y == 0:a,a1 = i, j
                else:a, a1 = j, i
                if [a,a1] not in d and b[a,a1]==0:c.append([a,a1]);d.extend([[k,a1] if y==0 else [a,k] for k in range(m)]);break
    return c,d
#VERIFICATION
def verification(b,d,m):return False if len([[i, j] for i, j in zip(np.where(b == 0)[0], np.where(b == 0)[1]) if[i, j] not in d and b[i, j] == 0]) == 0 else True
#DIAGONAL
def diagonal(b,c,d,m):
    c1=[]
    for i in range(m):
        for j in range(m):
            if [i,j] not in d and b[i,j]==0:
                [d.append([i,i2]) for i2 in range(m)];[d.append([i2,j]) for i2 in range(m) if [i2,j]!=[i,j]]
                a1,a2=i+1,j+1
                while a1<m and a2<m and b[a1,a2]==0 and [a1,a2] not in d:c1.append([a1,a2]);a1,a2=a1+1,a2+1
                a1,a2=i+1,j-1
                while a1<m and b[a1,a2]==0 and [a1:=a1+1,a2:=a2-1] not in d:c1.append([a1,a2]);a1,a2=a1+1,a2+1
                c.extend([[i,j],c1[0]]);[d.append([i2,c1[0][1]]) for i2 in range(m)];[d.append([c1[0][0],i2]) for i2 in range(m) if [i2,c1[0][0]]!=c1[0]]
                for i1 in range(2): c, d = r_c_all(b,c, d, max, 0);c, d = r_c_all(b,c, d, max, 1)
                return c,d
#MANIPULATION
def manipulation(b,d,m):
    c1,min1=[],1000
    [[c1.append([i, j]) for j in range(m) if [i, j] not in d] for i in range(m)]
    [min1:=b[i[0],i[1]] for i in c1 if b[i[0],i[1]]<min1]
    for i in c1:b[i[0],i[1]]-=min1
    for i in d:
        if d.count(i)==2:b[i[0],i[1]]+=min1;d.remove(i)
    return b
#COST
def cost(c,m,x,b1,b2):return [[[j[0]+1,j[1]+1] for j in c if j[0]==i] for i in range(m)]

def matcal(c2,x,m,n):
    m=int(m)
    b2=(b:=np.matrix(c2)).copy()
    #MAXIMUM PROFIT
    if x==1:b=max_profit(b)
    #BALANCING
    b1=(b:=balancing(b,m,n)).copy()
    #ROW_REDUCTION
    for i in range(mx:=max(m,n)):b[i]-=np.min(b[i])
    b=np.transpose(b)
    #COLUMN_REDUCTION
    for i in range(mx):b[i]-=np.min(b[i])
    b,c=np.transpose(b),[]
    #ALLOCATION
    while len(c)<mx:
        c,d=[],[]
        for i in range(2):c,d=r_c_all(b,c,d,mx,0);c,d=r_c_all(b,c,d,mx,1)
        if verification(b,d,mx):c,d=diagonal(b,c,d,mx)
        if len(c)<mx:b=manipulation(b,d,mx)
        else:return cost(c,mx,x,b1,b2)
    else:return cost(c,mx,x,b1,b2)
    