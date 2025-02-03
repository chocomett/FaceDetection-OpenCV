import cv2

face_ref = cv2.CascadeClassifier("ref.xml")
camera = cv2.VideoCapture(0)

def face_detection(frame): # (frame) => collect camera  
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=1.1)
    return faces
    

def drawer_box(frame):
    for x, y, w, h in face_detection(frame):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)


def close_windows():
    camera.release
    cv2.destroyAllWindows
    print("Program selesai")
    exit()
    
    
def main():
    while True:
        _, frame = camera.read() #permission to accsess camera 
        drawer_box(frame)
        cv2.imshow("Chocomett CAM", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_windows()
        

if __name__ == "__main__":
    print("Program di jalankan ...")
    main()