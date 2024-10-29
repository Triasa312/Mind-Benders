from flask import Flask, render_template, request, jsonify, session
from serpapi import GoogleSearch

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('newhomepage.html')


# Medicines page route
@app.route('/medicines')
def medicines():
    return render_template('medicines.html')

# Appointments page route
@app.route('/appointments')
def appointments():
    return render_template('appointments.html')

# Food ordering page route
@app.route('/foodordering')
def foodordering():
    return render_template('foodordering.html')

# Clothes page route
@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

# Sign-in page route
@app.route('/signin')
def signin():
    return render_template('signin.html')
# privacy route
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
@app.route('/term')
def term():
    return render_template('term.html')


@app.route('/account')
def account():
    # Assuming you have the user's name stored in the session
    user_name = session.get('user_name', 'Guest')  # Replace 'Guest' with a default if not logged in
    return render_template('accounts.html', user_name=user_name)
# In your Flask app
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/pet')
def pet():
    return render_template('pet.html')

# API endpoint to get vets based on pincode
@app.route('/get_vets', methods=['GET'])
def get_vets():
    pincode = request.args.get('pincode')
    location = f"{pincode}, India"
    
    # Define parameters for SerpAPI request
    params = {
        "q": "Vet near me",
        "location": location,  # Use the pincode in the location
        "hl": "en",  # Set the language to English
        "gl": "in",  # Country code for India
        "google_domain": "google.co.in",  # Use Google India domain
        "api_key": "8c48cacef3b3978d6e3ab55d191c2cdf761fe9c1e876ff9a3a6bc35f6c270d72"  # Replace with your actual SerpAPI key
}

    # Perform the search using GoogleSearch
    search = GoogleSearch(params)
    results = search.get_dict()
    vets_info = []

    if "local_results" in results and "places" in results["local_results"]:
        for vet in results["local_results"]["places"]:
            vet_info = {
                "name": vet.get('title', 'N/A'),
                "address": vet.get('address', 'N/A'),
                "rating": vet.get('rating', 'N/A'),
                "phone": vet.get('phone', 'N/A')
            }
            vets_info.append(vet_info)
    
    return jsonify(vets_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
