def TestFunction(x):
    """
    A Test function
    """
    
    if x > 0:
        print("Greater than 0")
    elif x == 0:
        print("Equals 0")
    else:
        print("Less than 0")
    
    return x > 0

if __name__ == "__main__":
  print(TestFunction(5))
