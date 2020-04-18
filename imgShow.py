import cv2

def main():
    print('横のサイズどうする？')
    width = int(input())
    
    src = cv2.imread('/Users/ononayuta/Pictures/simulator.png')
    if (src is None):
        return

    scale = width/src.shape[1]
    resizeImg = cv2.resize(src,dsize = None, fx = scale, fy = scale)
    cv2.namedWindow('resize', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('resize', resizeImg)
    cv2.waitKey(0)

    for i in range(0, resizeImg.shape[0] % width):
        cv2.rectangle(resizeImg, (0, width * i), (width, width * (i+1)), (0, 0, 255), 5)
    cv2.imshow('resize', resizeImg)
    cv2.waitKey(0)

    cv2.destroyWindow('resize')
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()