from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for notes
notes = []
note_id_counter = 1

# Helper function to find a note by ID
def find_note(note_id):
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

# Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    global note_id_counter
    if not request.json or 'content' not in request.json:
        abort(400)  # Bad Request
    note = {
        'id': note_id_counter,
        'content': request.json['content'],
    }
    notes.append(note)
    note_id_counter += 1
    return jsonify(note), 201  # Created

# Get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

# Get a specific note by ID
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = find_note(note_id)
    if note is None:
        abort(404)  # Not Found
    return jsonify(note)

# Update a note by ID
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = find_note(note_id)
    if note is None:
        abort(404)  # Not Found
    if not request.json or 'content' not in request.json:
        abort(400)  # Bad Request
    note['content'] = request.json['content']
    return jsonify(note)

# Delete a note by ID
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = find_note(note_id)
    if note is None:
        abort(404)  # Not Found
    notes.remove(note)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
