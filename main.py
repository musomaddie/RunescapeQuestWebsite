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


@app.route('/view_quest/<quest_name>', methods=['GET'])
def view_quest(quest_name):
    quest_info = db.get_quest_info(quest_name)
    print(quest_info)
    return render_template('view_quest.html')
