# Screen OCR Analyzer Project

The aim of the project was to make a program that captures and analyzes the content displayed on the user's screen. Created during my third year of Bachelor of Engineering studies at Metropolia UAS, program utilizes (OCR) Optical Character Recognition to extract text from the computer screen and performs sentiment analysis on the recognized text. The Result is given in form of User encountered : 1 positive information, 0 neutral information, -1 negative information.

### USAGE:
Tesseract OCR [Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki) installation instructions.

Clone Repository:
```
git clone https://github.com/damakes/REC-OCR-Sentiment-Analysis.git
```
Dependencies 👉 `requirements.txt`:
```
pip install -r requirements.txt
```
Run program: 
```
python REC_OCR.py
```
### To stop program **'q'** key press **[on top Window where Recognized Text is shown].**
PROGRAM IN ACTION:

<img src="https://github.com/damakes/REC-OCR-Sentiment-Analysis/assets/155246347/7bc78881-94e3-414b-a599-cae52e340b96" width="280" height="280">
<img src="https://github.com/damakes/REC-OCR-Sentiment-Analysis/assets/155246347/24e2bcde-b518-4e5b-b3e3-b494dfe4b409" width="280" height="280">


RESULT : `User encountered {'positive': 0.05687029496559418} information.`
