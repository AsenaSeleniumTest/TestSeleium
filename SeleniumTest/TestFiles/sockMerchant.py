
def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    sample_list = set(ar)
    sample_list=list(sample_list)
    suma_socks = []
    total_pairs=0
    print(sample_list)
    for val_sample in range(len(sample_list)):
        for data in range(len(ar)):
            if sample_list[val_sample]==ar[data]:
                pair_count=pair_count+1
        suma_socks.append(int(pair_count))
        pair_count=0          
    for indice in range(len(suma_socks)):
       # if suma_socks[indice]%2!=0:
            total_pairs += suma_socks[indice]//2 
            
    print(suma_socks)
    print(total_pairs)            
    return total_pairs

sockMerchant(10,[1,1,3,1,2,1,3,3,3,3])