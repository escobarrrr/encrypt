saisie = str(input("text to encrypt: "))
dec = int(input("offset value "))
crypt = ""
for r in saisie :
    if r != " ":
        result = ord(r)+dec
        if ord(r) >= 97 and ord(r) <= 122:
          if result > 122 :    
            crypt += chr(result - 26)
          elif result < 97 :
            crypt += chr(result + 26)
          else:   
            crypt += chr(result)

        if ord(r) >= 65 and ord(r) <= 90:
          if result > 90 :    
            crypt += chr(result - 26)
          elif result < 65 :
            crypt += chr(result + 26)
          else:   
            crypt += chr(result)
    else :  
      crypt += " "
print(crypt)   
