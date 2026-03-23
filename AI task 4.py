print("Movie Recommendation System")

genre = input("Enter your favorite genre (action/comedy/romance): ").lower()

if genre == "action":
    print("Recommended Movies:")
    print("1. Avengers")
    print("2. Mission Impossible")
    print("3. John Wick")

elif genre == "comedy":
    print("Recommended Movies:")
    print("1. Varuthapadatha Valibar Sangam")
    print("2. Kalakalappu ")
    print("3. Panchathanthiram")

elif genre == "romance":
    print("Recommended Movies:")
    print("1. Titanic")
    print("2. The Notebook")
    print("3. La La Land")

else:
    print("Sorry, no recommendations available for this genre.")