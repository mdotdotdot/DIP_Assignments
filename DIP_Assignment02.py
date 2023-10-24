import cv2
import numpy as np

original_image = cv2.imread("img.png", 0)

_, label_image = cv2.threshold(original_image, 127, 255, cv2.THRESH_BINARY)


height, width = label_image.shape


matrix = np.zeros((height, width), dtype=int)


matrix = np.pad(matrix, 1, mode='constant',
                constant_values=0)[:, :-1]


for i in range(1, height):
    for j in range(1, width-1):
        neighbor_array = []
        matrix[i, j - 1] != 0 and neighbor_array.append(matrix[i, j - 1])
        matrix[i - 1, j] != 0 and neighbor_array.append(matrix[i - 1, j])
        matrix[i - 1, j -
               1] != 0 and neighbor_array.append(matrix[i - 1, j - 1])
        matrix[i - 1, j +
               1] != 0 and neighbor_array.append(matrix[i - 1, j + 1])
        matrix[i, j] = label_image[i-1, j-1] != 0 and (
            (not neighbor_array and np.max(matrix) + 1) or min(neighbor_array))
print(np.max(matrix))

for i in range(1, height):
    for j in range(1, width):
        if matrix[i, j] != 0:
            neighbor_array = []
            matrix[i, j - 1] != 0 and neighbor_array.append(matrix[i, j - 1])
            matrix[i - 1, j] != 0 and neighbor_array.append(matrix[i - 1, j])
            matrix[i - 1, j -
                   1] != 0 and neighbor_array.append(matrix[i - 1, j - 1])
            matrix[i - 1, j +
                   1] != 0 and neighbor_array.append(matrix[i - 1, j + 1])
            if neighbor_array:
                matrix[i, j] = min(neighbor_array)
                for neighbor in neighbor_array:
                    if neighbor != min(neighbor_array):
                        matrix[matrix == neighbor] = min(neighbor_array)

color_image = cv2.cvtColor(
    np.uint8(matrix*255/np.max(matrix)), cv2.COLOR_GRAY2BGR)

colors = np.random.randint(0, 255, size=(np.max(matrix), 3))


for i in range(1, np.max(matrix)):
    color_image[matrix == i] = colors[i]


cv2.imshow("8 pixel connectivity", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()