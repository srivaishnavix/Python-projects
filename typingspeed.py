from time import time 

def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors +=1
        return errors
    
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords =len(inwords)
    speed = twords/time

    return speed

def elapsedtime(stime,etime):
    time = etime - stime#endtime -starttime
    return time

if __name__ =='__main__':
    prompt = "The quick brown fox jumps over the lazy dog, showcasing all 26 letters of the alphabet. This classic sentence is not only a pangram, ensuring each key on the keyboard is used, but also a whimsical tale of an agile fox leaping over a relaxed canine companion in a playful escapade."
    print("Type this: ",prompt)
    input("Press Enter key when you are ready to check your speed!!")

    stime = time()
    inprompt = input()
    etime = time()


    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)


    print("Total time elapsed: ", time, "seconds")
    print("Your average typing speed is: ", speed, "wpm(words per minute)")
    print("with the total of ", errors, "errors")