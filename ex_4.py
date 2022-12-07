
read_file = open('dddaattta.txt','r')
data = read_file.readline()
read_file.close()

def codingFile(data):
    coding = ""
    i = 0
    while (i <= len(data)-1):
        count = 1
        char = data[i]
        j = i
        while (j < len(data)-1): 
            if (data[j] == data[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        coding = coding + str(count) + char
        i = j + 1
    f = open('3d2a3ta.txt','w')
    f.write(str(coding))
    f.close() 

# Запуск кодирования
codingFile(data)

read_file = open('3d2a3ta.txt','r')
dedata = read_file.readline()
read_file.close()


def decodingFile(data):
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
       
    f = open('decoded.txt','w')
    f.write(str(decode))
    f.close() 

# Запуск де-кодирования
decodingFile(dedata)
