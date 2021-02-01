def nthLetter(w,n):
    if w[n]:
        return w[n-1]
    else:
        return False

print(nthLetter("camera",1))

