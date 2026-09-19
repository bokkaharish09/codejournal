alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
direction = input("Enter 'ENCODE' to encrpyt & 'DECODE' to decrypt").lower()
input_text=input("Enter Your Message!").lower() #convert everything in lower case
shift=int(input("Enter the shift number:"))

def encrypt(og_text,shift_pattern):
    en_text=''    
    for i in og_text:
        shift_pos=alphabet.index(i)+shift_pattern
        en_text+=alphabet[shift_pos]

    print(f"here is your encrypted result {en_text}")    

def decrypt(og_text,shift_pattern):
    dy_text=''    
    for i in og_text:
        shift_pos=alphabet.index(i)-shift_pattern
        dy_text+=alphabet[shift_pos]

    print(f"here is your encrypted result {dy_text}")    

if direction=='encode':
    encrypt(input_text,shift)
elif direction=='decode':
    decrypt(input_text,shift)
else:
    print("Error in direction")

