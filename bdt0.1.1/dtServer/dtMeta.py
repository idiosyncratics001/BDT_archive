dtMeta = [
    {
        "title": "Ryu's Data Tools",
        "name": "root",
        "description": "Operations with users. The **login** logic is also here.",
        "date created": "22-11-2020",
        "last modified": "14-12-2020",
    },
    {
        "name": "main",
        "description": "Manage personal items. Goodmorning / announcenments / messages / tips.",
        "date": "22-11-2020", 
        "last modified": "05-12-2020",
        "externalDocs": {"description": "Items external docs", "url": "https://fastapi.tiangolo.com/",},
    },
    {
        "name": "dashboard",
        "description": "Operations with tasks.",
        "date created": "09-12-2020",
        "last modified": "21-12-2020",
    },
    {
        "name": "about",
        "description": "references and thanks to sources.",
        "date created": "09-12-2020",
        "last modified": "21-12-2020",
    },
    {
        "name": "jupyterlab",
        "description": "Functions to start a session and launch lab in a new tab.",
        "date created": "08-12-2020",
    },
]

def return_me(pageid = str):
    return list(filter(lambda x:x["name"]== pageid, dtMeta))
