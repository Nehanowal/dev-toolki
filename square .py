def canFormSquare(l1, b1, l2, b2, l3, b3):
    # Return "YES" if the rectangles can be arranged to form a square, otherwise return "NO"
   
    if l1==l2==l3 and b1+b2+b3==l1:
       return "YES"
    if b1==b2==b3 and l1+l2+l3==b1:
        return "YES"
        
    if l1+l2==b1 and l2==l3 and b3 +b2==b1 :
        return "YES"

    if b1+b2==l1 and b2==b3 and l3 +l2==l1 :
        return "YES"
    else:
        return "NO"
