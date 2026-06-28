from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="Fudbalska Taktika Pro")

# ============= 150+ IGRAČA =============
SVI_IGRACI = [
    # GOLMANI (15)
    {"ime": "Jan Oblak", "pozicija": "GK", "drzava": "Slovenija", "klub": "Atletico Madrid", "rating": 88},
    {"ime": "Thibaut Courtois", "pozicija": "GK", "drzava": "Belgija", "klub": "Real Madrid", "rating": 90},
    {"ime": "Alisson Becker", "pozicija": "GK", "drzava": "Brazil", "klub": "Liverpool", "rating": 89},
    {"ime": "Ederson", "pozicija": "GK", "drzava": "Brazil", "klub": "Manchester City", "rating": 88},
    {"ime": "Manuel Neuer", "pozicija": "GK", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 87},
    {"ime": "Gianluigi Donnarumma", "pozicija": "GK", "drzava": "Italija", "klub": "PSG", "rating": 87},
    {"ime": "Mike Maignan", "pozicija": "GK", "drzava": "Francuska", "klub": "AC Milan", "rating": 86},
    {"ime": "Emiliano Martinez", "pozicija": "GK", "drzava": "Argentina", "klub": "Aston Villa", "rating": 85},
    {"ime": "David Raya", "pozicija": "GK", "drzava": "Španija", "klub": "Arsenal", "rating": 84},
    {"ime": "Diogo Costa", "pozicija": "GK", "drzava": "Portugal", "klub": "Porto", "rating": 84},
    {"ime": "Keylor Navas", "pozicija": "GK", "drzava": "Kostarika", "klub": "PSG", "rating": 83},
    {"ime": "Jordan Pickford", "pozicija": "GK", "drzava": "Engleska", "klub": "Everton", "rating": 83},
    {"ime": "Kepa Arrizabalaga", "pozicija": "GK", "drzava": "Španija", "klub": "Real Madrid", "rating": 82},
    {"ime": "Marc-Andre ter Stegen", "pozicija": "GK", "drzava": "Njemačka", "klub": "Barcelona", "rating": 86},
    {"ime": "Andriy Lunin", "pozicija": "GK", "drzava": "Ukrajina", "klub": "Real Madrid", "rating": 81},
    
    # ODBRAMBENI - CB (30)
    {"ime": "Virgil van Dijk", "pozicija": "CB", "drzava": "Holandija", "klub": "Liverpool", "rating": 89},
    {"ime": "Ruben Dias", "pozicija": "CB", "drzava": "Portugal", "klub": "Manchester City", "rating": 88},
    {"ime": "Antonio Rudiger", "pozicija": "CB", "drzava": "Njemačka", "klub": "Real Madrid", "rating": 87},
    {"ime": "David Alaba", "pozicija": "CB", "drzava": "Austrija", "klub": "Real Madrid", "rating": 86},
    {"ime": "Marquinhos", "pozicija": "CB", "drzava": "Brazil", "klub": "PSG", "rating": 87},
    {"ime": "Milan Skriniar", "pozicija": "CB", "drzava": "Slovačka", "klub": "PSG", "rating": 86},
    {"ime": "Matthijs de Ligt", "pozicija": "CB", "drzava": "Holandija", "klub": "Bayern Munich", "rating": 86},
    {"ime": "John Stones", "pozicija": "CB", "drzava": "Engleska", "klub": "Manchester City", "rating": 85},
    {"ime": "Kalidou Koulibaly", "pozicija": "CB", "drzava": "Senegal", "klub": "Al Hilal", "rating": 85},
    {"ime": "Alessandro Bastoni", "pozicija": "CB", "drzava": "Italija", "klub": "Inter Milan", "rating": 85},
    {"ime": "Eder Militao", "pozicija": "CB", "drzava": "Brazil", "klub": "Real Madrid", "rating": 85},
    {"ime": "Ronald Araujo", "pozicija": "CB", "drzava": "Urugvaj", "klub": "Barcelona", "rating": 85},
    {"ime": "Kim Min-jae", "pozicija": "CB", "drzava": "Južna Koreja", "klub": "Bayern Munich", "rating": 84},
    {"ime": "William Saliba", "pozicija": "CB", "drzava": "Francuska", "klub": "Arsenal", "rating": 84},
    {"ime": "Dayot Upamecano", "pozicija": "CB", "drzava": "Francuska", "klub": "Bayern Munich", "rating": 84},
    {"ime": "Lisandro Martinez", "pozicija": "CB", "drzava": "Argentina", "klub": "Manchester United", "rating": 84},
    {"ime": "Jules Kounde", "pozicija": "CB", "drzava": "Francuska", "klub": "Barcelona", "rating": 84},
    {"ime": "Cristian Romero", "pozicija": "CB", "drzava": "Argentina", "klub": "Tottenham", "rating": 83},
    {"ime": "Gabriel Magalhaes", "pozicija": "CB", "drzava": "Brazil", "klub": "Arsenal", "rating": 83},
    {"ime": "Ibrahima Konate", "pozicija": "CB", "drzava": "Francuska", "klub": "Liverpool", "rating": 83},
    {"ime": "Pau Torres", "pozicija": "CB", "drzava": "Španija", "klub": "Aston Villa", "rating": 82},
    {"ime": "Aymeric Laporte", "pozicija": "CB", "drzava": "Francuska", "klub": "Al Nassr", "rating": 82},
    {"ime": "Leonardo Bonucci", "pozicija": "CB", "drzava": "Italija", "klub": "Union Berlin", "rating": 81},
    {"ime": "Giorgio Chiellini", "pozicija": "CB", "drzava": "Italija", "klub": "LAFC", "rating": 80},
    {"ime": "Mats Hummels", "pozicija": "CB", "drzava": "Njemačka", "klub": "Borussia Dortmund", "rating": 81},
    {"ime": "Niklas Sule", "pozicija": "CB", "drzava": "Njemačka", "klub": "Borussia Dortmund", "rating": 82},
    {"ime": "Lucas Hernandez", "pozicija": "CB", "drzava": "Francuska", "klub": "PSG", "rating": 84},
    {"ime": "Benjamin Pavard", "pozicija": "CB", "drzava": "Francuska", "klub": "Inter Milan", "rating": 83},
    {"ime": "Stefan de Vrij", "pozicija": "CB", "drzava": "Holandija", "klub": "Inter Milan", "rating": 82},
    {"ime": "Fikayo Tomori", "pozicija": "CB", "drzava": "Engleska", "klub": "AC Milan", "rating": 82},
    
    # BEKOVI - LB/RB (20)
    {"ime": "Theo Hernandez", "pozicija": "LB", "drzava": "Francuska", "klub": "AC Milan", "rating": 85},
    {"ime": "Alphonso Davies", "pozicija": "LB", "drzava": "Kanada", "klub": "Bayern Munich", "rating": 84},
    {"ime": "Andrew Robertson", "pozicija": "LB", "drzava": "Škotska", "klub": "Liverpool", "rating": 85},
    {"ime": "Trent Alexander-Arnold", "pozicija": "RB", "drzava": "Engleska", "klub": "Liverpool", "rating": 86},
    {"ime": "Joao Cancelo", "pozicija": "RB", "drzava": "Portugal", "klub": "Barcelona", "rating": 85},
    {"ime": "Nuno Mendes", "pozicija": "LB", "drzava": "Portugal", "klub": "PSG", "rating": 83},
    {"ime": "Federico Dimarco", "pozicija": "LB", "drzava": "Italija", "klub": "Inter Milan", "rating": 83},
    {"ime": "Kieran Trippier", "pozicija": "RB", "drzava": "Engleska", "klub": "Newcastle", "rating": 84},
    {"ime": "Achraf Hakimi", "pozicija": "RB", "drzava": "Maroko", "klub": "PSG", "rating": 84},
    {"ime": "Jeremie Frimpong", "pozicija": "RB", "drzava": "Holandija", "klub": "Bayer Leverkusen", "rating": 83},
    {"ime": "Raphael Guerreiro", "pozicija": "LB", "drzava": "Portugal", "klub": "Bayern Munich", "rating": 82},
    {"ime": "Ben Chilwell", "pozicija": "LB", "drzava": "Engleska", "klub": "Chelsea", "rating": 82},
    {"ime": "Luke Shaw", "pozicija": "LB", "drzava": "Engleska", "klub": "Manchester United", "rating": 82},
    {"ime": "Reece James", "pozicija": "RB", "drzava": "Engleska", "klub": "Chelsea", "rating": 83},
    {"ime": "Kyle Walker", "pozicija": "RB", "drzava": "Engleska", "klub": "Manchester City", "rating": 84},
    {"ime": "Dani Carvajal", "pozicija": "RB", "drzava": "Španija", "klub": "Real Madrid", "rating": 84},
    {"ime": "Ferland Mendy", "pozicija": "LB", "drzava": "Francuska", "klub": "Real Madrid", "rating": 82},
    {"ime": "Alejandro Grimaldo", "pozicija": "LB", "drzava": "Španija", "klub": "Bayer Leverkusen", "rating": 83},
    {"ime": "Jordi Alba", "pozicija": "LB", "drzava": "Španija", "klub": "Inter Miami", "rating": 81},
    {"ime": "Marcos Acuna", "pozicija": "LB", "drzava": "Argentina", "klub": "Sevilla", "rating": 81},
    
    # VEZNI - CM/CDM/CAM (40)
    {"ime": "Kevin De Bruyne", "pozicija": "CM", "drzava": "Belgija", "klub": "Manchester City", "rating": 91},
    {"ime": "Jude Bellingham", "pozicija": "CM", "drzava": "Engleska", "klub": "Real Madrid", "rating": 88},
    {"ime": "Rodri", "pozicija": "CDM", "drzava": "Španija", "klub": "Manchester City", "rating": 88},
    {"ime": "Declan Rice", "pozicija": "CDM", "drzava": "Engleska", "klub": "Arsenal", "rating": 87},
    {"ime": "Federico Valverde", "pozicija": "CM", "drzava": "Urugvaj", "klub": "Real Madrid", "rating": 86},
    {"ime": "Joshua Kimmich", "pozicija": "CDM", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 87},
    {"ime": "Bernardo Silva", "pozicija": "CM", "drzava": "Portugal", "klub": "Manchester City", "rating": 87},
    {"ime": "Bruno Fernandes", "pozicija": "CAM", "drzava": "Portugal", "klub": "Manchester United", "rating": 86},
    {"ime": "Phil Foden", "pozicija": "CAM", "drzava": "Engleska", "klub": "Manchester City", "rating": 86},
    {"ime": "Jamal Musiala", "pozicija": "CAM", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 85},
    {"ime": "Pedri", "pozicija": "CM", "drzava": "Španija", "klub": "Barcelona", "rating": 85},
    {"ime": "Gavi", "pozicija": "CM", "drzava": "Španija", "klub": "Barcelona", "rating": 84},
    {"ime": "Florian Wirtz", "pozicija": "CAM", "drzava": "Njemačka", "klub": "Bayer Leverkusen", "rating": 84},
    {"ime": "Martin Odegaard", "pozicija": "CAM", "drzava": "Norveška", "klub": "Arsenal", "rating": 85},
    {"ime": "Enzo Fernandez", "pozicija": "CM", "drzava": "Argentina", "klub": "Chelsea", "rating": 84},
    {"ime": "Alexis Mac Allister", "pozicija": "CM", "drzava": "Argentina", "klub": "Liverpool", "rating": 84},
    {"ime": "Leon Goretzka", "pozicija": "CM", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 84},
    {"ime": "Frenkie de Jong", "pozicija": "CM", "drzava": "Holandija", "klub": "Barcelona", "rating": 85},
    {"ime": "Nicolo Barella", "pozicija": "CM", "drzava": "Italija", "klub": "Inter Milan", "rating": 85},
    {"ime": "Sandro Tonali", "pozicija": "CM", "drzava": "Italija", "klub": "Newcastle", "rating": 84},
    {"ime": "Luka Modric", "pozicija": "CM", "drzava": "Hrvatska", "klub": "Real Madrid", "rating": 86},
    {"ime": "Toni Kroos", "pozicija": "CM", "drzava": "Njemačka", "klub": "Real Madrid", "rating": 87},
    {"ime": "Casemiro", "pozicija": "CDM", "drzava": "Brazil", "klub": "Manchester United", "rating": 85},
    {"ime": "Aurelien Tchouameni", "pozicija": "CDM", "drzava": "Francuska", "klub": "Real Madrid", "rating": 85},
    {"ime": "Eduardo Camavinga", "pozicija": "CM", "drzava": "Francuska", "klub": "Real Madrid", "rating": 84},
    {"ime": "James Maddison", "pozicija": "CAM", "drzava": "Engleska", "klub": "Tottenham", "rating": 84},
    {"ime": "Mason Mount", "pozicija": "CM", "drzava": "Engleska", "klub": "Manchester United", "rating": 82},
    {"ime": "Kai Havertz", "pozicija": "CAM", "drzava": "Njemačka", "klub": "Arsenal", "rating": 83},
    {"ime": "Ilkay Gundogan", "pozicija": "CM", "drzava": "Njemačka", "klub": "Barcelona", "rating": 85},
    {"ime": "Mateo Kovacic", "pozicija": "CM", "drzava": "Hrvatska", "klub": "Manchester City", "rating": 84},
    {"ime": "Marcel Sabitzer", "pozicija": "CM", "drzava": "Austrija", "klub": "Borussia Dortmund", "rating": 82},
    {"ime": "Konrad Laimer", "pozicija": "CM", "drzava": "Austrija", "klub": "Bayern Munich", "rating": 82},
    {"ime": "Ryan Gravenberch", "pozicija": "CM", "drzava": "Holandija", "klub": "Liverpool", "rating": 81},
    {"ime": "Teun Koopmeiners", "pozicija": "CM", "drzava": "Holandija", "klub": "Atalanta", "rating": 82},
    {"ime": "Mikel Merino", "pozicija": "CM", "drzava": "Španija", "klub": "Real Sociedad", "rating": 82},
    {"ime": "Fabian Ruiz", "pozicija": "CM", "drzava": "Španija", "klub": "PSG", "rating": 82},
    {"ime": "Carlos Soler", "pozicija": "CM", "drzava": "Španija", "klub": "PSG", "rating": 81},
    {"ime": "Pablo Fornals", "pozicija": "CM", "drzava": "Španija", "klub": "West Ham", "rating": 81},
    {"ime": "Dani Olmo", "pozicija": "CAM", "drzava": "Španija", "klub": "RB Leipzig", "rating": 83},
    {"ime": "Marco Asensio", "pozicija": "CAM", "drzava": "Španija", "klub": "PSG", "rating": 82},
    
    # KRILA (25)
    {"ime": "Vinícius Júnior", "pozicija": "LW", "drzava": "Brazil", "klub": "Real Madrid", "rating": 88},
    {"ime": "Mohamed Salah", "pozicija": "RW", "drzava": "Egipat", "klub": "Liverpool", "rating": 89},
    {"ime": "Neymar Jr", "pozicija": "LW", "drzava": "Brazil", "klub": "Al Hilal", "rating": 87},
    {"ime": "Bukayo Saka", "pozicija": "RW", "drzava": "Engleska", "klub": "Arsenal", "rating": 85},
    {"ime": "Rafael Leao", "pozicija": "LW", "drzava": "Portugal", "klub": "AC Milan", "rating": 85},
    {"ime": "Kingsley Coman", "pozicija": "RW", "drzava": "Francuska", "klub": "Bayern Munich", "rating": 85},
    {"ime": "Leroy Sane", "pozicija": "RW", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 85},
    {"ime": "Marcus Rashford", "pozicija": "LW", "drzava": "Engleska", "klub": "Manchester United", "rating": 84},
    {"ime": "Raheem Sterling", "pozicija": "RW", "drzava": "Engleska", "klub": "Chelsea", "rating": 83},
    {"ime": "Ousmane Dembele", "pozicija": "RW", "drzava": "Francuska", "klub": "PSG", "rating": 84},
    {"ime": "Jack Grealish", "pozicija": "LW", "drzava": "Engleska", "klub": "Manchester City", "rating": 84},
    {"ime": "Serge Gnabry", "pozicija": "RW", "drzava": "Njemačka", "klub": "Bayern Munich", "rating": 84},
    {"ime": "Khvicha Kvaratskhelia", "pozicija": "LW", "drzava": "Gruzija", "klub": "Napoli", "rating": 84},
    {"ime": "Federico Chiesa", "pozicija": "RW", "drzava": "Italija", "klub": "Juventus", "rating": 83},
    {"ime": "Jadon Sancho", "pozicija": "LW", "drzava": "Engleska", "klub": "Manchester United", "rating": 82},
    {"ime": "Antony", "pozicija": "RW", "drzava": "Brazil", "klub": "Manchester United", "rating": 81},
    {"ime": "Riyad Mahrez", "pozicija": "RW", "drzava": "Alžir", "klub": "Al Ahli", "rating": 84},
    {"ime": "Cody Gakpo", "pozicija": "LW", "drzava": "Holandija", "klub": "Liverpool", "rating": 83},
    {"ime": "Luis Diaz", "pozicija": "LW", "drzava": "Kolumbija", "klub": "Liverpool", "rating": 83},
    {"ime": "Gabriel Martinelli", "pozicija": "LW", "drzava": "Brazil", "klub": "Arsenal", "rating": 83},
    {"ime": "Leandro Trossard", "pozicija": "LW", "drzava": "Belgija", "klub": "Arsenal", "rating": 82},
    {"ime": "Mykhailo Mudryk", "pozicija": "LW", "drzava": "Ukrajina", "klub": "Chelsea", "rating": 80},
    {"ime": "Cole Palmer", "pozicija": "RW", "drzava": "Engleska", "klub": "Chelsea", "rating": 83},
    
    # NAPADAČI - ST (20)
    {"ime": "Erling Haaland", "pozicija": "ST", "drzava": "Norveška", "klub": "Manchester City", "rating": 91},
    {"ime": "Kylian Mbappé", "pozicija": "ST", "drzava": "Francuska", "klub": "Real Madrid", "rating": 91},
    {"ime": "Lionel Messi", "pozicija": "ST", "drzava": "Argentina", "klub": "Inter Miami", "rating": 90},
    {"ime": "Cristiano Ronaldo", "pozicija": "ST", "drzava": "Portugal", "klub": "Al Nassr", "rating": 86},
    {"ime": "Harry Kane", "pozicija": "ST", "drzava": "Engleska", "klub": "Bayern Munich", "rating": 90},
    {"ime": "Robert Lewandowski", "pozicija": "ST", "drzava": "Poljska", "klub": "Barcelona", "rating": 88},
    {"ime": "Karim Benzema", "pozicija": "ST", "drzava": "Francuska", "klub": "Al Ittihad", "rating": 86},
    {"ime": "Lautaro Martinez", "pozicija": "ST", "drzava": "Argentina", "klub": "Inter Milan", "rating": 87},
    {"ime": "Victor Osimhen", "pozicija": "ST", "drzava": "Nigerija", "klub": "Napoli", "rating": 86},
    {"ime": "Antoine Griezmann", "pozicija": "ST", "drzava": "Francuska", "klub": "Atletico Madrid", "rating": 86},
    {"ime": "Christopher Nkunku", "pozicija": "ST", "drzava": "Francuska", "klub": "Chelsea", "rating": 84},
    {"ime": "Randal Kolo Muani", "pozicija": "ST", "drzava": "Francuska", "klub": "PSG", "rating": 83},
    {"ime": "Julian Alvarez", "pozicija": "ST", "drzava": "Argentina", "klub": "Manchester City", "rating": 84},
    {"ime": "Gabriel Jesus", "pozicija": "ST", "drzava": "Brazil", "klub": "Arsenal", "rating": 83},
    {"ime": "Darwin Nunez", "pozicija": "ST", "drzava": "Urugvaj", "klub": "Liverpool", "rating": 83},
    {"ime": "Dusan Vlahovic", "pozicija": "ST", "drzava": "Srbija", "klub": "Juventus", "rating": 83},
    {"ime": "Tammy Abraham", "pozicija": "ST", "drzava": "Engleska", "klub": "Roma", "rating": 82},
    {"ime": "Jonathan David", "pozicija": "ST", "drzava": "Kanada", "klub": "Lille", "rating": 82},
    {"ime": "Ciro Immobile", "pozicija": "ST", "drzava": "Italija", "klub": "Lazio", "rating": 82},
    {"ime": "Olivier Giroud", "pozicija": "ST", "drzava": "Francuska", "klub": "AC Milan", "rating": 82},
]

TIMOVI = ["Real Madrid", "Barcelona", "Manchester City", "Liverpool", "Bayern Munich", 
          "PSG", "Arsenal", "Chelsea", "Manchester United", "Juventus", "Inter Milan", 
          "AC Milan", "Napoli", "Borussia Dortmund", "Atletico Madrid"]

# ============= HTML =============
BASE_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Fudbalska Taktika Pro</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #0a0a2a; color: white; min-height: 100vh; }
        nav { background: #1a1a3a; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid gold; flex-wrap: wrap; }
        nav a { color: white; text-decoration: none; padding: 0.5rem 1.5rem; border-radius: 5px; font-weight: 600; }
        nav a:hover { background: gold; color: #0a0a2a; }
        .logo { font-size: 1.8rem; font-weight: bold; color: gold; }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .btn { display: inline-block; background: gold; color: #0a0a2a; padding: 0.75rem 2rem; text-decoration: none; border-radius: 5px; font-weight: bold; border: none; cursor: pointer; }
        .btn:hover { background: #ffed4a; }
        .btn-danger { background: #e74c3c; color: white; }
        .btn-danger:hover { background: #c0392b; }
        .btn-success { background: #2ecc71; color: white; }
        .btn-success:hover { background: #27ae60; }
        .match-setup { background: #1a1a3a; padding: 2rem; border-radius: 10px; border: 1px solid gold; max-width: 1000px; margin: 0 auto; }
        .match-setup h2 { color: gold; text-align: center; margin-bottom: 1.5rem; }
        .team-select { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        .team-box { background: #0a0a2a; padding: 1.5rem; border-radius: 8px; border: 1px solid #333; max-height: 600px; overflow-y: auto; }
        .team-box h3 { margin-bottom: 1rem; }
        .team-box label { display: block; margin: 0.5rem 0 0.2rem; color: #aaa; }
        .team-box select { width: 100%; padding: 0.5rem; border-radius: 5px; border: 1px solid #555; background: #1a1a3a; color: white; }
        .player-list { margin-top: 0.5rem; }
        .player-item { padding: 0.2rem 0.5rem; background: #1a1a3a; margin: 0.1rem 0; border-radius: 3px; font-size: 0.85rem; display: flex; align-items: center; }
        .player-item input { margin-right: 8px; }
        .player-item .pos { color: #888; font-size: 0.75rem; margin-left: 5px; }
        .match-info { background: #1a1a3a; padding: 1.5rem; border-radius: 10px; border: 1px solid gold; margin-top: 2rem; }
        .match-info .score { font-size: 3rem; text-align: center; color: gold; }
        .match-info .time { text-align: center; font-size: 1.5rem; color: #fff; margin: 0.5rem 0; }
        .match-info .stats { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-top: 1rem; }
        .match-info .stat-box { text-align: center; background: #0a0a2a; padding: 1rem; border-radius: 8px; }
        .match-info .stat-box .value { font-size: 1.5rem; color: gold; }
        .match-log { background: #0a0a2a; padding: 1rem; border-radius: 8px; max-height: 300px; overflow-y: auto; margin-top: 1rem; }
        .match-log .log-entry { padding: 0.3rem 0; border-bottom: 1px solid #1a1a3a; font-size: 0.9rem; }
        .goal { color: gold; font-weight: bold; }
        .yellow { color: #f1c40f; }
        .red { color: #e74c3c; font-weight: bold; }
        .active-link { background: gold; color: #0a0a2a !important; }
        .text-center { text-align: center; }
        .mt-2 { margin-top: 2rem; }
        .mb-1 { margin-bottom: 0.5rem; }
        .lineup-title { color: gold; font-size: 0.9rem; margin-top: 0.5rem; }
        .mvp-box { background: #0a0a2a; padding: 1rem; border-radius: 8px; border: 2px solid gold; margin: 1rem 0; text-align: center; }
        .mvp-box .mvp-name { color: gold; font-size: 1.5rem; font-weight: bold; }
        .mvp-box .mvp-info { color: #aaa; }
        .half-box { background: #0a0a2a; padding: 2rem; border-radius: 10px; border: 2px solid gold; margin: 1rem 0; text-align: center; }
        .half-box .big-text { font-size: 2rem; color: gold; }
        .sub-btn { background: #3498db; color: white; border: none; padding: 0.3rem 0.8rem; border-radius: 3px; cursor: pointer; font-size: 0.8rem; }
        .sub-btn:hover { background: #2980b9; }
    </style>
    <script>
        function continueMatch() {
            document.getElementById('continueForm').submit();
        }
        function doSubstitution() {
            document.getElementById('subForm').submit();
        }
    </script>
</head>
<body>
    <nav>
        <a href="/" class="logo">⚽ Fudbalska Taktika Pro</a>
        <div>
            <a href="/" class="ACTIVE_HOME">Početna</a>
            <a href="/match" class="ACTIVE_MATCH">Meč</a>
            <a href="/players" class="ACTIVE_PLAYERS">Igrači</a>
        </div>
    </nav>
    <div class="container">
        CONTENT_PLACEHOLDER
    </div>
    <footer style="text-align:center; padding:2rem; color:#555; border-top:1px solid #1a1a3a; margin-top:2rem;">
        ⚽ Fudbalska Taktika Pro &copy; 2024
    </footer>
</body>
</html>
'''

def render_page(content, active=""):
    html = BASE_HTML
    html = html.replace("CONTENT_PLACEHOLDER", content)
    html = html.replace("ACTIVE_HOME", "active-link" if active == "home" else "")
    html = html.replace("ACTIVE_MATCH", "active-link" if active == "match" else "")
    html = html.replace("ACTIVE_PLAYERS", "active-link" if active == "players" else "")
    return html

# ============= RUTE =============

@app.get("/", response_class=HTMLResponse)
async def home():
    content = '''
    <div style="text-align:center; padding:3rem 0;">
        <h1 style="font-size:3rem; color:gold;">⚽ FUDBALSKA TAKTIKA PRO</h1>
        <p style="font-size:1.2rem; color:#aaa; margin-bottom:2rem;">150+ igrača | Potpuna simulacija</p>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; max-width:500px; margin:0 auto;">
            <div style="background:#1a1a3a; padding:2rem; border-radius:10px; border:1px solid #333; text-align:center;">
                <h3 style="color:gold;">🎮 Meč</h3>
                <p style="color:#888;">Simuliraj utakmicu</p>
                <a href="/match" class="btn" style="margin-top:1rem;">Započni</a>
            </div>
            <div style="background:#1a1a3a; padding:2rem; border-radius:10px; border:1px solid #333; text-align:center;">
                <h3 style="color:gold;">📋 Igrači</h3>
                <p style="color:#888;">Pregled svih igrača</p>
                <a href="/players" class="btn" style="margin-top:1rem;">Pogledaj</a>
            </div>
        </div>
    </div>
    '''
    return render_page(content, "home")

@app.get("/players", response_class=HTMLResponse)
async def players():
    player_cards = ""
    for igrac in SVI_IGRACI:
        player_cards += f'''
        <div style="background:#1a1a3a; padding:0.8rem; border-radius:8px; border:1px solid #333;">
            <div style="color:gold; font-weight:bold;">{igrac["ime"]}</div>
            <div style="color:#aaa; font-size:0.9rem;">{igrac["pozicija"]} | {igrac["drzava"]}</div>
            <div style="color:#aaa; font-size:0.9rem;">{igrac["klub"]} | Rating: {igrac["rating"]}</div>
        </div>
        '''
    content = f'''
    <h2 style="color:gold; margin-bottom:1.5rem;">📋 Svi igrači ({len(SVI_IGRACI)})</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(250px,1fr)); gap:1rem;">
        {player_cards}
    </div>
    '''
    return render_page(content, "players")

@app.get("/match", response_class=HTMLResponse)
async def match_page():
    gk_players = [p for p in SVI_IGRACI if p["pozicija"] == "GK"]
    cb_players = [p for p in SVI_IGRACI if p["pozicija"] in ["CB", "LB", "RB"]]
    cm_players = [p for p in SVI_IGRACI if p["pozicija"] in ["CM", "CDM", "CAM"]]
    fw_players = [p for p in SVI_IGRACI if p["pozicija"] in ["LW", "RW", "ST"]]
    
    content = f'''
    <div class="match-setup">
        <h2>⚽ Postavi meč</h2>
        <div style="color:#888; text-align:center; margin-bottom:1rem; font-size:0.9rem;">
            Odaberi 11 igrača po timu (1 GK, 4 ODB, 4 VEZ, 2 NAP)
        </div>
        <form action="/match/simulate" method="post">
            <div class="team-select">
                <div class="team-box">
                    <h3 style="color:#e74c3c;">🔴 Tim 1</h3>
                    <label>Tim:</label>
                    <select name="team1_name">
                        {''.join([f'<option value="{t}">{t}</option>' for t in TIMOVI])}
                    </select>
                    <label>Formacija:</label>
                    <select name="team1_formation">
                        {''.join([f'<option value="{f}">{f}</option>' for f in ["4-3-3", "4-4-2", "3-5-2"]])}
                    </select>
                    <div class="lineup-title">🎯 Golmani (GK) - odaberi 1</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team1_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in gk_players[:8]])}
                    </div>
                    <div class="lineup-title">🛡️ Odbrana (CB/LB/RB) - odaberi 4</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team1_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in cb_players[:12]])}
                    </div>
                    <div class="lineup-title">⚡ Vezni (CM/CDM/CAM) - odaberi 4</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team1_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in cm_players[:12]])}
                    </div>
                    <div class="lineup-title">🎯 Napadači (LW/RW/ST) - odaberi 2</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team1_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in fw_players[:10]])}
                    </div>
                </div>
                <div class="team-box">
                    <h3 style="color:#3498db;">🔵 Tim 2</h3>
                    <label>Tim:</label>
                    <select name="team2_name">
                        {''.join([f'<option value="{t}">{t}</option>' for t in TIMOVI])}
                    </select>
                    <label>Formacija:</label>
                    <select name="team2_formation">
                        {''.join([f'<option value="{f}">{f}</option>' for f in ["4-3-3", "4-4-2", "3-5-2"]])}
                    </select>
                    <div class="lineup-title">🎯 Golmani (GK) - odaberi 1</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team2_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in gk_players[8:15]])}
                    </div>
                    <div class="lineup-title">🛡️ Odbrana (CB/LB/RB) - odaberi 4</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team2_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in cb_players[12:24]])}
                    </div>
                    <div class="lineup-title">⚡ Vezni (CM/CDM/CAM) - odaberi 4</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team2_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in cm_players[12:24]])}
                    </div>
                    <div class="lineup-title">🎯 Napadači (LW/RW/ST) - odaberi 2</div>
                    <div class="player-list">
                        {''.join([f'<div class="player-item"><input type="checkbox" name="team2_players" value="{p["ime"]}"> {p["ime"]} <span class="pos">({p["pozicija"]})</span></div>' for p in fw_players[10:20]])}
                    </div>
                </div>
            </div>
            <div class="text-center mt-2">
                <button type="submit" class="btn btn-danger" style="font-size:1.2rem; padding:1rem 3rem;">▶ ZAPOČNI MEČ</button>
            </div>
        </form>
    </div>
    '''
    return render_page(content, "match")

# ============= SIMULACIJA =============
simulation_data = {}

@app.post("/match/simulate", response_class=HTMLResponse)
async def simulate_match(
    team1_name: str = Form(...),
    team1_formation: str = Form(...),
    team1_players: list = Form(...),
    team2_name: str = Form(...),
    team2_formation: str = Form(...),
    team2_players: list = Form(...)
):
    # Inicijalizacija podataka
    data = {
        "team1": {"name": team1_name, "formation": team1_formation, "players": team1_players, "goals": 0, "shots": 0, "shots_on_target": 0},
        "team2": {"name": team2_name, "formation": team2_formation, "players": team2_players, "goals": 0, "shots": 0, "shots_on_target": 0},
        "posjed1": 50, "posjed2": 50,
        "log": [],
        "kartoni": {"zuti": [], "crveni": []},
        "golovi": {},
        "minut": 0,
        "half": 1,
        "finished": False,
        "mvp": None,
        "paused": False,
        "klupa1": team1_players[11:] if len(team1_players) > 11 else [],
        "klupa2": team2_players[11:] if len(team2_players) > 11 else [],
        "igraci1": team1_players[:11],
        "igraci2": team2_players[:11],
    }
    
    # Simulacija 90 minuta
    for minut in range(1, 91):
        data["minut"] = minut
        
        # Šut
        if random.random() < 0.30:
            if random.random() < 0.5:
                data["team1"]["shots"] += 1
                strijelac = random.choice(data["igraci1"]) if data["igraci1"] else "Nepoznat"
                if random.random() < 0.35:
                    data["team1"]["shots_on_target"] += 1
                    if random.random() < 0.30:
                        data["team1"]["goals"] += 1
                        if strijelac not in data["golovi"]:
                            data["golovi"][strijelac] = 0
                        data["golovi"][strijelac] += 1
                        data["log"].append(f'⚽ <span class="goal">GOL!</span> {strijelac} ({minut}") za {team1_name}')
                    else:
                        data["log"].append(f'🧤 <span style="color:#3498db;">OBRANA!</span> Golman brani šut {strijelac} ({minut}")')
                else:
                    data["log"].append(f'❌ {strijelac} šutira pored gola ({minut}")')
            else:
                data["team2"]["shots"] += 1
                strijelac = random.choice(data["igraci2"]) if data["igraci2"] else "Nepoznat"
                if random.random() < 0.35:
                    data["team2"]["shots_on_target"] += 1
                    if random.random() < 0.30:
                        data["team2"]["goals"] += 1
                        if strijelac not in data["golovi"]:
                            data["golovi"][strijelac] = 0
                        data["golovi"][strijelac] += 1
                        data["log"].append(f'⚽ <span class="goal">GOL!</span> {strijelac} ({minut}") za {team2_name}')
                    else:
                        data["log"].append(f'🧤 <span style="color:#3498db;">OBRANA!</span> Golman brani šut {strijelac} ({minut}")')
                else:
                    data["log"].append(f'❌ {strijelac} šutira pored gola ({minut}")')
        
        # Faul
        if random.random() < 0.12:
            if random.random() < 0.5:
                igrac = random.choice(data["igraci1"]) if data["igraci1"] else "Nepoznat"
                if random.random() < 0.30:
                    data["kartoni"]["zuti"].append(f'{igrac} ({minut}")')
                    data["log"].append(f'🟨 <span class="yellow">ŽUTI KARTON</span> za {igrac} ({minut}")')
                elif random.random() < 0.08:
                    data["kartoni"]["crveni"].append(f'{igrac} ({minut}")')
                    data["log"].append(f'🟥 <span class="red">CRVENI KARTON</span> za {igrac} ({minut}")')
            else:
                igrac = random.choice(data["igraci2"]) if data["igraci2"] else "Nepoznat"
                if random.random() < 0.30:
                    data["kartoni"]["zuti"].append(f'{igrac} ({minut}")')
                    data["log"].append(f'🟨 <span class="yellow">ŽUTI KARTON</span> za {igrac} ({minut}")')
                elif random.random() < 0.08:
                    data["kartoni"]["crveni"].append(f'{igrac} ({minut}")')
                    data["log"].append(f'🟥 <span class="red">CRVENI KARTON</span> za {igrac} ({minut}")')
        
        if minut % 5 == 0:
            data["posjed1"] = random.randint(40, 60)
            data["posjed2"] = 100 - data["posjed1"]
            data["log"].append(f'⏱️ {minut}" - Posjed: {team1_name} {data["posjed1"]}% : {data["posjed2"]}% {team2_name}')
        
        # Poluvrijeme
        if minut == 45:
            data["paused"] = True
            data["half"] = 1
            break
    
    # MVP
    if data["golovi"]:
        mvp = max(data["golovi"], key=data["golovi"].get)
        data["mvp"] = mvp
    
    data["finished"] = True
    
    return prikazi_rezultat(data)

def prikazi_rezultat(data):
    team1_name = data["team1"]["name"]
    team2_name = data["team2"]["name"]
    golovi1 = data["team1"]["goals"]
    golovi2 = data["team2"]["goals"]
    
    if golovi1 > golovi2:
        rezultat = f"🏆 POBJEDNIK: {team1_name} {golovi1}:{golovi2} 🏆"
    elif golovi2 > golovi1:
        rezultat = f"🏆 POBJEDNIK: {team2_name} {golovi2}:{golovi1} 🏆"
    else:
        rezultat = f"🤝 NERJEŠENO {golovi1}:{golovi2} 🤝"
    
    # MVP
    mvp_html = ""
    if data["mvp"]:
        mvp_html = f'''
        <div class="mvp-box">
            <div style="color:#888;">🌟 MVP UTAKMICE 🌟</div>
            <div class="mvp-name">{data["mvp"]}</div>
            <div class="mvp-info">Golovi: {data["golovi"].get(data["mvp"], 0)}</div>
        </div>
        '''
    else:
        mvp_html = '<div class="mvp-box"><div style="color:#888;">Nema golova, nema MVP</div></div>'
    
    log_html = ""
    for entry in data["log"][-30:]:
        log_html += f'<div class="log-entry">{entry}</div>'
    
    content = f'''
    <div class="match-info">
        <div class="score">{team1_name} {golovi1} : {golovi2} {team2_name}</div>
        <div class="time">⏱️ 90:00 - KRAJ UTAKMICE</div>
        <div style="text-align:center; font-size:1.2rem; color:gold; margin:0.5rem 0;">{rezultat}</div>
        
        {mvp_html}
        
        <div class="stats">
            <div class="stat-box">
                <div class="value">{data["team1"]["shots"]}</div>
                <div class="label">Šutevi {team1_name}</div>
            </div>
            <div class="stat-box">
                <div class="value">{data["posjed1"]}%</div>
                <div class="label">Posjed lopte</div>
            </div>
            <div class="stat-box">
                <div class="value">{data["team2"]["shots"]}</div>
                <div class="label">Šutevi {team2_name}</div>
            </div>
        </div>
        
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; margin-top:1rem;">
            <div style="background:#0a0a2a; padding:1rem; border-radius:8px; text-align:center;">
                <div style="color:gold; font-size:1.2rem;">{data["team1"]["shots_on_target"]}</div>
                <div style="color:#888; font-size:0.8rem;">Šutevi na gol {team1_name}</div>
            </div>
            <div style="background:#0a0a2a; padding:1rem; border-radius:8px;">
                <h4 style="color:#e74c3c;">🟨 Žuti kartoni</h4>
                {''.join([f'<div style="color:#f1c40f;">{k}</div>' for k in data["kartoni"]["zuti"]]) if data["kartoni"]["zuti"] else '<div style="color:#888;">Nema</div>'}
            </div>
            <div style="background:#0a0a2a; padding:1rem; border-radius:8px;">
                <h4 style="color:#e74c3c;">🟥 Crveni kartoni</h4>
                {''.join([f'<div style="color:#e74c3c;">{k}</div>' for k in data["kartoni"]["crveni"]]) if data["kartoni"]["crveni"] else '<div style="color:#888;">Nema</div>'}
            </div>
        </div>
        
        <div class="match-log">
            <h4 style="color:gold; margin-bottom:0.5rem;">📋 Događaji:</h4>
            {log_html}
        </div>
        
        <div class="text-center mt-2">
            <a href="/match" class="btn">🔄 Nova utakmica</a>
            <a href="/" class="btn" style="margin-left:1rem;">🏠 Početna</a>
        </div>
    </div>
    '''
    return render_page(content, "match")


