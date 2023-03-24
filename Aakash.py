"""
Step1: Input the elements in number
step2: create an empty list
step3: use while condition
step4: while the user entered the less than the 0 the loop need to end
step5: in the remainder equals to remainder%2 for getting the last element
step6: number it is need to find the quation and again it need to run in the loop
step7: again append the number
step8: Finally using for loop to print the elements
step9: print the elements
step10: End
"""

number = int(input("Enter the number: "))
a=[] #0

while number>0:
    remainder = number%2
    a.append(remainder)
    number=number//2

for i in a:
    print(i,end=" ")