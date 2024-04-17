import cv2
import numpy as np
from PIL import ImageGrab
import time
import pytesseract
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Path to the Tesseract.exe

def capture_screen(): #Returns: The captured screen screen as a NumPy array.
    return np.array(ImageGrab.grab(bbox=(0, 40, 1200, 800)))

def convert_to_grayscale(screen): # Returns: The grayscale version of the input screen.
    return cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

def recognize_text(screen): # Returns: The recognized text.
    return pytesseract.image_to_string(screen)

def write_text_to_file(text, file_path): # Write the given text to the specified file.
    with open(file_path, "a") as output_file: output_file.write(text + "\n")

def draw_rectangles(screen, boxes): # Returns: np.array: The screen with rectangles drawn around recognized words.
    h, w, _ = screen.shape # Get the height and width of the screen image
    for b in boxes.splitlines(): # Iterate over each line of bounding box information
        b = b.split() # Split the line into individual values
        x, y, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4]) # Extract and convert bounding box coordinates from the Tesseract OCR result
        cv2.rectangle(screen, (x, h - y), (x2, h - y2), (0, 255, 0), 2) # Draw rectangle around the word
        cv2.putText(screen, b[0], (x, h - y), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2) # Add text label to the rectangle
    return screen 

def analyze_sentiment(file_path):
    
    with open(file_path, 'r') as file: text = file.read() # Read the text from the file

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine the polarity
    if polarity > 0: return {'positive' : polarity}
    elif polarity < 0: return {'negative' : polarity}
    else: return {'neutral' : polarity}



def main(): # Main function to capture screen, recognize text, and display results.
 
    last_time = time.time()
    file_path = "recognized_text.txt"
    while True:
        screen = capture_screen() # Capture the scree
        screen_gray = convert_to_grayscale(screen) # Convert screen from RGB to GRAY
        text = recognize_text(screen_gray) # Use OCR to recognize text
        write_text_to_file(text, file_path) # Write the recognized text to the file
        screen_with_rectangles = draw_rectangles(screen, pytesseract.image_to_boxes(screen_gray)) # Draw rectangles around the recognized words
        print('Recognized Text:', text) # show recognized text in terminal
        print('Loop took {} seconds'.format(time.time() - last_time)) # Show loop time in terminal
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen_with_rectangles, cv2.COLOR_BGR2RGB)) # Display the window
        if cv2.waitKey(25) & 0xFF == ord('q'): # Break the loop on 'q' key press
            cv2.destroyAllWindows()
            polarity = analyze_sentiment(file_path)
            print(f'User encountered {polarity} information.')
            break

if __name__ == "__main__":
    main()
