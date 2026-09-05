from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")
result = ocr.predict("text.png")

for page in result:
    print(page)
