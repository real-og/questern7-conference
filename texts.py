import aiotables


no_team_error = 'Такой команды не найдено'

async def generate_all_scores():
    team_names, scores = await aiotables.get_all_scores()
    mess = f"""{team_names[0]} - <b>{scores[0]}</b>
{team_names[1]} - <b>{scores[1]}</b>
{team_names[2]} - <b>{scores[2]}</b>
{team_names[3]} - <b>{scores[3]}</b>
{team_names[4]} - <b>{scores[4]}</b>
{team_names[5]} - <b>{scores[5]}</b>"""
    return mess


async def generate_score_by_name(name):
    row_values, rooms_names = await aiotables.get_score(name)
    if row_values == None:
        return no_team_error
    mess = f"""Команда <b>{row_values[0]}</b>

{rooms_names[0]} - <b>{row_values[1]}</b>
{rooms_names[1]} - <b>{row_values[2]}</b>
{rooms_names[2]} - <b>{row_values[3]}</b>
{rooms_names[3]} - <b>{row_values[4]}</b>
{rooms_names[4]} - <b>{row_values[5]}</b>
{rooms_names[5]} - <b>{row_values[6]}</b>

{rooms_names[6]} - <b>{row_values[7]}</b>
    """
    return mess


start_message = 'Здесь можешь задать вопрос и получить счет'