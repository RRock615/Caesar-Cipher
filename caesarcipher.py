#Formula: phi(x) = sigma(0<=c<=25)f(c)p(c-i)

dict = {'a': 0.080,
        'b': 0.015,
        'c': 0.030,
        'd': 0.040,
        'e': 0.130,
        'f': 0.020,
        'g': 0.015,
        'h': 0.060,
        'i': 0.065,
        'j': 0.005,
        'k': 0.005,
        'l': 0.035,
        'm': 0.030,
        'n': 0.070,
        'o': 0.080,
        'p': 0.020,
        'q': 0.002,
        'r': 0.065,
        's': 0.060,
        't': 0.090,
        'u': 0.030,
        'v': 0.010,
        'w': 0.015,
        'x': 0.005,
        'y': 0.020,
        'z': 0.002}

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabets(letter):
    k = 0
    for j in alphabet:
        if(j == letter):
            break
        k+=1
    return k


def newChar(c,i):
    place = alphabets(c)
    value = place - i
    if value < 0:
        num = 26 + value
        return num
    else:
        return value


def cipher_calc(c, cDict, length, i):
    value = 0
    c_freq = cDict[c]

    num = newChar(c,i)
    p = dict[alphabet[num]]
    z = (float(c_freq) / float(length))*p
    return z


def c_frequency(cipher):
    char_dictionary = {}
    cipher = cipher.replace(' ','')

    while cipher:
        count = 1
        key = cipher[0]
        if(len(cipher) == 1):
            char_dictionary.update({cipher[0] : 1})
            cipher = cipher.replace(cipher[0],'')
            break

        for i in range(1,len(cipher)):
            if(cipher[i] == key):
                count += 1
                cipher = cipher.replace(cipher[i],' ')

        cipher = cipher.replace(cipher[0],'')
        cipher = cipher.replace(' ','')
        char_dictionary.update({key : count})
    return char_dictionary

def main():
	freq = []
	results = []

	print("Cryptanalysis of Caesar Cipher")
	print("---------------------------------------------")
	print("This program will give you the statistical analysis for every value i in phi_i")
	print("---------------------------------------------")
	cipher = input("Please enter your string: ") 
	print("")
	cipher = cipher.lower()
	cipher = cipher.replace(' ','')
	length = len(cipher)
	cDict = c_frequency(cipher)
	for i in range(0,26):
	    for c in cDict:
	        freq.append(cipher_calc(c,cDict,length,i))
	    results.append(sum(freq))
	    del freq[:]
	print("i |","phi_i")
	print("_________")
	for j in range(0,26):
	    print(j,"|",round(results[j],3))


if __name__ == "__main__":
	main()



