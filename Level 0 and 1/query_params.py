from flask import Flask,jsonify,request

app= Flask(__name__)

@app.route("/search",methods=['GET'])
def query_params():
    query=request.args.get('query')
 
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    return jsonify({"query":query}),200

if __name__=="__main__":
    app.run(debug=True)