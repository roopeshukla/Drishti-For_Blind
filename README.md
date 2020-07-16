# Drishti-For_Blind
Visual impairment can pose a challenge to accomplish everyday activities such as driving, reading, and walking. 
People with visual impairment experience their surroundings uniquely when compared to a sighted person.
They have more active senses (touch, smell, sound, and taste) to learn about their surrounding but activity as easy as reading a book or detecting objects
in front without touching seems impossible for them. Drishti (meaning "vision" in the Hindi language) is designed to describe this beautiful world to the visually impaired.
Drishti helps to read the text in front of the user, and it also conveys the environment around the visually impaired, by describing the objects and relationship b/w the objects.
Examples are a 'person sitting on a bench,' 'a dog is sleeping,' 'a stop sign on the road'. On users command the image is captured with a camera connected to the raspberry pi.
If the user wants text description of the image, the image is analysed by Google's Cloud Vision API using Optical Character Recognition to detect the characters,
letters in the picture, and if the user wants the scene description of the nearby environment, the image is sent to the Microsoft Cognitive Services to analyse the image
using Computer Vision. Generated result is stored in the Dynamo DB (Cloud database). When the user asks Alexa to 'Read the text' or 'Explain the environment', 
the Alexa Skill Kit triggers AWS Lambda Function to fetch the results from the database (Dynamo Db). The Alexa app then recites the stored result on the user's mobile.
This innovative device, designed to serve the visually impaired, is handy, easy to use with high accuracy.

procedure:
1. first you need to take the microsoft computer vision api servise from "https://azure.microsoft.com/en-in/services/cognitive-services/computer-vision/".
2. Take the Amazon DynamoDb services. create your table as per the program.
3. login to Alexa developer console and create a skill.
4. download Alexa app on your phone and turn on the skill you created.
5. test.
