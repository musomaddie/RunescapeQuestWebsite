from flask import *
import database as db


app = Flask(__name__)
app.secret_key = "super_secret31415926535"


@app.route('/')
def main_page():
    return redirect(url_for('list_all_quests'))


@app.route('/list_all_quests', methods=['GET'])
def list_all_quests():
    quest_list = [x[0] for x in db.get_all_quest_names()]
    return render_template('list_all_quests.html', quest_list=quest_list)


@app.route('/view_quest/<quest_name>', methods=['GET', 'POST'])
def view_quest(quest_name):
    quest_info = db.get_quest_info(quest_name)
    return render_template('view_quest.html', quest_info=quest_info)


@app.route('/view_quest_table/<quest_name>', methods=['GET', 'POST'])
def view_quest_table(quest_name):
    all_quests = db.get_quest_info_including_sub(quest_name)
    return render_template('view_quest_table.html', all_quests=all_quests)


@app.route('/free/<value>', methods=['GET'])
def list_all_free_or_members_quests(value):
    quest_list = [x[0] for x in db.get_all_free_or_members_quests(value)]
    return render_template('list_all_quests.html', quest_list=quest_list)


@app.route('/age/<value>', methods=['GET'])
def list_all_age_quests(value):
    quest_list = [x[0] for x in db.get_all_age_quests(value)]
    return render_template('list_all_quests.html', quest_list=quest_list)
