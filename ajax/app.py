
from flask.app import Flask
from flask.templating import render_template
from flask.globals import request


app=Flask(__name__)


@app.route("/")
def function():
    if request.method=="GET":
        return render_template("homepage.html")
    
@app.route("/sugestion/<suggest>",methods=["GET","POST"])
def suggestion(suggest):
    suggestions=''
    states=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    
    
    if suggest is not None:
        for i in range(len(states)):
            if states[i].upper().startswith(suggest.upper()):
                suggestions +=states[i]+"<br>"
        print(suggestions)
                
    return f"{suggestions}"



if __name__ == "__main__":
    app.run(host="localhost",port=1418,debug=True)