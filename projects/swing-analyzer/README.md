# SwingOS Prototype

This is a real time computer vision tool that uses your webcam to track your head position during a baseball swing. You press S to lock in your head level as an anchor point and then the system watches whether your head stays level or drops through the swing.

It draws a green line at your anchor and a red line at your current position. If your head drops it tells you WATCH YOUR HEAD and if you come up it says STAY DOWN. The feedback is instant which is the whole point.

I built this because I wanted to know if I could train the body to feel what correct mechanics looked like without needing a coach in the room. Computer vision made that possible.

Built with Python, OpenCV, and MediaPipe.
