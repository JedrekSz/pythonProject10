def bin(x):
    liczba = ""
    while x != 0:
        liczba = str(x%2) + liczba
        x = int(x/2)
    return liczba


print("Adres IP:")
ip=int(input())

print("Maska:")
maska=int(input())

ipZmiana=[]
ipZmiana=bin(ip)
print(ipZmiana)

maskaZmiana=[]
maskaZmiana=bin(maska)
print(maskaZmiana)
