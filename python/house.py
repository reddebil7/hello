name = input("What's your name? ")


match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Droco":
        print("Slytherin")
    case _:
        print("Who?")
#if name == "Harry":
  #  print("Gryffindor")
#elif name == "Hermoine":
 #   print("Slytherin")
#else:
 #   print("who??? ")