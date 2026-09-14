import string

cipher = input()
start_index, second_index, current_index = -1, -1, -1
change = -1
result = ''
for i in range(len(cipher)):
    if cipher[i] in string.ascii_uppercase:
        start_index = i
    if start_index != -1:
        if cipher[i] in '0123456789':
            second_index = i
            change = second_index - start_index + 1
            current_index = start_index
            while cipher[current_index] != '.':
                result += cipher[current_index]
                current_index += change
            break
print(result + '.')

# dlya komandi
# Mwqt1iyteg oxxnkelgyouieymvscbakroynokawdykrwaispk wqbr2fgmx2luei8kffy upsnonsencubdghihvaekuglnaxch pstfmrpsrnmmbbodqrrgqsmvoclau cipckdjumuxttgsyqqshtnbgatfqftuxin'ucqy yxzepmgflrgpelozhexssvafiqybbmgtoy.