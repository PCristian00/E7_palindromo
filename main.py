def palindromo(stringa):
    indice = (len(stringa) - 1)
    i = 0
    while indice >= 0:
        if stringa[indice] == stringa[i]:
            i += 1
        indice -= 1
    if i == (len(stringa)):
        print("Palindromo")
    else:
        print("Non palindromo")


s = input("Inserire stringa: ")
palindromo(s)
