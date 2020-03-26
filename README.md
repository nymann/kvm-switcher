# KVM Switch (Work in progress)
> Multi monitor helper for kvm-switches. 

## Intended use-case
This software is targeted people who has a physical multi-way KVM switch
(for multiple computers, one monitor) but has multiple monitors that they 
would like to also automatically switch upon toggling their physical 
kvm-switch.

### Example
![Picture of kvm-switch][kvm-switch]

You have the switch as seen above, you hook it up to your two computers.
And everything is nice and dandy. But now you would like a 
second monitor, so you take a look at multi-monitor KVM switches and
looking at the price you almost fall down your chair!

Don't fear, my software is here.

## How does it work?
We use the fact that monitors look for other active inputs when an input 
(from a computer) is switched off.

To switch the signal off, we can either hibernate the computer, or use 
another program like `xrandr --output ${MONITOR_TO_BE_SWITCHED_OFF} --off`.
And the opposite to turn on the monitor.

To figure out when to do this, we scan the DBUS for related signals:
* Keyboard disconnect.
* Keyboard connect.

## Install
Do the following on both of your computers that you would like to switch between:
`git clone https://github.com/nymann/kvm-switch.git`

`cd kvm-switch && pip install .`

`kvm_switch -m DP-3`

For additional help:

> kvm_switch --help
```
usage: kvm_switch [-h] [-v [VERBOSE]] [-m EXTRA_MONITOR]

optional arguments:
  -h, --help            show this help message and exit
  -v [VERBOSE], --verbose [VERBOSE]
                        Enables verbose mode
  -m EXTRA_MONITOR, --extra-monitor EXTRA_MONITOR
                        xrandr compatible name of the extra monitor you would like to auto-switch.
```

<!-- References -->
[kvm-switch]: docs/images/kvm-switch.png