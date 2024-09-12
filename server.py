''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the list of emotions 
        and its score for the provided text, as well as, the 
        dominant emotion
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if not response['dominant_emotion']:
        return 'Invalid text! Please try again!'

    return f"""
        'anger': {response['anger']}, 
        'disgust': {response['disgust']},
        'fear': {response['fear']},
        'joy': {response['joy']},
        'sadness': {response['sadness']},
        The dominant emition is {response['dominant_emotion']}
        """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
