#calculator
fn = float(input("First number : "))
sn = float(input("Second number : "))
op = input("Choose operation (+, -, *, /) : ")

if op == "+":
   result = (fn + sn)
   print(f"Result: {fn} + {sn} = {result}")
elif op == "-":
   result = (fn - sn)
   print(f"Result: {fn} - {sn} = {result}")
elif op == "*":
   result = (fn * sn)
   print(f"Result: {fn} * {sn} = {result}")
else:
   result = (fn / sn)
   print(f"Result: {fn} / {sn} = {result}")