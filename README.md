# Screen Text Recognition
This Python script captures the screen within a defined bounding box, recognizes text using Optical Character Recognition (OCR), and analyzes the sentiment of the recognized text.

## Prerequisites
Before running the script, make sure you have the following libraries installed:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Pillow (`PIL`)
- pytesseract (`pytesseract`)
- TextBlob (`textblob`)

You can install the required libraries using `pip`:
```
pip install opencv-python numpy pillow pytesseract textblob
```
You also need to install Tesseract OCR. Please refer to the [Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki) for installation instructions. Set the path to the Tesseract executable (`tesseract_cmd`) in the script: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


## Functions
- capture_screen(): Capture the screen within the defined bounding box.
- convert_to_grayscale(screen): Convert the given screen to grayscale.
- recognize_text(screen): Use OCR to recognize text from the given screen.
- write_text_to_file(text, file_path): Write the given text to the specified file.
- draw_rectangles(screen, boxes): Draw rectangles around recognized words on the given screen.
- analyze_sentiment(file_path): Read the text from the specified file and return its polarity.
  
## Sentiment Analysis
The script includes a function to analyze the sentiment of text stored in a file. It reads the text from the file and returns its polarity, which can be 'positive', 'negative', or 'neutral'.

