import cv2
import string
import os

# Dictionary to map characters to their ASCII values and vice versa
char_to_int = {chr(i): i for i in range(256)}
int_to_char = {i: chr(i) for i in range(256)}

# Read the input image
image = cv2.imread("jk.jpg")

# Check if the image is loaded successfully
if image is not None:
    height, width, _ = image.shape
    print("Image dimensions:", height, "x", width)
else:
    print("Error: Unable to load the image")

# Function to hide text in the image
def hide_text_in_image(image, text, key):
    encrypted_image = image.copy()
    key_index = 0

    for char in text:
        encrypted_image[0, key_index, 0] = char_to_int[char] ^ char_to_int[key[key_index % len(key)]]
        key_index += 1

    return encrypted_image

# Function to extract text from the encrypted image
def extract_text_from_image(encrypted_image, key):
    decrypted_text = ""
    key_index = 0

    for i in range(len(text)):
        decrypted_text += int_to_char[encrypted_image[0, key_index, 0] ^ char_to_int[key[key_index % len(key)]]]
        key_index += 1

    return decrypted_text

# Main function
if __name__ == "__main__":
    key = input("Enter key to edit (Security Key): ")
    text = input("Enter text to hide: ")

    # Hide text in the image
    encrypted_image = hide_text_in_image(image, text, key)
    cv2.imwrite("encrypted_img.jpg", encrypted_image)
    print("Data hiding in image completed successfully.")
    os.startfile("encrypted_img.jpg")

    # Extract text from the encrypted image
    choice = int(input("\nEnter 1 to extract data from the image: "))
    if choice == 1:
        key_input = input("\nRe-enter key to extract text: ")
        if key == key_input:
            decrypted_text = extract_text_from_image(encrypted_image, key)
            print("Encrypted text was:", decrypted_text)
        else:
            print("Key doesn't match.")
    else:
        print("Thank you. EXITING.")
