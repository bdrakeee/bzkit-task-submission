from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    user_index = set()
    result = []
    for i in range(len(USERS)):
        if "id" in args:
            if args["id"] == USERS[i]["id"]:
                user_index.add(i)
        if "name" in args:
            if args["name"].lower() in USERS[i]["name"].lower():
                user_index.add(i)
        if "age" in args:
            if USERS[i]["age"] in [int(args["age"]), int(args["age"])+1, int(args["age"])-1]:
                user_index.add(i)
        if "occupation" in args:
            if args["occupation"].lower() in USERS[i]["occupation"].lower():
                user_index.add(i)
        
        result = [USERS[i] for i in user_index]


    return result
