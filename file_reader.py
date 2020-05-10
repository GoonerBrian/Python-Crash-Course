filePath = 'ehmatthes-pcc_2e-1.1-1-g9e7977b/ehmatthes-pcc_2e-9e7977b/chapter_10/pi_digits.txt'

# with open(filePath) as file_object:
#     contents = file_object.read()
#     print(contents)

pi_str = ''
with open(filePath) as file_object:
    for line in file_object:
        pi_str += line.strip()

print(pi_str)
