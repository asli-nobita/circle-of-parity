import itertools
import random

def round_robin(n):
  teams = list(range(1, n + 1))
  matches = list(itertools.combinations(teams, 2))

  results = {}
  team_wins = {team: 0 for team in teams}
  team_losses = {team: 0 for team in teams}

  for match in matches:
    team1, team2 = match
    result = random.choice(['1', '2'])

    if result == '1':
      results[match] = f"Team {team1} wins"
      team_wins[team1] += 1
      team_losses[team2] += 1
    else:
      results[match] = f"Team {team2} wins"
      team_wins[team2] += 1
      team_losses[team1] += 1

  print("\nTournament Results:")
  print("{:<12} {:<12} {:<12}".format("Team 1", "Team 2", "Result"))
  print("-"*36)
  for match, result in results.items():
    print("{:<12} {:<12} {:<12}".format(f"Team {match[0]}", f"Team {match[1]}", result))

  # Display the final tally table
  print("\nFinal Tally:")
  print("{:<12} {:<12} {:<12}".format("Team", "Matches Won", "Matches Lost"))
  print("-"*36)
  for team in teams:
    print("{:<12} {:<12} {:<12}".format(f"Team {team}", team_wins[team], team_losses[team]))
  for team in teams:
    flag = 0
    if team_wins[team] == 0 or team_losses[team] == 0:
      flag = 1
      break
  if flag == 1:
    print("\nCircle of Parity is not possible!")
  else:
    print("\nCircle of Parity is possible!")

n = int(input("No. of teams: "))
round_robin(n)
