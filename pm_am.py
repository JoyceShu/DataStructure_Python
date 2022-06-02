s= "07:05:45PM"
n = len(s)


time = s[(n-2):n]
ans =''
if time == 'PM':
    first = int(s[:2])
    if first < 12:
        first += 12
        new = str(first)
    else:
        new = '00'
    ans = new + ":" + s[3:(n-2)]
else:
    ans += s[:(n-2)]
print(ans)
            
