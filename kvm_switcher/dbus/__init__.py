import os

import pyudev


class Watcher:
    def __init__(self, extra_monitor: str, verbose: bool = False):
        self.extra_monitor = extra_monitor
        self.verbose = verbose
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='usb')
        self.observer = pyudev.MonitorObserver(monitor=monitor, event_handler=self._watch)

    def run(self):
        self.observer.start()

    def _watch(self, action, device):
        if action == "remove":
            # disconnected device.
            self.print("Switch toggled off, turn off the monitor.")
            os.system(f"xrandr --output {self.extra_monitor} --off")
        elif action == "add":
            # connected device.
            self.print("Switch toggled on, turn on the monitor.")
            os.system(f"xrandr --output {self.extra_monitor} --auto")
            os.system(f"xrandr --output {self.extra_monitor} --left-of VGA-1")  # TODO(make dynamic)
        # unknown action.
        self.print(f"{device.device_number} ({device.device_type}): {action}.")

    def stop(self):
        self.observer.send_stop()

    def print(self, text: str):
        if self.verbose:
            print(text)
