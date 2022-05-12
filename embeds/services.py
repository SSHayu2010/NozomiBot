import csv
from datetime import date


def extract_unit_database_from_csv():
    """Transform a csv units file in json data
    fields: name, rank, stars, ue_level, notes, imagen, thumbnail, specific_rank, unit_type
    rows: [['Christina', '14-3', '5', 'Sin UE', 'No hay restriccion', 'https://i.imgur.com/NyCozR2.jpg',
         'https://i.imgur.com/OH7t19d.png', '', 'phy'], [
    """
    # csv file name
    filename = "units_database.csv"

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    return fields, rows


def transform_unit_data_to_objects(fields, rows):
    """Transform a csv units file in json data
    fields: name, rank, stars, ue_level, notes, imagen, thumbnail, specific_rank, unit_type
    rows: [['Christina', '14-3', '5', 'Sin UE', 'No hay restriccion', 'https://i.imgur.com/NyCozR2.jpg',
    return: [
        {
            "name": "Kokkoro",
            "rank": "5",
            "stars": "5",
            "ue_level": "130",
            "notes": "Notas del personaje",
            "image": "https://.../1.png",
            "thumbnail": "https://.../thumbnail 1",
            "specific_rank": "https://www.unitenames.com/images/units/1.png",
            "unit_type": "phy"
        },
        {
            "name": "Christina",
            ...
    """
    # initializing the list of dictionaries
    unit_data = []
    for row in rows:
        # parsing each column of a row
        unit_data.append({
            fields[0]: str(row[0]).lower(),
            fields[1]: row[1],
            fields[2]: row[2],
            fields[3]: row[3],
            fields[4]: row[4],
            fields[5]: row[5],
            fields[6]: row[6],
            fields[7]: row[7],
            fields[8]: row[8]
        })
    print(f'Se cargaron un total de {len(unit_data)} unidades')
    return unit_data


def refactor_unit_name(string):
    """Replace the first letter of a string in uppercase
    """
    separated_string = string.split('.')
    if len(separated_string) > 1:
        string_refactor = separated_string[0].upper() + '.' + separated_string[1].capitalize()
    else:
        string_refactor = string.capitalize()
    return string_refactor


def get_current_date():
    """Get the current date"""
    today = date.today()
    return today.strftime("%B, %Y")
