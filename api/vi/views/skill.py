#!/usr/bin/python3
"""defines view functions to handle requests for skill data"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.skill import Skill
app = Flask(__name__)


@app_views.route('/skill', methods=['GET'], strict_slashes=False)
def get_skill():
    """Retrieves all Skill objects from database and returns a list containing
    all of them"""
    skill_dict = storage.all(Song)
    skill_list = []
    for skill in skill_dict.values():
        skill_list.append(skill.to_dict())
    return jsonify(skill_list), 200


@app_views.route('/skill/<text>', methods=['GET'], strict_slashes=False)
def get_skill(text):
    """Retrieves Skill object from database and returns a dictionary"""
    skill_dict = storage.all(Skill)
    return jsonify(skill_dict.get("Skill.{:}".format(text)).to_dict()), 200
