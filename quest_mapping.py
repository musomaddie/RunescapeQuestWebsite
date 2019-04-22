import sqlite3

MY_DATABASE = "db/quests.db"


class _Vertex_QuestDependencyGraph:
    """ Stores the quest as a vertex in the quest dependency graph
        Parameters:
            quest_name: the name of the quest as it appears in the db
            score: the skill score associated with the given quest
    """
    def __init__(self, quest_name):
        self.quest_name = quest_name
        self.full_processed = False
        self.sub_quests = []
        self.quests_immediate_require = 0
        self.quests_all_require = 0
        self.overall_subquests_length = 0


def get_all_quest_names():
    """Queries the database for all the quest names

    Returns:
        list<tuple<str>> a list of tuples of which the first (and only) element
            is the name of the quest
    """
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM quest_details")
    results = cur.fetchall()
    cur.close()
    conn.close()
    if results is None:
        return []
    return results


def _get_subquests(quest):
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute(""" SELECT pre_quest
                    FROM pre_quests
                    WHERE main_quest=?""", (quest,))
    subquests = [x[0] for x in cur.fetchall()]
    cur.close()
    conn.close()
    return subquests


def perform_bfs(start_quest, graph):
    # TODO: almost fully rewrite later, behaviour will differ for the
    # different options I guess.
    visited = [start_quest]
    can_reach = graph[start_quest.quest_name].sub_quests  # ignoring the full
    # complete here since still need to include them no
    while (can_reach):
        current_quest = can_reach.pop()
        visited.append(current_quest)

        # Update start quest score

        # Add its subquests
        for sq in current_quest.sub_quests:
            if (sq not in visited and
                sq not in can_reach and
                not sq.full_processed):
                # Problaby want to remove full_processed, still want to count
                # just not get subquests for
                can_reach.append(sq)

    start_quest.full_processsed = True


def _calculate_graph_overall_score(graph):
    # TODO: try and speed this up by doing them in heap order with the fewest
    # dependencies being down first. Challenge is will need a fast way to count
    # these. Probably best to have an extra database table and refer to that.
    for quest in graph:
        perform_bfs(graph[quest], graph)
    return graph


def _build_quest_dependency_graph(subquests_by_quest):
    # Add every node as a vertex
    # Only include quests we haven't completed / cannot complete
    graph = {}
    for quest in get_all_quest_names():
        quest = quest[0]
        graph[quest] = _Vertex_QuestDependencyGraph(quest)

    # Add all the relevant edges -> ignoring quests completed / can complete
    for quest in subquests_by_quest:
        # subquests_by_quest should actually have all the subquests now
        for sq in subquests_by_quest[quest]:
            if sq in graph:
                graph[quest].sub_quests.append(graph[sq])

    # Great we have all of this so now we need to actually calculate the score
    # overall
    return _calculate_graph_overall_score(graph)


def generate_info():
    all_quests = [x[0] for x in get_all_quest_names()]
    subquests_for_quest = {}
    for quest in all_quests:
        subquests_for_quest[quest] = _get_subquests(quest)

    quest_graph = _build_quest_dependency_graph(subquests_for_quest)
    return quest_graph


generate_info()
