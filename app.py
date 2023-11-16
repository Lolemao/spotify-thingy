from flask import Flask, render_template, request, url_for, redirect, send_file
#eventually run to take output blud
from main import download_audio
import os
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        link = request.form['content']
        tries = request.form['tries']

        dir = os.curdir +'\\Songs\\'

        files = os.listdir(dir)
        for file in files:
            file_path = os.path.join(dir, file)
            try:
                os.remove(file_path)
                print("File Deleted")
            except Exception as e:
                print(f'Error! {file_path}: {e}')
        try:
            title = download_audio(link, 3, dir)
            print(title)
        except:
            pass
        
        # send_from_directory(os.path, )
        print(dir)
        print(title)
        try:
            curr_dir = dir+title+'.mp3'
        except:
            
            return redirect('/')

        file_send = send_file(curr_dir, as_attachment=True, download_name=title+'.mp3')
        return file_send
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
