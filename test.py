import cv2
from paddleocr import PaddleOCR
import numpy as np

# PaddleOCRのインスタンスを作成
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# 画像を読み込む
image_path = './test.jpg'
image = cv2.imread(image_path)

# OCRを使って画像全体からテキストを抽出
results = ocr.ocr(image, cls=True)

# 抽出されたテキストから数字を抽出
numbers = []
for line in results[0]:
    text = line[1][0]
    # 数字のみを抽出
    for char in text:
        if char.isdigit() or char in ['.', ',']:  # 小数点やカンマも含める場合
            numbers.append(char)

#抽出された数字をテキストに保存
extracted_numbers = ''.join(numbers)

print(f"Extracted Numbers: {extracted_numbers}")

# 画像とOCR結果を表示および保存（数字を強調表示）
for line in results[0]:
    box = line[0]
    text = line[1][0]
    # 数字の部分だけを強調表示
    if any(char.isdigit() for char in text):
        cv2.polylines(image, [np.array(box).astype(int)], isClosed=True, color=(0, 255, 0), thickness=2)

# OCR結果を保存
output_image_file = 'ocr_results.jpg'
cv2.imwrite(output_image_file, image)
