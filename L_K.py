import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/sofianeagounikaci/Downloads/traffic.mp4')

# params for ShiTomasi corner detection
feature_params = dict(maxCorners = 300, 
                     qualityLevel = 0.15, 
                     minDistance = 5, 
                     blockSize = 3)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize = (15,15),
                maxLevel = 2,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it
ret, old_frame = cap.read()

if not ret:
    print("Erreur: Impossible de lire la vidéo")
    cap.release()
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(True):
    ret, frame = cap.read()
    
    # Vérifier si la frame a été lue correctement
    if not ret:
        print("Fin de la vidéo ou erreur de lecture")
        break
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    
    # Vérifier si le flux optique a réussi
    if p1 is not None:
        # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]
        
        # draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            # Convertir en entiers
            a, b = int(new[0]), int(new[1])
            c, d = int(old[0]), int(old[1])
            
            # Dessiner la ligne de trajectoire
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            # Dessiner le point actuel
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
        
        img = cv2.add(frame, mask)
        cv2.imshow('Optical Flow', img)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # ESC pour quitter
            break
        
        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)
    else:
        print("Flux optique perdu, recherche de nouveaux points...")
        # Réinitialiser les points si le flux optique échoue
        p0 = cv2.goodFeaturesToTrack(frame_gray, mask = None, **feature_params)
        mask = np.zeros_like(frame)
        old_gray = frame_gray.copy()

cv2.destroyAllWindows()
cap.release()