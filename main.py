import definitions as defs

main_var = "Hello from main.py!"

if __name__ == "__main__":
    if hasattr(defs, "functionTwo"):
        defs.functionTwo(main_var)
    else:
        print("Execution module %s" % __file__)
