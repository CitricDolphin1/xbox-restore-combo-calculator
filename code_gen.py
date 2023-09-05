import hmac
import struct

string_hdd_key = input("Input your HDD key in hexidecimal now, no spaces: ")
hdd_key = bytearray.fromhex(string_hdd_key)

# hardcoded constant
random_key = bytearray.fromhex('BC20051AB597F96048375A83787FE594')

key_combo_generator_hmac = hmac.new(random_key, hdd_key, 'sha1')
key_combo_generator_digest = bytearray.fromhex(key_combo_generator_hmac.hexdigest())

recovery_key_map = "AXYUDLR"

button_indexes = []

digest_counter = 0
for i in range(4):
    word_int = struct.unpack('H', key_combo_generator_digest[digest_counter:digest_counter+2])[0]
    button_index = word_int % 7
    button_indexes.insert(0, button_index)
    digest_counter += 2

buttons = []
for index in button_indexes:
    buttons.append(recovery_key_map[index])

print(f'Your button combo is: Y{buttons[0]}{buttons[1]}{buttons[2]}{buttons[3]}')
print('To use this buttom combo, go to the System Info screen of your dashboard and input the button combo.')
print('Directions (U,D,L,R) should be performed on the left stick.')
