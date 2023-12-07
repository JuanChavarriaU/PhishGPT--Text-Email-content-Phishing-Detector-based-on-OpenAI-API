from flask import Flask, render_template, request
import data as data
import chat as chat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def text_input():
    if request.method=='POST':
        user_input = data.textHandler(request.form['user_input'])
        prompt = f'''Classify if the following text is phishing or legitimate: 
                
                    User submitted text: {user_input} 

                    Classify if all information in the email is legitimate or phishing. Provide your classification and a percentage likelihood score.
                    
                    JSON Output format: 
                    classification: Phishing or No Phishing
                    Likelihood: porcentage %
                    details: response'''
        gpt_response, likelihood, classification  = chat.query(prompt)
        print(classification, likelihood)
        return render_template('results.html', user_input=user_input, input_type='Text', gpt_response=gpt_response, classification=classification, likelihood=likelihood)
    

if __name__ == '__main__':
    app.run()
