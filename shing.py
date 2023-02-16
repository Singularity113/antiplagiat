import binascii

source =  'Разум дан человеку для того, чтобы он разумно жил, а не для того только, чтобы он понимал, что он неразумно живет.'
words = source.split()
text = []
for word in words:
    text.append(word)

shingleLen = 2 #длина шингла     
out = []      
for i in range(len(text) - (shingleLen - 1)):
    shingle = [x for x in text[i:i + shingleLen]]
    out.append(shingle)

# # хеширование
# hash = []
# for el in out:
#     hash.append(binascii.crc32(' '.join(el).encode('utf-8')))

print(out)