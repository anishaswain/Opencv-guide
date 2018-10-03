import cv2
import matplotlib.pyplot as plt

def main():
    imgpath ='/home/nisnt2411/Downloads/Messi.jpg'  #works fine in unix platforms
    #  path = "\\IMAGEPATH\\IMAGE.jpg"  "works with windows machine"
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
   # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edgesx = cv2.Sobel(img, -1, dx=3, dy=0, ksize=11, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
    edgesy = cv2.Sobel(img, -1, dx=0, dy=3, ksize=11, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
      #above we are multiplying image with the sobel operator to get the edges
    edges = edgesx + edgesy

    output = [img, edgesx, edgesy, edges]
    titles = ['Original', 'dx=1 dy=0', 'dx=0 dy=1', 'Edges']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()