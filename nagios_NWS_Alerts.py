#!/usr/bin/env python3

'''
    Project home: git.zebpalmer.com/nws-alerts
    Original Author: Zeb Palmer   (www.zebpalmer.com)
    For more info, please see the README.rst

    This program is free software you can redistribute it and
    or modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, either version
    3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''


from sys import exit, argv
from nws_alerts import nws_alerts



def check_alerts(alerts):
    if len(alerts) == 0:
        print("No active alerts")
        exit(0)
    elif len(alerts) == 1:
        print(cap.alerts.alerts_type())
    else:
        #print "{0} Alerts".format(len(alerts))
        types = []
        for alert in alerts:
            alert_type = cap.alert_type(alert)
            if alert_type not in types:
                types.append(alert_type)
        for alert_type in types:
            print(alert_type + ',', end=' ')
    exit(1)


def loadalerts(geocodes):
    geocodes = geocodes.split(',')
    same = nws_alerts.SameCodes()
    scope = same.getfeedscope(geocodes)
    cap = nws_alerts.CapAlerts(state=scope, same=same)
    alerts = cap.alerts_by_samecodes(geocodes)    
    check_alerts(alerts)



if __name__ == "__main__":
    if len(argv) != 2:
        print ('''Please specify the SAME code(s) for the area(s) you wish to check
\tSee http://www.nws.noaa.gov/nwr/indexnw.htm for help finding your SAME area.
\tSeparate multiple same codes by commas with no spaces''') 
        exit(3)
    else:
        loadalerts(argv[1])





