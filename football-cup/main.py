import json
import math as mt
import random as rd


def load_clubs() -> list:
    """
    :return: list of club names
    """

    with open("teams.txt") as f:
        clubs = [t.strip() for t in f.readlines()]
    clubs = clubs[:2 ** mt.floor(mt.log2(len(clubs)))]

    return clubs


def arrange(clubs) -> list:
    """
    :param clubs: list of club name strings
    :return: fixtures list
    """

    # fixtures - save each as len 2 tuple
    fxs = []

    # fixtures until clubs run out
    while len(clubs) != 0:
        # select rand teams
        home = rd.choice(clubs)
        clubs.remove(home)
        away = rd.choice(clubs)
        clubs.remove(away)

        fxs.append({
            "hTeam": home,
            "hScore": 0,
            "aTeam": away,
            "aScore": 0,
        })

    return fxs


def play(fx) -> dict:
    """
    :param fx: dictionary fixture object
    :return: fixture dictionary object
    """

    fx["hScore"] = rd.randint(0, 10)
    fx["aScore"] = rd.choice([i for i in range(10) if i != fx["hScore"]])

    return fx


def cup_sim(clubs, all_results=None) -> list:
    """
    Simulates a cup season by running fixtures and returning a JSON object of the results

    :param clubs:
    :param all_results:
    :return:
    """

    if all_results is None:
        all_results = []
    results = []
    fxs = arrange(clubs)  # fixtures

    # choose round name
    round_n = int(mt.log2(len(fxs) * 2))
    if round_n == 1:
        round_name = "FINALS"
    elif round_n == 2:
        round_name = "SEMI-FINALS"
    elif round_n == 3:
        round_name = "QUARTER-FINALS"
    else:
        round_name = f"ROUND {round_n}"

    print(f"""
####################################################################################################
    {round_name}
####################################################################################################
""")

    # loop through fixtures and filter winners
    winners = []
    for fx in fxs:
        fx = play(fx)
        results.append(fx)

        # display match
        print("%25s vs %25s | %25s won    %2d - %2d" % (
            fx["hTeam"], fx["aTeam"],
            fx["hTeam"] if fx["hScore"] > fx["aScore"] else fx["aTeam"],
            fx["hScore"] if fx["hScore"] > fx["aScore"] else fx["aScore"],
            fx["hScore"] if fx["hScore"] < fx["aScore"] else fx["aScore"]))

        # add to winners
        winners.append(fx["hTeam"] if fx["hScore"] > fx["aScore"] else fx["aTeam"])

    all_results.append(results)
    if len(winners) == 1:
        return all_results
    return cup_sim(winners, all_results)


def main():
    # repeat sim 100 times and display frequency stats
    freq = {}

    all_sim_results = []
    for _ in range(1000):
        all_sim_results.append(cup_sim(load_clubs()))
        final = all_sim_results[-1][-1][0]
        wnr = final["hTeam"] if final["hScore"] > final["aScore"] else final["aTeam"]

        # add to frequency table
        if wnr in freq.keys():
            # entry already exists
            freq[wnr] += 1
        else:
            # add new entry
            freq[wnr] = 1

    print("\n\n\n\n\nFREQUENCY STATISTICS")
    # display frequency statistics
    for team in freq.keys():
        print("%25s    - %4d wins" % (team, freq[team]))

    # save json
    with open("sim.json", "w") as f:
        f.write(json.dumps(all_sim_results, indent=4))


if __name__ == "__main__":
    main()
