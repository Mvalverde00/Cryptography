def bruteforce(string):
    for radius in range(2,len(string)//2):
        print("With radius " + str(radius))
        
        for i in range(radius):
            s = ""
            
            for j in range((len(string)//radius)+1):

                # Horribly inefficient, but the first solution I could come up with
                # Efficiency isn't really an issue with soemthing like this anyway
                try:
                    s += string[radius*j+i]
                except IndexError:
                    pass
                
            print(s)
        print("====================")

                

string = "CLNGTDHOBOABTCLTFLNTRHOUHTEGIEEDCEHMROAFEKRESANKIGWEPEDSIROISRTUONSOTTO"
bruteforce(string)

