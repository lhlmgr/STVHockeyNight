import urllib2
import json

__author__ = 'foo'


def main():
    streams = {}

    for i in xrange(1, 66):
        result = urllib2.urlopen("http://ebel.hockeydata.net/stat-attack/data/getSpieltag.aspx?json={%%22spieltag%%22:%i,%%22divid%%22:27}" % i)
        data = json.load(result)

        print "--------------"
        print "spieltag: " + str(i)

        for game in data["data"]:
            if game["broadcastId"] == 3:
                print "(s): " + game["homeTeamShort"] + " vs. " + game["awayTeamShort"]

                if game["homeTeamShort"] in streams:
                    s = int(streams[game["homeTeamShort"]])
                    s = s + 1
                    streams[game["homeTeamShort"]] = s
                else:
                    streams[game["homeTeamShort"]] = 1

                if game["awayTeamShort"] in streams:
                    s = int(streams[game["awayTeamShort"]])
                    s = s + 1
                    streams[game["awayTeamShort"]] = s
                else:
                    streams[game["awayTeamShort"]] = 1
            else:
                print game["homeTeamShort"] + " vs. " + game["awayTeamShort"]

    for team in streams:
        print team + ": " + str(streams[team])


if __name__ == "__main__":
    main()
