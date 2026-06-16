# try:
#     print("Importing FileConcept")
#     with open("FileConcept.py", "r") as f:
#         code = f.read()
#     exec(code)
# except Exception as e:    
#     print(f"Error importing FileConcept: {e}")
try:
    print("Importing FileConcept")
    with open("intro.txt", "r") as f:
        code = f.read()
        print("Code read from intro.txt:")
        print(code)
        code=code.upper()  # Example of processing the code
        print("Code after processing:")
        print(code)
except Exception as e:    
    print(f"Error importing FileConcept: {e}")