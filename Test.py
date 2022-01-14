#la Methode utilisée est "least squares circle fitting"
import cv2
import numpy as np
import os
import circle_fit as cf
data=[] #data utilisé pour le tracage en fesant changemant de repere pour avoir un cercle dans le mileiu de l'ecran
data1=[] #data original sans changement de repère pour determiner le centre et le rayon
w=1000  #dimension de l'image surlaquelle on va tracer le cercle
h=1000
# Créer une image noir vide
while True :
    image=np.zeros((h,w,3),np.uint8)  #image noir
    image = cv2.circle(image, (w//2,h//2), radius=0, color=(0, 0, 255), thickness=1)  #centre de plan crée
    for i in range( 0,h):  #tracage de deux axes
        image[500,i]= (255, 255, 255)
    for i in range( 0,w):
        image[i,int(h/2)]= (255, 255, 255)
    with open(os.getcwd()+"/circle_points2D.txt") as f:  #lire le fichier texte
        lines = f.readlines()


    for i in  lines :
        x_pt=h/2+float(i.split(",")[0])*10 # Agrandir l'échelle et changer les coordonnées selon le plan crée
        y_pt=w/2-float(i.split(",")[1])*10
        data.append((x_pt,y_pt))
        x_pt1 = float(i.split(",")[0])  #on determine les coordonnées de chaque point
        y_pt1 = float(i.split(",")[1])
        data1.append((x_pt1, y_pt1)) #on met ces coordonnées dans data

        cv2.circle(image, (int(x_pt),int(y_pt)), radius=1, color=(255, 0, 0), thickness=2) #tracage de points
    #print(data)
    xc, yc, r, _ = cf.least_squares_circle((data)) # la methode utiliser pour determiner le rayon et le centre dans le plan crée
    xc1, yc1, r1, _ = cf.least_squares_circle((data1)) # la methode utiliser pour determiner le rayon et le centre dans le plan original
    print("x=  ",xc1) #retourner l'abscisse de centre
    print("y=  ",yc1) #retourner l'ordonné de centre
    print("r=  ",r1) #retourner le rayon
    cv2.circle(image, (int(xc), int(yc)), radius=int(r), color=(0, 255, 255), thickness=1) #tracage de centre
    cv2.circle(image, (int(xc), int(yc)), radius=1, color=(0, 255, 255), thickness=1)
    cv2.imshow("Cercle",image) #affichage le resultat
    while True :
        if cv2.waitKey() & 0xff == ord('q'):
            break
    cv2.destroyAllWindows()



