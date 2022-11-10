def encrypt(key,message):
    crypted="";
    countKey=0;
    for char in list(message):
        if countKey<len(key):
            crypted+=chr(ord(char)*ord(key[countKey]));
            countKey+=1;
        else:
            countKey=0;
            crypted+=chr(ord(char)*ord(key[countKey]));
            countKey+=1;
    return toHex(crypted);
def decrypt(key,message):
    uncrypt="";
    countKey=0;
    for byte in toDec(message):
        if countKey<len(key):
            uncrypt+=chr(int(byte/ord(key[countKey])));
            countKey+=1;
        else:
            countKey=0;
            uncrypt+=chr(int(byte/ord(key[countKey])));
            countKey+=1;
    return uncrypt;
def toHex(message):
    encode="";
    for char in list(message):
        encode+=hex(ord(char)).split("0x")[1]+" ";
    return encode;
def toDec(message):
    decode=[]
    for hexa in message.split(" "):
        decode.append(eval("0x"+hexa));
    return decode;