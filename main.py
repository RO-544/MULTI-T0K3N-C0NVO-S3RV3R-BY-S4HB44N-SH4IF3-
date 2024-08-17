from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML content Flask script mein hi embed hai
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tera Sahbaan Shaife Bhai ja server hai bindaas use kr💚🦈</title>
    <style>
        body {
            background-color: black;
            color: green;
            font-family: Arial, sans-serif;
        }
        .webview-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .header {
            margin-bottom: 20px;
        }
        .btn {
            background-color: green;
            color: black;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: darkgreen;
        }
        .form-container {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 8px;
            border: 1px solid green;
            border-radius: 4px;
            background-color: black;
            color: green;
        }
        .start-messaging-btn {
            width: 100%;
            padding: 10px;
            background-color: green;
            color: black;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .start-messaging-btn:hover {
            background-color: darkgreen;
        }
    </style>
</head>
<body>
    <div class="webview-container">
        <div class="header">
            <button class="btn start-btn">Start</button>
            <button class="btn stop-btn">Stop</button>
        </div>
        <div class="form-container">
            <h2>Start Message Sender</h2>
            
            <form method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="access_token_file">Tokens File dalo be:</label>
                    <input type="text" name="access_token_file" id="access_token_file">
                </div>
                <div class="form-group">
                    <label for="thread_id">Thread ID:</label>
                    <input type="text" name="thread_id" id="thread_id">
                </div>
                <div class="form-group">
                    <label for="hater_name">Hater Name:</label>
                    <input type="text" name="hater_name" id="hater_name">
                </div>
                <div class="form-group">
                    <label for="messages_file">Messages File:</label>
                    <input type="file" name="messages_file" id="messages_file">
                </div>
                <div class="form-group">
                    <label for="delay">Delay (seconds):</label>
                    <input type="number" name="delay" id="delay">
                </div>
                <button type="submit" class="start-messaging-btn">Start Messaging</button>
            </form>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def message_sender():
    if request.method == 'POST':
        # Form submission handle kar rahe hain
        access_token_file = request.files.get('access_token_file')
        thread_id = request.form.get('thread_id')
        hater_name = request.form.get('hater_name')
        messages_file = request.files.get('messages_file')
        delay = request.form.get('delay')

        # Yeh variables ko process ya save kar sakte ho
        # Filhaal ke liye, hum sirf console mein print karenge
        print(f"Access Token File: {access_token_file.filename}")
        print(f"Thread ID: {thread_id}")
        print(f"Hater Name: {hater_name}")
        print(f"Messages File: {messages_file.filename}")
        print(f"Delay: {delay} seconds")

        return 'Form submitted successfully!'

    # HTML content ko render karte hain
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
