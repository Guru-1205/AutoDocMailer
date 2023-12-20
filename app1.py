from flask import Flask, render_template, request, send_file
from flask_mail import Mail, Message
from io import BytesIO
from docx import Document
from docx.shared import Pt

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'premguru1045@gmail.com'
app.config['MAIL_PASSWORD'] = 'lzyy wors izla arxw'

mail = Mail(app)

template_path = 'static/template.docx'
custom_font_path = 'static/fonts/times new roman bold.ttf'
custom_font_size = Pt(12)  # Set the desired font size


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # Get user input from the form
    replace_dict = {
        '{{activityName}}': request.form['name'],
        '{{activityFromDate}}': request.form['fromDate'],
        '{{activityYear}}': request.form['year'],
        '{{activityDate}}': request.form['date'],
        '{{activityPlace}}': request.form['place'],
        '{{activityDuration}}': request.form['timing'],
        '{{activityDay}}': request.form['day']
    }

    # Load the Word document template
    with open(template_path, 'rb') as doc_stream:
        doc = Document(BytesIO(doc_stream.read()))

    # Replace placeholders with user input
    for paragraph in doc.paragraphs:
        for key, value in replace_dict.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, str(value))

    # Create an in-memory stream for the modified document
    output_stream = BytesIO()
    doc.save(output_stream)

    # Move the stream cursor to the beginning
    output_stream.seek(0)

    # Send the modified document via email
    send_email(request.form['receiver_email'], output_stream)

    return "Email sent successfully!"


def send_email(receiver_email, attachment_stream):
    em = Message(
        'Subject of the email',
        sender='premguru1045@gmail.com',
        recipients=[receiver_email]
    )
    em.body = 'Hello, this is a test message.'
    em.attach('output_document.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
              attachment_stream.read())
    mail.send(em)


# if __name__ == '__main__':
#     app.run(debug=True)
