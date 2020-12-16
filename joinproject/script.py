string = "Join the project for our"
event = " Hacky New Year Hackathon"
date = " Jan 9th 9am-5pm."

projects = [" Accessibility Ratings ", " Every Voice Engaged ", " Fire Refuge ", " Little Help Book ", " Nonprofit Exchange Hub "," Orcasound ", " ShelterApp/Strappd "]

for project in projects:
  newstring = string[:17] + project + string[17:] + event + date
  print(newstring)