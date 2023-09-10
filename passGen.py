import string
import sys
import random
print("\n=============================\n|| PassGen @KuliOnline0011 ||\n=============================\n")
t1 = list(string.ascii_lowercase)
t2 = list(string.ascii_uppercase)
t3 = list(string.digits)
t4 = list(string.punctuation)
cek = sys.argv
pwd = t1+t2+t3+t4
yuhu = "Inputan tidak jelas"

# for a in t4:
#     print(a)

if len(sys.argv) < 2:
    print("Bantuan:\n        passGen.py -h\n        passGen.py --help\n")
elif len(sys.argv) >= 2:
    if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
        print("Haram-Code\nPassword Generator berdasarkan panjang karakter\nCara penggunaan:\n                PassGen.py [Panjang digit]\n")
    elif sys.argv[1].isnumeric():
        try:
            pjPasswd = int(sys.argv[1])
            if pjPasswd < 8:
                print("Panjang password wajib minimal 8 digit")
            else:
                random.shuffle(t1)
                random.shuffle(t2)
                random.shuffle(t3)
                random.shuffle(t4)
                passwd1 = round(pjPasswd * (30/100))
                passwd2 = round(pjPasswd * (20/100))
                
                jwbn=[]
                for a in range(passwd1):
                    jwbn.append(t1[a])
                    jwbn.append(t2[a])
                for b in range(passwd2):
                    jwbn.append(t3[b])
                    jwbn.append(t4[b])
                
                # print(jwbn)
                random.shuffle(jwbn)
                password = "".join(jwbn)
                print("Password anda: ", password,"\n")
                # print("Panjang Password: ",pjPasswd,"\n")
                
        except:
            print("Program close ya\n")
    else:
        print(yuhu,"\n")
else:
    print(yuhu,"\n")