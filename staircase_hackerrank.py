n=4
def staircase(n):
    # Write your code here
    i=0
    while i<=n-1:
        column=((n-i-1)*" ")+"#"    
        print(column,end="")
        row=i*"#"
        print(row)
        i +=1
staircase(n)