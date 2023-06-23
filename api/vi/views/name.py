#!/usr/bin/python3
"""defines view functions to handle requests for name data"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.skill import Skill
from models.location import Location
from models.name import Name
from better_profanity import profanity
app = Flask(__name__)


@app_views.route('/name/<location_id>/<skill_id>', methods=['GET'],
                 strict_slashes=False)
def get_name(location_id=None, skill_id=None):
    """Retrieves all Name objects for a location from a skill and returns
    a list containing all of them"""
    location = storage.get('Location', location_id)
    if location is None:
        abort(404)
    skill = storage.get('Skill', skill_id)
    if skill is None:
        abort(404)
    name_dict = storage.all(Name)
    name_list = []
    for name in name_dict.values():
        if name.location_id == location_id and name.skill_id == skill_id:
            name_list.append(name.to_dict())
    return jsonify(name_list), 200


@app_views.route('/interpretations/<word_id>/<song_id>', methods=['POST'],
                 strict_slashes=False)
def post_interpretation(word_id=None, song_id=None):
    """Creates an interpretation for a word from a song"""
    print(word_id)
    print(song_id)
    word = storage.get('Word', word_id)
    if word is None:
        abort(404)
    song = storage.get('Song', song_id)
    if song is None:
        abort(404)
    result = request.get_json()
    if result is None:
        return jsonify({"error": "Not a JSON"}), 400
    if 'text' not in result:
        return jsonify({"error": "Missing text"}), 400
    if profanity.contains_profanity(result["text"]) is True:
        return jsonify({"error": "Profane"}), 400
    interpretation_obj = Interpretation(word_id=word_id, song_id=song_id)
    setattr(interpretation_obj, "text", result["text"])
    storage.new(interpretation_obj)
    storage.save()
    return jsonify(interpretation_obj.to_dict()), 201


@app_views.route('/interpretations/<interpretation_id>', methods=['PUT'],
                 strict_slashes=False)
def put_interpretation(interpretation_id=None):
    """Updates an Interpretation object"""
    interpretation_obj = storage.get('Interpretation', interpretation_id)
    if interpretation_obj is None:
        abort(404)
    result = request.get_json()
    if result is None:
        return jsonify({"error": "Not a JSON"}), 400
    if 'likes' not in result:
        return jsonify({"error": "Missing likes"}), 400
    setattr(interpretation_obj, "likes", result["likes"])
    storage.save()
    return jsonify(interpretation_obj.to_dict()), 200
