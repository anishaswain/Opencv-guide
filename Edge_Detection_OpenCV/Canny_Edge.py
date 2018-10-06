import cv2
import matplotlib.pyplot as plt
def main():
    #  path = "\\IMAGEPATH\\IMAGE.jpg"  "works with windows machine"
    img = cv2.imread('/home/nisnt2411/Downloads/Messi.jpg', cv2.IMREAD_GRAYSCALE)
    #works fine in unix platforms
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Else we could also use this for converting image from colored top grayscale

    
    L1 = cv2.Canny(img, 50, 300, L2gradient=False)
    # here 50 and 300 are threshold values. 
    L2 = cv2.Canny(img, 100, 150, L2gradient=True)

    
    titles = ['Original Image', 'L1 Norm', 'L2 Norm']

    outputs = [img, L1, L2]
    
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(outputs[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()