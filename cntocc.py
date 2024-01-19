inp_str=input("enter strings:")
freq={}
for ele in inp_str:
    if ele in freq:
        freq[ele]+=1
    else:
        freq[ele]=1
print("occurance of all characters:\n "+ str(freq))        
