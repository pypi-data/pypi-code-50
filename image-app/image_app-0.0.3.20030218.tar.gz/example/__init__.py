from image_app import load_smooth_area

if __name__ == '__main__':
    import os
    import cv2

    path = os.path.abspath("../example/11123.png")
    print(path)

    image = cv2.imread(path)
    rects = load_smooth_area(image)
    for rect in rects:
        cv2.rectangle(image, (rect[0], rect[1]), (rect[2], rect[3]), (120, 78, 255), 2)
    cv2.imwrite('test.jpg', image)
    cv2.imshow("test", image)
    cv2.waitKey(3000)
