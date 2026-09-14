def show_match_result(home_team, away_team, home_score, away_score):
     if home_score > away_score:
         print(f"{home_team} {home_score} : {away_score} {away_team} - The {home_team} team won!")
     elif home_score < away_score:
         print(f"{away_team} {away_score} : {home_score} {home_team} - The {away_team} team won!")
     else:
         print(f"{home_team} {home_score} : {away_score} {away_team} - The match ended in a draw.")


show_match_result("Liverpool", "Chelsea", 0, 3)
show_match_result("Liverpool", "Chelsea", 3, 0)
show_match_result("Liverpool", "Chelsea", 2, 2)