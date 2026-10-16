# sched

## sched.Event(time, priority, sequence, action, argument, kwargs)

Event(time, priority, sequence, action, argument, kwargs)

## sched.scheduler.cancel(self, event)

Remove an event from the queue. This must be presented the ID as returned by enter().
If the event is not in the queue, this raises ValueError.

## sched.scheduler.empty(self)

Check whether the queue is empty.

## sched.scheduler.enter(self, delay, priority, action, argument=(), kwargs=<object object at 0x7fc8a19215e0>)

A variant that specifies the time as a relative time. This is actually the more commonly used interface.

## sched.scheduler.enterabs(self, time, priority, action, argument=(), kwargs=<object object at 0x7fc8a19215e0>)

Enter a new event in the queue at an absolute time. Returns an ID for the event which can be used to remove it,
if necessary.

## sched.scheduler.run(self, blocking=True)

If blocking is False executes the scheduled events due to expire soonest (if any) and then return the deadline of the next scheduled call in the scheduler.

When there is a positive delay until the first event, the
delay function is called and the event is left in the queue;
otherwise, the event is removed from the queue and executed
(its action function is called, passing it the argument).  If
the delay function returns prematurely, it is simply
restarted.

It is legal for both the delay function and the action
function to modify the queue or to raise an exception;
exceptions are not caught but the scheduler's state remains
well-defined so run() may be called again.

A questionable hack is added to allow other threads to run:
just after an event is executed, a delay of 0 is executed, to
avoid monopolizing the CPU when other threads are also
runnable.
