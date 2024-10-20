def main():
    my_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5
    }

    key = input("Enter the key you want to find: ").strip()

    if key in my_dict:
        print(f"The value for '{key}' is: {my_dict[key]}")
    else:
        print(f"Key '{key}' not found in the dictionary.")

if __name__ == "__main__":
    main()
