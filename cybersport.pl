% Facts with 1 argument (Team names)
team(astralis).
team(liquid).
team(natus_vincere).
team(faze_clan).
team(fnatic).
team(og).
team(g2_esports).
team(mousesports).
team(eg).
team(virtus_pro).
team(nip).
team(renegades).
team(flashpoint).
team(copenhagen_wolves).
team(ence).

% Facts with 2 arguments (Team and Country)
country(astralis, europe).
country(liquid, usa).
country(natus_vincere, cis).
country(faze_clan, usa).
country(fnatic, europe).
country(og, europe).
country(g2_esports, europe).
country(mousesports, europe).
country(eg, usa).
country(virtus_pro, cis).
country(nip, europe).
country(renegades, australia).
country(flashpoint, europe).
country(copenhagen_wolves, europe).
country(ence, europe).

% Facts with 2 arguments (Team and Achievements)
achievements(astralis, ['Major Champions', 'ESL Pro League Winners', 'Intel Grand Slam Winner']).
achievements(liquid, ['Intel Grand Slam Winner', 'IEM Champions', 'ESL One New York Winners']).
achievements(eg, ['Major Champions', 'ESL One New York Winners', 'IEM Champions']).
achievements(virtus_pro, ['IEM Champions', 'EPICENTER Champions', 'BLAST Pro Series Champions']).
achievements(nip, ['Major Champions', 'ESL One Cologne Winners', 'IEM Champions']).
achievements(renegades, ['IEM Champions', 'StarLadder Champions', 'Asia Minor Champions']).
achievements(flashpoint, ['DreamHack Masters Champions', 'ESL Pro League Winners', 'BLAST Pro Series Champions']).
achievements(copenhagen_wolves, ['DreamHack Masters Champions', 'IEM Champions', 'ESL Pro League Winners']).
achievements(ence, ['IEM Champions', 'StarLadder Champions', 'BLAST Pro Series Champions']).
achievements(natus_vincere, ['Major Champions', 'ESL Pro League Winners', 
                            'Intel Grand Slam Winner', 'DreamHack Masters Champions', 
                            'BLAST Pro Series Champions', 'IEM Champions']).


strong_region(Region) :-
    team(Team1),
    team(Team2),
    team(Team3),
    Team1 \= Team2,
    Team1 \= Team3,
    Team2 \= Team3,
    country(Team1, Region),
    country(Team2, Region),
    country(Team3, Region).


major_champs_not_iem_champs(Team) :-
    achievements(Team, Achievements),
    member('Major Champions', Achievements),
    not(member('IEM Champions', Achievements)).


top_tier(Team) :-
    achievements(Team, Achievements),
    member('Major Champions', Achievements),
    member('ESL Pro League Winners', Achievements).


team_from_country(Country, Team) :-
    country(Team, Country).


diverse_achievements(Team) :-
    achievements(Team, Achievements),
    member('Major Champions', Achievements),
    member('ESL Pro League Winners', Achievements),
    member('IEM Champions', Achievements),
    member('DreamHack Masters Champions', Achievements),
    member('BLAST Pro Series Champions', Achievements).








