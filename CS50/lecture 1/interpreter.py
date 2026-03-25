expression = input("Enter ur maths expression: ").strip()

x,y,z = expression.split(" ")

x = float(x)
z = float(z)

match y:

    case "+":
        print(f" {x + z:.1f}")

    case "*":
        print(f" {x * z:.1f}")

    case "/":
        print(f" {x / z:.1f}")

    case _:
        print(f" {x - z:.1f}")

