text = "alice is a good girl she is a good student"
first = "a"
second = "good"

words = text.split()
s=[]
for i in range(len(words)-2):
    # Check if the current word matches the 'first' or 'second' word
    if words[i] == first and words[i+1] == second:
        s.append(words[i+2])
    
print(s)