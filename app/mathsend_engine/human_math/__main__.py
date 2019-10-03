from HumanMath.engine import compute

def main():
    calculate = "Y"
    while calculate == "Y":
        in_expr = input("Input Expression =  ")
        solution = compute(in_expr)
        print("solution = ", solution)
        calculate = input("Solve another expression ? 'Y'|'N' = ")
    print("Mathsend Aborted")
if __name__ == '__main__':
    main()