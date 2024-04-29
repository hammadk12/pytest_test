names = []


def main(name):
    # name = input("What's your age? ")
    if name == "21":
        return (f"You are good to go, {name}")
       # names.append(name)
       # print(names)
       # print(age(name))
    else:
        return ("maybe in a few years buddy")
    
    

def age(to="18"):
    return f"age: {to}"

if __name__ == "__main__":
    main()