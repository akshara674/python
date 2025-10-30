def feedback_system():
    try:
        
        name = input("Enter your name: ").strip()
        feedback = input("Enter your feedback: ").strip()

    
        if not name:
            raise ValueError("Error: Name cannot be empty.")
        if not feedback:
            raise ValueError("Error: Feedback cannot be empty.")

        
        print("\nThank you for your feedback!")
        print(f"Name: {name}")
        print(f"Feedback: {feedback}")

    except ValueError as e:
        print(e)

    finally:
        print("\nFeedback process completed.")



feedback_system()
