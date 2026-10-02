import pandas as pd
import os

os.makedirs('data', exist_ok=True)

# Generate projects.csv
projects = [
    ["E-Commerce Web App", "Web Development", "HTML, CSS, JavaScript, React, Node.js", 6, 120, "VS Code, Git, React, Node", "3,4", "CSE,IT", "Build a full stack ecommerce platform."],
    ["IoT Smart Home", "IoT", "C++, Arduino, Python, MQTT", 7, 80, "Arduino IDE, ESP32, MQTT Broker", "2,3,4", "ECE,EEE,CSE", "Automate home appliances using IoT."],
    ["Machine Learning Stock Predictor", "AI/ML", "Python, Pandas, Scikit-Learn, XGBoost", 8, 100, "Jupyter, Python", "3,4", "CSE,IT", "Predict stock prices using historical data."],
    ["Bridge Structural Analysis", "Civil", "AutoCAD, SAP2000, Python", 8, 150, "AutoCAD, SAP2000", "3,4", "Civil", "Analyze bridge stress and load distributions."],
    ["Drone Flight Controller", "Robotics", "C, C++, PID Control", 9, 200, "STM32, C++", "3,4", "ECE,Mech", "Custom flight controller for quadcopters."],
    ["Personal Portfolio Website", "Web Development", "HTML, CSS, JavaScript", 3, 30, "VS Code, GitHub Pages", "1,2,3,4", "CSE,IT,ECE", "A simple static portfolio to showcase projects."],
    ["Weather Forecasting App", "Mobile App", "Flutter, Dart, REST API", 5, 60, "Flutter, Android Studio", "2,3,4", "CSE,IT", "Mobile app to check weather using external APIs."],
    ["Automated Plant Watering System", "IoT", "Arduino, Sensors, C++", 4, 40, "Arduino, Moisture Sensors", "1,2,3", "ECE,EEE,Mech", "Water plants automatically based on soil moisture."],
    ["Blockchain Voting System", "Blockchain", "Solidity, React, Node.js", 9, 160, "Remix, Truffle, React", "3,4", "CSE,IT", "Secure and anonymous voting using smart contracts."],
    ["Customer Churn Prediction", "Data Science", "Python, Pandas, Scikit-Learn", 6, 80, "Jupyter, Scikit-Learn", "3,4", "CSE,IT", "Predict whether a customer will leave a service."],
    ["Voice Controlled Assistant", "AI/ML", "Python, SpeechRecognition, NLP", 7, 90, "Python, APIs", "2,3,4", "CSE,IT,ECE", "A simple Alexa-like virtual assistant."],
    ["Solar Power Monitor", "Power Systems", "Python, Arduino, Voltage Sensors", 5, 70, "Arduino, ESP32", "2,3,4", "EEE,ECE", "Monitor solar panel output and efficiency in real-time."],
    ["HVAC Energy Optimization", "Mechanical", "Thermodynamics, Python", 7, 110, "Python, Excel", "3,4", "Mech", "Optimize energy usage for heating and cooling systems."],
    ["Traffic Sign Recognition", "Computer Vision", "Python, OpenCV, TensorFlow", 8, 130, "Jupyter, TensorFlow", "3,4", "CSE,IT,ECE", "Detect and classify traffic signs from images."],
    ["Library Management System", "Software Dev", "Java, MySQL", 4, 50, "Eclipse, MySQL", "2,3", "CSE,IT", "Desktop application to manage library books."],
    ["Smart Street Lighting", "IoT", "C++, Microcontrollers, LDR", 4, 40, "Arduino, Sensors", "1,2,3", "ECE,EEE", "Street lights that turn on/off based on ambient light."],
    ["3D Printed Robotic Arm", "Robotics", "CAD, C++, Arduino", 8, 150, "SolidWorks, Arduino", "3,4", "Mech,ECE", "Design, print, and program a robotic arm."],
    ["Cybersecurity Password Manager", "Security", "Python, Cryptography", 6, 70, "Python, SQLite", "2,3,4", "CSE,IT", "Securely store and generate passwords locally."],
    ["Sentiment Analysis of Reviews", "NLP", "Python, NLTK, Scikit-Learn", 5, 60, "Jupyter, NLTK", "3,4", "CSE,IT", "Classify product reviews as positive or negative."],
    ["Electric Vehicle Battery Management", "Power Systems", "MATLAB, Simulink, C++", 9, 180, "MATLAB", "3,4", "EEE,ECE,Mech", "Manage EV battery charging and health."],
    ["Real-time Chat Application", "Web Development", "React, Node.js, Socket.io", 7, 90, "VS Code, Node.js", "3,4", "CSE,IT", "A real-time messaging app like WhatsApp Web."],
    ["Fraud Detection in Credit Cards", "Data Science", "Python, Pandas, Machine Learning", 7, 100, "Jupyter, Python", "3,4", "CSE,IT", "Detect fraudulent transactions using anomaly detection."],
    ["Smart Irrigation System", "Agriculture Tech", "IoT, Arduino, Sensors", 5, 50, "Arduino, ESP8266", "2,3,4", "ECE,EEE,Civil", "Optimize water usage for agriculture."],
    ["Seismic Analysis of Buildings", "Civil", "ETABS, SAP2000", 8, 140, "ETABS", "3,4", "Civil", "Analyze building stability under earthquake loads."],
    ["Wind Turbine Aerodynamics", "Mechanical", "ANSYS, CFD", 9, 160, "ANSYS", "3,4", "Mech", "Simulate and optimize wind turbine blades."],
    ["Expense Tracker App", "Mobile App", "React Native, Firebase", 5, 60, "React Native, Firebase", "2,3,4", "CSE,IT", "Track personal expenses and income."],
    ["Spam Email Classifier", "Machine Learning", "Python, Scikit-Learn, NLP", 5, 50, "Jupyter, Python", "2,3,4", "CSE,IT", "Filter out spam emails from legitimate ones."],
    ["Home Automation Dashboard", "Web Development", "Vue.js, Firebase", 6, 70, "Vue.js, Firebase", "3,4", "CSE,IT,ECE", "Web interface to control smart home devices."],
    ["Gesture Controlled Car", "Robotics", "Arduino, Accelerometer, RF", 6, 80, "Arduino, RF Modules", "2,3,4", "ECE,Mech,EEE", "Control a toy car using hand gestures."],
    ["Resume Parsing API", "AI/ML", "Python, FastAPI, NLP", 7, 90, "FastAPI, Spacy", "3,4", "CSE,IT", "Extract skills and details from PDF resumes."]
]

df_projects = pd.DataFrame(projects, columns=["title", "domain", "required_skills", "difficulty_1_to_10", "estimated_hours", "tools", "suitable_year", "suitable_departments", "description"])
df_projects.to_csv('data/projects.csv', index=False)

skills = [
    ["Python", "Programming", "None", "Python programming for beginners"],
    ["HTML", "Web Development", "None", "HTML tutorial for beginners"],
    ["CSS", "Web Development", "HTML", "CSS tutorial for beginners"],
    ["JavaScript", "Web Development", "HTML, CSS", "JavaScript full course"],
    ["React", "Web Development", "JavaScript", "React JS crash course"],
    ["Node.js", "Web Development", "JavaScript", "Node.js for beginners"],
    ["C++", "Programming", "None", "C++ programming tutorial"],
    ["Arduino", "IoT", "C++", "Arduino basics for beginners"],
    ["Pandas", "Data Science", "Python", "Pandas data analysis tutorial"],
    ["Scikit-Learn", "Machine Learning", "Python", "Scikit-Learn machine learning tutorial"],
    ["AutoCAD", "Civil/Mech", "None", "AutoCAD for beginners"],
    ["Flutter", "Mobile App", "None", "Flutter app development crash course"],
    ["Dart", "Programming", "None", "Dart programming for beginners"],
    ["Solidity", "Blockchain", "JavaScript", "Solidity smart contract tutorial"],
    ["TensorFlow", "Deep Learning", "Python, Machine Learning", "TensorFlow crash course"],
    ["Java", "Programming", "None", "Java programming full course"],
    ["MySQL", "Databases", "None", "SQL database tutorial for beginners"],
    ["Socket.io", "Web Development", "Node.js", "Socket.io real-time chat tutorial"],
    ["Firebase", "Backend", "None", "Firebase setup and database tutorial"],
    ["FastAPI", "Backend", "Python", "FastAPI tutorial in Python"],
    ["MQTT", "IoT", "Networking", "MQTT protocol for IoT explained"],
    ["React Native", "Mobile App", "React", "React Native crash course"]
]

df_skills = pd.DataFrame(skills, columns=["skill", "domain", "prerequisite_skill", "youtube_search_query"])
df_skills.to_csv('data/skills.csv', index=False)

print("Data generated successfully.")
