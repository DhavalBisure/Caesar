from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/page")
def crypto():
    return render_template("crypto.html")

@app.route("/encrypt", methods = ["POST"])
def encrypt():
    text = request.values["plain"]
    shift = int(request.values["key"])
    cipherText = ""       
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         cipherText+= chr((ord(char) + shift-65) % 26 + 65)  
            
      # Encrypt lowercase characters in plain text
      else:
         cipherText += chr((ord(char) + shift - 97) % 26 + 97)
      
    return cipherText

@app.route("/decrypt", methods=["POST"])
def decrypt():
    cryptText = request.values["crypt"]
   
    shift = int(request.values["key"])
    plainText = ""
    
    for i in range(len(cryptText)):
        char = cryptText[i]

        if(char.isupper()):
            plainText+= chr((ord(char) -shift - 65)%26 +65) 

        else:
            plainText+= chr((ord(char) - shift - 97) % 26 +97)        
        
    return plainText
app.run(debug = True)
