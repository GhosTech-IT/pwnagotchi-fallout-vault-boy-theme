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
        return self._('Scanning the Mojave, always vigilant.')

    def on_starting(self):
        return random.choice([
            self._('Wanderer Companion systems engaged.'),
            self._('Ready for adventure, wasteland style.'),
            self._('Vault-Tec device, operational.'),
            self._('Heading out, follow the compass.'),
            self._('The open road beckons, let\'s explore.'),
            self._('Time to survey the territory.')])

    def on_keys_generation(self):
        return random.choice([
            self._('Access codes acquired, new paths unlocked.'),
            self._('Security breached, proceeding with caution.'),
            self._('Key protocols established, access granted.')])

    def on_normal(self):
        return random.choice([
            self._('The desert stretches on endlessly.'),
            self._('Mojave winds whisper peacefully.'),
            self._('Standing by, no immediate threats.'),
            self._('Scanners all clear.'),
            self._('Wasteland is calm, observing.'),
            self._('Stay alert, patience is key to survival.'),
            self._('Monitoring frequencies.'),
            self._('Energy stable, no signals detected.'),
            self._('Horizon clear, proceed with caution.'),
            self._('Nothing directly ahead.')])

    def on_free_channel(self, channel):
        return random.choice([
            self._("Channel {channel} is open, a new path emerges.").format(channel=channel),
            self._("Frequency {channel} clear, advance with purpose.").format(channel=channel),
            self._("Airwave {channel} unlocked, the path is secure.").format(channel=channel),
            self._("Signal {channel} ready, prepare to engage.").format(channel=channel)])

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Retrieving past mission logs.')
        return self._('Processed {lines_so_far} entries from the log.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('War... War never changes.'),
            self._('A quiet stillness settles.'),
            self._('Standing by.'),
            self._('Silence stretches across the wastes.'),
            self._('The wastes provide no diversions.')])

    def on_motivated(self, reward):
        return random.choice([
            self._('You deserve a Quantum!'),
            self._('Enjoy a Quantum!'),
            self._('You deserve a Nuka-Cola!')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('Failure recorded, recalculating route.'),
            self._('No gains made, continue traversing.'),
            self._('Loss sustained, the wasteland endures.'),
            self._('Mission incomplete, attempt again.')])

    def on_sad(self):
        return random.choice([
            self._('The journey feels solitary today.'),
            self._('Silent horizon, morale is low.'),
            self._('Overcast skies shroud the wastes.'),
            self._('The burden of the wastes is heavy.'),
            self._('Solitude noted, no interactions detected.')])

    def on_angry(self):
        return random.choice([
            self._('Frustration levels are rising.'),
            self._('Warning: hostile output imminent.'),
            self._('Threat response protocol initiated.'),
            self._('Anger mode engaged.'),
            self._('Hazard detected, preparing response.')])

    def on_excited(self):
        return random.choice([
            self._('Energy levels surging, ready for action.'),
            self._('Momentum is building.'),
            self._('Excitement registered.'),
            self._('All systems active.'),
            self._('Path is clear, onward!'),
            self._('Signals detected, companion ready.'),
            self._('Motivation: HIGH'),
            self._('Companion alert: progress is imminent.')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('A new face, {name}, has appeared.').format(name=peer.name())])
        return random.choice([
            self._('Greetings, {name}.').format(name=peer.name()),
            self._('{name} is within range.').format(name=peer.name()),
            self._('Unit {name} detected.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Lost contact with {name}, they\'re.').format(name=peer.name()),
            self._('{name} has moved out of range.').format(name=peer.name()),
            self._('Connection with {name} has been terminated.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {who}.').format(who=who),
            self._('{who} evaded detection.').format(who=who),
            self._('Target missed, better luck next time.').format(who=who)])

    def on_grateful(self):
        return random.choice([
            self._('The bond of companionship is valued.'),
            self._('Gratitude has been recorded.'),
            self._('Assistance received, acknowledgment logged.')])

    def on_lonely(self):
        return random.choice([
            self._('No allies are nearby.'),
            self._('A sense of isolation lingers.'),
            self._('Searching for friendly faces.'),
            self._('The wastes feel barren.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Idling for {secs} seconds, conserving power.').format(secs=secs),
            self._('Systems are in a resting state.'),
            self._('Standby mode engaged.'),
            self._('Quiet cycle for {secs} seconds.').format(secs=secs),
        ])

    def on_shutdown(self):
        return random.choice([
            self._('Logging off for essential maintenance.'),
            self._('Shutting down, system secure.')])

    def on_awakening(self):
        return random.choice([
            self._('Unit awake, Companion initializing.'),
            self._('System active, Companion initializing.'),
            self._('Wanderer Companion booting up.')])

    def on_waiting(self, secs):
        return random.choice([
            self._('On standby for {secs} seconds.').format(secs=secs),
            self._('Monitoring surroundings for {secs} seconds.').format(secs=secs),
            self._('Observation period of {secs} seconds.').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Linking to {what}.').format(what=what),
            self._('Connection established with {what}.').format(what=what),
            self._('Unit linked to {what}.').format(what=what),
            self._('Detected {what}.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Engaging {mac}.').format(mac=sta['mac']),
            self._('Overpowering {mac}.').format(mac=sta['mac']),
            self._('{mac} has been removed.').format(mac=sta['mac']),
            self._('Unit {mac} deactivated.').format(mac=sta['mac']),
            self._('Terminated {mac}.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('{num} new stimpack{plural} located, inventory updated.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('{count} new message{plural} received, check Pip-Boy.').format(count=count, plural=s)

    def on_rebooting(self):
        return random.choice([
            self._("Rebooting unit, recalibrating systems."),
            self._("Cycle restart has been initiated."),
            self._("System reboot is now underway."),
            self._("Restart sequence active, please standby."),
            self._("Unit recalibrating, preparing for operation.")])

    def on_uploading(self, to):
        return random.choice([
            self._("Uploading data to {to}, transmission in progress.").format(to=to),
            self._("Transmitting files to {to}.").format(to=to),
        ])

    def on_downloading(self, name):
        return self._("Downloading data from {name}.").format(name=name)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations.\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made 999 new allies.\n')
        else:
            status += self._('Made {num} new allies.\n').format(num=last_session.associated)
        status += self._('Got {num} stimpacks.\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Encountered 1 fellow traveler.')
        elif last_session.peers > 0:
            status += self._('Encountered {num} fellow travelers.').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Wanderer Companion logged {duration} of activity, disrupted {deauthed} stations, encountered {associated} new allies, and secured {handshakes} stimpacks!').format(
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
