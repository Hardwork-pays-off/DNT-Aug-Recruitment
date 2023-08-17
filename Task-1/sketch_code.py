import cv2

def sketch_image(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1=30, threshold2=70)

    # Invert the binary image to get white lines on black background
    inverted_edges = cv2.bitwise_not(edges)

    # Save the sketched image
    cv2.imwrite(output_path, inverted_edges)

if __name__ == "__main__":
    input_image_path = r"C:\Users\devir\Downloads\thug duck.jpeg"  
    output_image_path = r"C:\Users\devir\Desktop\VIT\Sem 3\Extras Sem 3\sketch.jpeg"  

    sketch_image(input_image_path, output_image_path)
