import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os
import pyttsx3


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



# Load known faces and their names with subject information

user_input = input("Please enter a Class Name: ")
students_data = [
    {"subject": user_input, "students": [
<<<<<<< Updated upstream
        {"id": 232501, "name": "Harry", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\harry.jpg"},
        {"id": 232502, "name": "Ahsan","image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\Ahsan.jpg"},
        {"id": 232503, "name": "Professor", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\professor.jpg"},
        # {"id": 232504, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232505, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232506, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232507, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232508, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232509, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232510, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232511, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232512, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232513, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232514, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232515, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232516, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232517, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232518, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232519, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232520, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232521, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232522, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232523, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232524, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232525, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232526, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232527, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232528, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232529, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232530, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232531, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232532, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232533, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232534, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232535, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232536, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232537, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232538, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232539, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232540, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232541, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232542, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232543, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232544, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232545, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232546, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232547, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232548, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232549, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232550, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232551, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232552, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232553, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232554, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232555, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232556, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232557, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232558, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232559, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232560, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jpg"},
        # {"id": 232561, "name": " ", "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\.jep"}

=======
        {"id": 232501, "name": "Harry",  "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\harry.jpg"},
        {"id": 232552, "name": "Ahsan",  "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\Ahsan.jpg"},
        {"id": 232552, "name": "Professor",  "image_path": "D:\\CodeBackground\\pythonProject\\Attendance\\faces\\professor.jpg"},
    #    add more sstudents data for as need
>>>>>>> Stashed changes
    ]}
]

known_face_encodings = []
known_face_names = []
subject_mapping = {}
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_month = now.strftime("%B")
dates = [current_date]

# Create a directory to store CSV files if it doesn't exist
output_directory = os.path.join("D:\\CodeBackground\\pythonProject\\Attendance\\Attendance_CSV", current_month)
os.makedirs(output_directory, exist_ok=True)

for subject_data in students_data:
    subject_name = subject_data["subject"]

    # Open CSV file in write mode or create a new one if it doesn't exist
    csv_file_path = os.path.join(output_directory, f"Attendance_{subject_name}_{current_month}.csv")
    with open(csv_file_path, "a", newline="\n") as f:
        lnwrite = csv.writer(f)

        lnwrite.writerow(["ID", "Name"] + dates)


        for student in subject_data["students"]:
            student_image = face_recognition.load_image_file(student["image_path"])
            student_encoding = face_recognition.face_encodings(student_image)[0]
            known_face_encodings.append(student_encoding)
            known_face_names.append(student["name"])
            subject_mapping[student["name"]] = {"id": student["id"], "subject": subject_name}

    video_capture = cv2.VideoCapture(0)
    students_attendance = {}

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                student_info = subject_mapping.get(known_face_names[best_match_index], {})
                student_id = student_info.get("id", "Unknown")
                name = known_face_names[best_match_index]
                students_attendance[student_id] = {"name": name, "status": "Present"}

                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner_of_text = (10, 100)
                font_scale = 1
                font_color = (66, 0, 255)
                thickness = 2
                line_type = 2
                cv2.putText(frame, f"{name} ({student_id}, {subject_name}) Present", bottom_left_corner_of_text, font,
                            font_scale, font_color, thickness, line_type)
                speak(f"{name} present in {subject_name}")

        cv2.imshow("Attendance", frame)

        # Break out of the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release video capture before writing attendance data to the CSV file
    video_capture.release()

    # Write attendance data to the CSV file sorted by student ID
    with open(csv_file_path, "a", newline="\n") as f:
        lnwrite = csv.writer(f)

        for student_id, info in sorted(students_attendance.items(), key=lambda x: int(x[0])):
            row_data = [student_id, info["name"], "Present"]
            lnwrite.writerow(row_data)

    print(f"Attendance saved to {csv_file_path}")

# Close all windows
cv2.destroyAllWindows()