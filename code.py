def encrypt(m,s):
  count = 0 
  result = ""
  for i in range(len(m)):
    char = m[i]
    
    if(char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
      
    if((i%5==0)) and (i>0):
      result = result + " "
      count += 1
      
    if(count==10):
      print(result)
      count = 0
      result = ""
      
  return result

shift = 0

message = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."

shift = int(input("Enter a shift amount: "))

message = message.upper()
encode = encrypt(message,shift)