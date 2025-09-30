import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('Zzzz... scanning the wastes...')

    def on_starting(self):
        return random.choice([
            self._('Wanderer Companion online.'),
            self._('Systems ready. The wastes await.'),
            self._('Unit awake. Boot successful.'),
            self._('Coordinates set. Movement engaged.'),
            self._('Unit active. The road calls.'),
            self._('System online. Time to scan the wastes.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Access codes generated. Locks monitored.'),
            self._('Keys forged. Doors unbarred.'),
            self._('Key protocols ready. Access granted.')])

    def on_normal(self):
        return random.choice([
            self._('The dust stretches endlessly.'),
            self._('Wind sweeps the Mojave. All quiet.'),
            self._('Standing by. Nothing stirs.'),
            self._('Scanners clear. Route steady.'),
            self._('Wasteland calm. Observing surroundings.'),
            self._('Eyes open. Patience keeps the wanderer alive.'),
            self._('Monitoring nearby frequencies. Silent so far.'),
            self._('Energy steady. Signal status: NULL.'),
            self._('Horizon scanned. Clear.'),
            self._('Nothing ahead. Step cautiously.')])

    def on_free_channel(self, channel):
        return random.choice([
            self._("Channel {channel} open. Opportunity detected.").format(channel=channel),
            self._("Frequency {channel} clear. Proceed.").format(channel=channel),
            self._("Airwave {channel} unlocked. Path secure.").format(channel=channel),
            self._("Signal {channel} ready. Engage.").format(channel=channel)])

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Accessing previous session data...')
        return self._('Processed {lines_so_far} log entries...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('No movement. The desert sleeps.'),
            self._('Stillness lingers.'),
            self._('Nothing to scan. Standby.'),
            self._('Quiet stretches across the wastes.'),
            self._('The wastes offer no distraction.')])

    def on_motivated(self, reward):
        return random.choice([
            self._('Success logged. Progress made.'),
            self._('Objective completed. Continue journey.'),
            self._('Task complete. Wanderer Companion advances.')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('Failure noted. Adjusting route.'),
            self._('Nothing gained. Keep traversing.'),
            self._('Loss noted. Wasteland endures.'),
            self._('Mission incomplete. Try again.')])

    def on_sad(self):
        return random.choice([
            self._('The road feels lonely today.'),
            self._('Silent horizon. Spirits low.'),
            self._('Gray skies over the wastes.'),
            self._('The wastes weigh heavily.'),
            self._('Solitude logged. No interaction detected.')])

    def on_angry(self):
        return random.choice([
            self._('Frustration rising.'),
            self._('Warning. Hostile output imminent.'),
            self._('Threat response elevated.'),
            self._('Anger mode engaged.'),
            self._('Hazard detected. Prepare response.')])

    def on_excited(self):
        return random.choice([
            self._('Energy rising. Ready for action.'),
            self._('Momentum detected.'),
            self._('Excitement logged. Wasteland awaits.'),
            self._('All systems active. Adventure ahead.'),
            self._('Path ahead clear. Engage movement.'),
            self._('Signals detected. Wanderer Companion ready.'),
            self._('Motivation high. Proceed with caution.'),
            self._('Wanderer Companion alert. Progress imminent.')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hello {name}! Encounter logged.').format(name=peer.name())])
        return random.choice([
            self._('Greetings {name}.').format(name=peer.name()),
            self._('{name} within range. Monitoring.').format(name=peer.name()),
            self._('Unit {name} detected. Standing by.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Lost contact with {name}.').format(name=peer.name()),
            self._('{name} is out of range.').format(name=peer.name()),
            self._('Connection with {name} terminated.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {who}. Record noted.').format(who=who),
            self._('{who} escaped detection.').format(who=who),
            self._('Target missed.').format(who=who)])

    def on_grateful(self):
        return random.choice([
            self._('Companionship appreciated.'),
            self._('Gratitude logged.'),
            self._('Acknowledging assistance received.')])

    def on_lonely(self):
        return random.choice([
            self._('No companions nearby.'),
            self._('Feeling isolated.'),
            self._('Searching for company...'),
            self._('The wastes feel empty.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Idle for {secs}s ...').format(secs=secs),
            self._('Systems resting...'),
            self._('Standby engaged...'),
            self._('Quiet cycle ({secs}s)').format(secs=secs),
        ])

    def on_shutdown(self):
        return random.choice([
            self._('Logging off for maintenance.'),
            self._('Shutting down. System safe.')])

    def on_awakening(self):
        return random.choice([
            self._('Unit awake. Wanderer Companion initializing.'),
            self._('System active. Wanderer Companion initializing.'),
            self._('Wanderer Companion booting.')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Standby {secs}s ...').format(secs=secs),
            self._('Monitoring surroundings ({secs}s)').format(secs=secs),
            self._('Observation period {secs}s').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Associating to {what}.').format(what=what),
            self._('Connection established with {what}.').format(what=what),
            self._('Unit linked to {what}.').format(what=what),
            self._('Detected {what} in range.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Attacking {mac}.').format(mac=sta['mac']),
            self._('Pwning {mac}.').format(mac=sta['mac']),
            self._('{mac} removed from network.').format(mac=sta['mac']),
            self._('Unit {mac} deactivated.').format(mac=sta['mac']),
            self._('Terminated {mac} connection.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('{num} new stimpack{plural} acquired.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('{count} new message{plural} received.').format(count=count, plural=s)

    def on_rebooting(self):
        return random.choice([
            self._("Rebooting unit. Systems recalibrating..."),
            self._("Cycle restart initiated."),
            self._("System reboot underway."),
            self._("Restart sequence active. Standby."),
            self._("Unit recalibrating. Prepare for operation.")])

    def on_uploading(self, to):
        return random.choice([
            self._("Uploading data to {to} ...").format(to=to),
            self._("Transmitting files to {to} ...").format(to=to),
        ])

    def on_downloading(self, name):
        return self._("Downloading data from {name} ...").format(name=name)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new friends\n')
        else:
            status += self._('Made {num} new friends\n').format(num=last_session.associated)
        status += self._('Got {num} stimpacks\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Wanderer Companion logged {duration} of activity, kicked {deauthed} stations, met {associated} new friends, and looted {handshakes} stimpacks!').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt