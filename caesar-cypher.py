logo = '''

  .oooooo.                                                         
 d8P'  `Y8b                                                        
888           .oooo.    .ooooo.   .oooo.o  .oooo.   oooo d8b       
888          `P  )88b  d88' `88b d88(  "8 `P  )88b  `888""8P       
888           .oP"888  888ooo888 `"Y88b.   .oP"888   888           
`88b    ooo  d8(  888  888    .o o.  )88b d8(  888   888           
 `Y8bood8P'  `Y888""8o `Y8bod8P' 8""888P' `Y888""8o d888b          
                                                                   
                                                                   
                                                                   
  .oooooo.                          oooo                           
 d8P'  `Y8b                         `888                           
888          oooo    ooo oo.ooooo.   888 .oo.    .ooooo.  oooo d8b 
888           `88.  .8'   888' `88b  888P"Y88b  d88' `88b `888""8P 
888            `88..8'    888   888  888   888  888ooo888  888     
`88b    ooo     `888'     888   888  888   888  888    .o  888     
 `Y8bood8P'      .8'      888bod8P' o888o o888o `Y8bod8P' d888b    
             .o..P'       888                                      
             `Y8P'       o888o                                     
                                                                   

'''
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_again = True


def encrypt(text, shift_n):
    encrypted_text = ""
    original_alpha = alphabet
    shifted_alpha = alphabet[shift_n:] + alphabet[:shift_n]
    text = text.split(" ")
    for word in text:
        encrypted_word = []
        for item in word:
            if item in original_alpha:
                index = original_alpha.index(item)
                encrypted_word += shifted_alpha[index]
            else:
                encrypted_word += item

        encrypted_w = "".join(encrypted_word)
        encrypted_text += (encrypted_w + " ")

    print(f"\n\n Your encrypted message reads: \n {encrypted_text} \n")


def decrypt(text, shift_n):
    decrypted_text = ""
    original_alpha = alphabet
    shifted_alpha = alphabet[-shift_n:] + alphabet[:-shift_n]
    text = text.split(" ")
    for word in text:
        decrypted_word = []
        for item in word:
            if item in original_alpha:
                index = original_alpha.index(item)
                decrypted_word += shifted_alpha[index]
            else:
                decrypted_word += item

        decrypted_w = "".join(decrypted_word)
        decrypted_text += (decrypted_w + " ")

    print(f"\n\n Your decrypted message reads: \n {decrypted_text} \n")


while run_again == True:
    direction = input(
        "\nType 'encode' to encrypt your message or 'decode' to decrypt it:\n --: ").lower()

    text = input("\nType your message here:\n --: ").lower()
    shift = int(input("\nKey in the shift number:\n --: "))

    if direction == "encode":
        encrypt(text=text, shift_n=shift)
    elif direction == "decode":
        decrypt(text=text, shift_n=shift)
    else:
        print("\That is not an acceptable option! ")

    answer = input(
        "\nWould you like to run it again? Type yes or no:\n --:").lower()

    if answer == "yes":
        run_again = True
    else:
        run_again = False
