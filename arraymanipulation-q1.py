# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:53:35 2022

@author: RUMEYSA
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

arr_zeros = [] #boş dizi tanımlandı# n ile aynı boyutta, queries'in ilk dizindeki ilk elemanı, sıfırlardan oluşan tek boyutlu bir liste oluşturuldu. n boyutlu bir dizi

def inpt_constraints(adim_sys,user_inp,eleman_s,n):  #input kısıtlarına uygunluk kontrolü yapılır.

#eleman sayısına göre kısıt kontolü değişiyor -- 1. indexde 2 değerin girilmiş olması, 2 ve sonraki indexlerde 3 elemanın girilmiş olması gerekir.
# =============================================================================
#    İnput içim kısıtlar:
#    
#    tüm değerler int olmalı
#    n,m,a,b,k değerleri girildiği
#    3 <= n <= 10^7
#    1 <= m <= 2*(10)^5
#    1 <= a <= b <= n
#    0 <= k <=10^9
# =============================================================================
   
    if adim_sys==0:
       
       if eleman_s != 2:
           print("2 eleman aralarında boşluk olacak şekilde girilmelidir!")
           return False
       
       else:
           try:
               n = int(n)
               m = int(user_inp[1])
               
               if 3 <= n <= 10**7 and 1 <= m <= 2*(10**5):
                   return True
                   
               else:
                   print("n veya m değeri olması gereken aralıkta değildir!")
                   return False
                   
           except:
               print("girilen değerler rakamlardan oluşmalıdır!")
               return False
           
    else:  #adim sayısı 1 den fazla olduğunda yani a b k değerleri için kontrol 
        if eleman_s != 3:
           print("3 eleman aralarında boşluk olacak şekilde girilmelidir!")
           return False
       
        else:
            try: 
            
                a = int(user_inp[0])
                b = int(user_inp[1])
                k = int(user_inp[2])
                n = int(n)
                                  
            except:
                print("girilen değerler rakamlardan oluşmalıdır!")
                return False
           
            else:
                
                if 1 <= a <= b <= n and 0 <= k <= 10**9 :
                    return True
                   
                else:
                    print("a,b veya k değeri olması gereken aralıkta değildir!")
                    return False
   
def arrayManipulation(n,queries):
            
    m = queries[0][1]   # kaç adım tekrarlanacağı belirlendi.  
    for i in range(0,m): 
        a= queries[i+1][0]
        b= queries[i+1][1]
        
        #print("a: {0} , b: {1}, m-operasyon: {2}".format(a, b, m))
        for i_zero in range(0,((b-a)+1)):
            arr_zeros[a+i_zero-1] += queries[i+1][2] 
    
        m -=1 #bir operasyon tamamlandı
        
    for sonuc_i in range(len(arr_zeros)):
        if(arr_zeros[sonuc_i] > arr_zeros[sonuc_i-1]):
            enbuyukdeger = arr_zeros[sonuc_i]           
    return  int(enbuyukdeger)      # integer değer döndürmeli                                           



# Kullanıcıya 2 seçenek sunulur - Örnek input ile işlem mi yapmak istersen 1, İnput girmek istersen 2'yi tuşla 

user_choice = None #söngüye girmesi için bu değer atandı
    
while user_choice not in {1,2}:
    
      
    try:
        user_choice = int(input("Örnek input ile işlem mi yapmak istersen 1, İnput girmek istersen 2'yi tuşla!\n"))
                  
    except:
        pass
        
    else:    
           
        if user_choice == 1:
            queriesx= [ [5,5], [1, 2, 100] ,[2 ,5 ,100] ,[3, 4, 100], [2, 3, 300], [1, 3, 600] ] #kullanıcı girişinden elde edilen son dizidir. 1. maddeyi yap daha sonra!
            #0'larda oluşan 1 boyutlu dii oluştur
            arr_zeros = [0]*queriesx[0][0] 
            print("listedeki en büyük değer: ",arrayManipulation(len(queriesx),queriesx))  #func. çağrılıyor.
            break;
            
        elif user_choice == 2:

            input_text = (""" 
                  Değerleri aşağıdaki örnekte oluduğu gibi girmelisiniz.
                  n= dizinin boyutu  ; m= opreasyon sayısı(dizi kaç kere manipüle edilecek
                  a= sol index ; b= sağ index örn 2 5 => 2. ve 5. index dahil arasındaki değerler ; k= eklenecek sayı
                    [n m] 
                    [a b k]
                    [a b k]
                    [a b k]
                    [a b k]
                    [a b k] 
                    
                    Dizi elemanlarının hepsi integer olmalı ayrıca aşağıdaki kısıtlara uyulmalıdır.
                    3 <= n <= 10^7
                    1 <= m <= 2*(10)^5
                    1 <= a <= b <= n
                    0 <= k <= 10^9 \nHer satır sonrası enter'a basınız.\nn m değeri: """)
            
            queriesx = [] # tüm inputu içeren dizi /  fonksiyona parametre gönderilen dizi      

            inpt_client = input(input_text)
            user_inp = inpt_client.split()
            n_deger = user_inp[0]
            eleman_s = len(user_inp)
            #print("eleman_s: ",eleman_s)
            adim_sys= 0  #hangi index giriliyor
            uygunluk_inpt= inpt_constraints(adim_sys,user_inp,eleman_s,n_deger)  # input kısıtlarına uygunluk kontrolü yapan fonksiyon çağrılır.
            
            if uygunluk_inpt == False:
               break
                
            else:  #diziye girilen değerler kısıtlara uyuyorsa hesaplama yapılır
                               
                queriesx.insert(0, list(int(num) for num in inpt_client.strip().split())[:2])
    
                for list_i in range(1,(queriesx[0][1]+1)):
                    
                    inpt_clientx = input("{0}. eleman: ".format(list_i))
                    user_inpx = inpt_clientx.split()
                    eleman_sx = len(user_inpx)
                    adim_sysx = list_i  #hangi index giriliyor
                    uygunluk_inptx= inpt_constraints(adim_sysx,user_inpx,eleman_sx,n_deger)  # input kısıtlarına uygunluk kontrolü yapan fonksiyon çağrılır.  
                    
                    if uygunluk_inptx == False:
                       break
                
                    else:
                        queriesx.insert(list_i, list(int(num) for num in inpt_clientx.strip().split())[:3])
                
                if uygunluk_inptx:
                    #0'larda oluşan 1 boyutlu dizi oluştur
                    arr_zeros = [0]*queriesx[0][0]        
                    print("listedeki en büyük değer: ",arrayManipulation(len(queriesx),queriesx))  #func. çağrılıyor.
                
                else:
                    pass
            
        else:
           pass
      
         
