from flask import Flask, jsonify , request
app=Flask(__name__)
@app.route('/cal' , methods=['POST'])
def gather():
    data=request.get_json()
    output=None
    name=data['name']
    print(name)
    age=data['age']
    print(age)
    ra_no=data['random_number']
    print(ra_no)
    output=int(age) + int(ra_no)
    return(jsonify({"output":output}))

@app.route('/details',methods=['GET'])
def fetch():
    details=[1,2,3,4]
    return(jsonify({"output": details}))

if __name__ =='__main__' :
    app.run(port=9000,debug=True)