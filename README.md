# KVM Switch (Work in progress)
> Multi monitor helper for kvm-switches. 

## Intended use-case
This software is targeted people who has a physical multi-way KVM switch
(for multiple computers, one monitor) but has multiple monitors that they 
would like to also automatically switch.

## How does it work?
We use the fact that monitors look for other active inputs when an input 
(from a computer) is switched off.

To switch the signal off, we can either hibernate the computer, or use another
program like `xrandr --output ${MONITOR_TO_BE_SWITCHED_OFF} --off`.
And the opposite to turn on the monitor.

To figure out when to do this, we scan the DBUS for related signals:
* Keyboard disconnect.
* Keyboard connect.
