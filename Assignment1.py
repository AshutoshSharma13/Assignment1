#%%
f = open("file.txt")
a = f.read().split(' ')


d = {}
for i in a:  
    if  d.get(i) is None:
         d[i] = 1 
    else:    
        d[i] = d[i]+1
        
for i,j in d.items():
    print(i+" "+str(j))
       
fh.close()

# %%
