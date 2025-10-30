def mini_library():
    try:
    
        title = input("Enter book title")

        
        if not all(char.isalpha() or char.isspace() for char in title) or title.strip() == "":
            raise ValueError("Error: Book title must contain only letters and spaces.")

        
        year = input("Enter publication year: ")

        
        if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
            raise ValueError("Error: Year must be a 4-digit number starting with '19' or '20'.")

    
        print("\nBook added successfully!")
        print(f"Title: {title}")
        print(f"Publication Year: {year}")

    except ValueError as e:
        print(e)

    finally:
        print("\nProcess completed.")



mini_library()
