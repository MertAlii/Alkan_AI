from flask import Flask, request, jsonify
from flask_cors import CORS
from database import initialize_db, add_note, get_notes, add_event, get_events
from assistant import detect_intent, get_gemini_response

app = Flask(__name__)
CORS(app)

initialize_db()

@app.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        data = request.json
        add_note(data.get('content'))
        return jsonify({"message": "Not eklendi"})
    else:
        return jsonify(get_notes())

@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        data = request.json
        add_event(data.get('description'), data.get('date'))
        return jsonify({"message": "Etkinlik eklendi"})
    else:
        return jsonify(get_events())

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    
    try:
        intent = detect_intent(message)
    except:
        intent = "general"

    if intent == "not_ozet":
        notes = get_notes()
        all_notes = "\n".join([f"- {n[0]}" for n in notes])
        prompt = f"Kullanıcı notları:\n{all_notes}\nSoru: {message}"
        response = get_gemini_response(prompt)
    else:
        response = get_gemini_response(message)
        
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)