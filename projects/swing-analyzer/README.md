# SwingOS Prototype

A real time webcam tool that tracks one thing: the vertical position of your nose landmark. You press `S` to lock in your current head level as an anchor, and from then on it compares where your head is against where it started.

It draws a green line at the anchor and a red line at your current position. If your head drops more than about 20 pixels below the anchor it says WATCH YOUR HEAD, if it rises the same amount it says STAY DOWN, and inside that window it says SOLID. Press `Q` to quit. The feedback is instant, which is the whole point.

It's a prototype, not a swing analyzer — there's no swing detection, no phase segmentation, and no recording. It watches one landmark against one anchor line, live.

I built it because I wanted to know if I could train the body to feel what correct mechanics looked like without needing a coach in the room. A single tracked landmark turned out to be enough to be useful.

Built with Python, OpenCV, and MediaPipe (`bbswing.py`). Needs a webcam.
