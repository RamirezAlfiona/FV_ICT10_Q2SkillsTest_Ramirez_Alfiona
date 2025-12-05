from pyscript import document

club_info = {
    "marching_band": {
        'selected_club': "Marching Band",
        'Description': 'A club where you can learn, improve, and show your skills by playing instruments.',
        'Meeting Time': 'Tuesday and Wednesday 03:00-4:30 PM',
        'Location': 'Band Room',
        'Advisor': 'Mr. Emilio Alumno',
        'Number of Members': 35
    },
    "glee": {
        'selected_club': "Glee Club",
        'Description': 'A club for people who can sing well and sing their hearts out.',
        'Meeting Time': 'Monday 03:00- 05:00 PM',
        'Location': 'High School Music Room',
        'Advisor': 'Mr. Denver Martin',
        'Number of Members': 30
    },
    "dance": {
        'selected_club': "Dance Club",
        'Description': 'A club for those who have good and groovy moves.',
        'Meeting Time': 'Tuesday 03:00 - 05:00 PM',
        'Location': 'Teatro Preciosa',
        'Advisor': 'Mr. Alfred Cases',
        'Number of Members': 27
    },
    "math": {
        'selected_club': "Math Club",
        'Description': 'A club for those math wizards in school.',
        'Meeting Time': 'Monday 02:30- 03:00 PM',
        'Location': 'Room 404',
        'Advisor': 'Mr. Nicole Gabuya',
        'Number of Members': 20
    },
    "science": {
        'selected_club': "Science Club",
        'Description': 'A club for the science nerds.',
        'Meeting Time': 'Tuesday 03:00 - 04:00 PM',
        'Location': 'Room 404',
        'Advisor': 'Ms. Jameelyn Maramag',
        'Number of Members': 25
    },
    "com_arts": {
        'selected_club': "Communications Arts Club",
        'Description': 'A club for people who love English.',
        'Meeting Time': 'Wednesday 03:00 - 04:00 PM, Friday 03:00 - 04:00 PM',
        'Location': 'Room 406',
        'Advisor': 'Ms. Yannis Fernandez',
        'Number of Members': 23
    }
}

def club_information(e):
    selected = document.getElementById("clubs").value
    info = club_info[selected]

    output = f"""
{info['selected_club']}
Description: {info['Description']}
Meeting Time: {info['Meeting Time']}
Location: {info['Location']}
Advisor: {info['Advisor']}
Number of Members: {info['Number of Members']}
"""

    document.getElementById("output").textContent = output
