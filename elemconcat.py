def concat(listInput):
    elements = listInput.split(", ")
    combos = []

    for i in range(len(elements)):
        for j in range(i, len(elements)):
            combos.append(f"{elements[i]} + {elements[j]}")


    print(combos)
    

userInput = input("Enter a comma separated list of strings:")
concat(userInput)