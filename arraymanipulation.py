# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


arr_zeros = [] #boş dizi tanımlandı# n ile aynı boyutta, queries'in ilk dizindeki ilk elemanı, sıfırlardan oluşan tek boyutlu bir liste oluşturuldu. n boyutlu bir dizi


def arrayManipulation(n,queries):
            
    m = queries[0][1]   # kaç adım tekrarlanacağı belirlendi.  
  
    for i in range(0,n-1): 
        if m > 0 :
            a= queries[i+1][0]
            b= queries[i+1][1]
            print("a: {0} , b: {1}, m-operasyon: {2}".format(a, b, m))
            for i_zero in range(0,((b-a)+1)):
                arr_zeros[a+i_zero-1] += queries[i+1][2] 
        
            m -=1 #bir operasyon tamamlandı
            #print("operasyon adımı: ",m)
            print(arr_zeros)      
            #return arrayManipulation(n-1,queries)      # for dögüsü gibi her adım için fonsiyonu çağırıp işlem yapıyor - recursive func.
                                                        # func'un kaç kere döneceği, input queries'indeki m e bağlı
        else: 
          pass

    for sonuc_i in range(len(arr_zeros)):
        if(arr_zeros[sonuc_i] > arr_zeros[sonuc_i-1]):
            enbuyukdeger = arr_zeros[sonuc_i]           
    return  int(enbuyukdeger)      # integer değer döndürmeli                                           


# input aşağıdaki gibi olmalı 
# ilk satırdaki veri dizinin boyutu ve operasyon sayısı ile ilgilidir. 
# a= sol index ; b= sağ index örn 2 5 => 2. ve 5. index dahil arasındaki değerler ; k= eklenecek sayı

# n= dizinin boyutu  ; m= opreasyon sayısı(dizi kaç kere manipüle edilecek) 
"""
   [n,m] 
   [a,b,k]
   [a,b,k]
   [a,b,k]
   [a,b,k]
   [a,b,k]
   
"""


#input    
#queries= [ [5,4], [1, 2, 100] ,[2 ,5 ,100] ,[3, 4, 100], [2, 3, 300], [1, 3, 600] ] #kullanıcı girişinden elde edilen son dizidir. 1. maddeyi yap daha sonra!

# 1- QUERIES elemanları aralarında boşluk olarak kullanıcı input girecektir. Onları bir diziye ata böylece yukarıdaki mantık çalışır.


# user_input = input("""
#       Değerleri aşağıdaki örnekte oluduğu gibi girmelisiniz.
#       n= dizinin boyutu  ; m= opreasyon sayısı(dizi kaç kere manipüle edilecek) 
#         [n m] 
#         [a b k]
#         [a b k]
#         [a b k]
#         [a b k]
#         [a b k] \ninput: """)

       
#list_input = user_input.split()

#print('list: ', list_input)

#for i_input in range(len(list_input)):
#    list_input[i_input] = int(list_input[i_input])
                 
#print("Sum = ", sum(list_input))

# lazım print("listedeki en büyük değer: ",arrayManipulation(len(queries),queries))  #func. çağrılıyor.

#print("size of array:",len(queries))

#deger = int(input("Enter the list size "))
               

# =============================================================================
# user_girdi = input("""
#       Değerleri aşağıdaki örnekte oluduğu gibi girmelisiniz.
#       n= dizinin boyutu  ; m= opreasyon sayısı(dizi kaç kere manipüle edilecek
#       a= sol index ; b= sağ index örn 2 5 => 2. ve 5. index dahil arasındaki değerler ; k= eklenecek sayı
#         [n m] 
#         [a b k]
#         [a b k]
#         [a b k]
#         [a b k]
#         [a b k] \ninput: """)
# =============================================================================

# girdi_list = user_girdi.split()

# #m ve n değerleri diziye atandı
# queries_nm=[]

# for n_m in range(len(girdi_list)):
#     queries_nm.insert(n_m,girdi_list)
# #print("print n m : ",girdi_list_nm[n_m])

# #dizi boyutu değişkene atandı
# deger_n = int(girdi_list[0])

# # #a,b,k değerleri diziye atandı
# queries_abk=[]

# for i_input in range(deger_n): 
#     user_girdi = input("\n: ")
#     girdi_list = user_girdi.split()
#     for ikinci_index in range(0,3):
#         queries_abk.insert(i_input,girdi_list)

# #print("print a b k : ",queries_abk[3][2])    
# #print("User list is ", queries_n)

#tüm bilgileri içeren queries dizisi
# queries = []

# girdi_list_nm = user_girdi.split()

# queries.insert(0,int(girdi_list_nm))
# #print("print n m : ",girdi_list_nm[n_m])

# #dizi boyutu değişkene atandı
# deger_n = int(queries[0][0])

# for i_input in range(1,int(queries[0][0])+1):
#     user_girdi = input("\n: ")
#     girdi_list = user_girdi.split()
#     queries.insert(i_input,int(girdi_list))

# #print(queries[2][1])

#girdi_list = user_girdi.split()


# n = int(input("Enter the size of the list "))
# print("\n")
# num_list = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

# print("User list: ", type(num_list))

# print(num_list[0])


# =============================================================================
# 
# for zeros_in in range(deger_n):
#     arr_zeros.append(0)

queriesx = []
#girdi_list_nm = user_girdi.split()

# #dizi boyutu değişkene atandı
#deger_n = int(girdi_list_nm[0][0])


#print(arr_zeros)

#queries dizisi oluşturulacak
# rows, cols = (deger_n, deger_n)
# arr = [[0]*cols]*rows
# print(arr)


queriesx.insert(0, list(int(num) for num in input("Enter n m ").strip().split())[:2])


for list_i in range(1,queriesx[0][1]+1):
    queriesx.insert(list_i, list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:3])

#0'larda oluşan 1 boyutlu dii oluştur
arr_zeros = [0]*queriesx[0][0]

#print("queriesx", queriesx[0][1])
print("listedeki en büyük değer: ",arrayManipulation(len(queriesx),queriesx))  #func. çağrılıyor.
# 
# =============================================================================



# SIRADAKİ YAPILACAKLAR LİSTESİ


# 2 seçenek sun - inputu şu şekilde girin ya da örnek değer için dönndürün 2. seçilirse örnek veri setini input olarak gönder!
""" 

inp_queries = [[1, 2, 100] ,[2 ,5 ,100] ,[3, 4, 100], [1, 2, 600] ] 
n =5
m=3 
sonuç olarak queries =  [ [5,3], [1, 2, 100] ,[2 ,5 ,100] ,[3, 4, 100], [1, 2, 600] ]  olarak gönderilsin fonksiyona

"""
# 2- input için kısıtlar vardır onları değerlendirip ona göre fonk. gönder



