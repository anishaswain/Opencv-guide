import cv2
import matplotlib.pyplot as plt

def main():
    imgpath ='/home/nisnt2411/Downloads/Messi.jpg'  #works fine in unix platforms
    #  path = "\\IMAGEPATH\\IMAGE.jpg"  "works with windows machine"
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
   # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Laplacian(img, -1, ksize=29, scale=1, delta=0, 
                          borderType=cv2.BORDER_DEFAULT)

    output = [img, edges]
    titles = ['Original', 'Edges']
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()