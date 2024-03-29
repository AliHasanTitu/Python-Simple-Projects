import cv2

# Image file location
main_image_location = "C:/Users/AliPC/Desktop/Image/"
filename = "20230121_065857.jpg"


# Read the image
img = cv2.imread(main_image_location + filename)

# Convert the image to gray mode
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
invert_gray_image = 255 - gray_img

# Blur the image by gaussian function
blured_img = cv2.GaussianBlur(invert_gray_image, (21,21), 0)

# Inverted the blured image
invert_blured_image = 255 - blured_img

# Pencil sketch
pencil_sketch_IMG = cv2.divide(gray_img, invert_blured_image, scale = 256.0)

# Show the image
cv2.imshow("Main Image", img)
cv2.imshow('New Image that are gray color', gray_img)
cv2.imshow('invert image', invert_gray_image)
cv2.imshow('GaussianBlur img', blured_img)
cv2.imshow('Inverted Blured img', invert_blured_image)
cv2.imshow('Pencil Sketch', pencil_sketch_IMG)
cv2.waitKey(0)


directory = "C:/Users/AliPC/Desktop/image/new/"
filename_2 = "savedimgae_2.png"
cv2.imwrite(filename_2, pencil_sketch_IMG)
print('Successfully save')
