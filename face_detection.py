# importing librarys
import cv2
import numpy as npy
import face_recognition as face_rec
# function
def resize(img, size) :
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)


# img declaration
jahangir = face_rec.load_image_file('sampe_images\jahangir.jpg')
jahangir = cv2.cvtColor(jahangir, cv2.COLOR_BGR2RGB)
jahangir = resize(jahangir, 0.50)
jahangir_test = face_rec.load_image_file('sampe_images\jahangir_test4.jpg')
jahangir_test = resize(jahangir_test, 0.50)
jahangir_test = cv2.cvtColor(jahangir_test, cv2.COLOR_BGR2RGB)

# finding face location

faceLocation_jahangir = face_rec.face_locations(jahangir)[0]
encode_jahangir = face_rec.face_encodings(jahangir)[0]
cv2.rectangle(jahangir, (faceLocation_jahangir[3], faceLocation_jahangir[0]), (faceLocation_jahangir[1], faceLocation_jahangir[2]), (255, 0, 255), 3)


faceLocation_jahangirtest = face_rec.face_locations(jahangir_test)[0]
encode_jahangirtest = face_rec.face_encodings(jahangir_test)[0]
cv2.rectangle(jahangir_test, (faceLocation_jahangir[3], faceLocation_jahangir[0]), (faceLocation_jahangir[1], faceLocation_jahangir[2]), (255, 0, 255), 3)

results = face_rec.compare_faces([encode_jahangir], encode_jahangirtest)######
print(results)
cv2.putText(jahangir_test, f'{results}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 2 )

cv2.imshow('main_img', jahangir)
cv2.imshow('test_img', jahangir_test)
cv2.waitKey(0)
cv2.destroyAllWindows()