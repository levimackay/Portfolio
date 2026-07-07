import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from collections import deque

# =========================================================
# SETTINGS
# =========================================================

VIDEO_PATH        = "test3.mp4"
MODEL_PATH        = "pose_landmarker_full.task"
VISIBILITY_THRESHOLD = 0.50
HUD_W             = 320
HANDEDNESS        = "LEFT"   # "LEFT" or "RIGHT"
# Camera angle: "CHEST" = across-plate facing batter's chest
# affects which elbow is "back" and hip rotation sign
CAMERA_ANGLE      = "CHEST"

# =========================================================
# LANDMARK INDICES
# =========================================================
NOSE       = 0
L_EAR = 7;  R_EAR = 8
L_SHOULDER = 11; R_SHOULDER = 12
L_ELBOW    = 13; R_ELBOW    = 14
L_WRIST    = 15; R_WRIST    = 16
L_HIP      = 23; R_HIP      = 24
L_KNEE     = 25; R_KNEE     = 26
L_ANKLE    = 27; R_ANKLE    = 28
L_HEEL     = 29; R_HEEL     = 30
L_FOOT     = 31; R_FOOT     = 32

# For left-handed batter viewed from chest:
# "back" arm (closer to catcher) = RIGHT arm
# "front" arm (closer to pitcher) = LEFT arm
BACK_SHOULDER  = R_SHOULDER if HANDEDNESS == "LEFT" else L_SHOULDER
BACK_ELBOW     = R_ELBOW    if HANDEDNESS == "LEFT" else L_ELBOW
BACK_WRIST     = R_WRIST    if HANDEDNESS == "LEFT" else L_WRIST
FRONT_SHOULDER = L_SHOULDER if HANDEDNESS == "LEFT" else R_SHOULDER
FRONT_ELBOW    = L_ELBOW    if HANDEDNESS == "LEFT" else R_ELBOW
FRONT_WRIST    = L_WRIST    if HANDEDNESS == "LEFT" else R_WRIST

# Lead hip (toward pitcher) for a left-hander = right hip
LEAD_HIP   = R_HIP  if HANDEDNESS == "LEFT" else L_HIP
TRAIL_HIP  = L_HIP  if HANDEDNESS == "LEFT" else R_HIP
LEAD_KNEE  = R_KNEE if HANDEDNESS == "LEFT" else L_KNEE
TRAIL_KNEE = L_KNEE if HANDEDNESS == "LEFT" else R_KNEE
LEAD_ANKLE = R_ANKLE if HANDEDNESS == "LEFT" else L_ANKLE
TRAIL_ANKLE= L_ANKLE if HANDEDNESS == "LEFT" else R_ANKLE

# =========================================================
# COLORS (BGR)
# =========================================================
C_YELLOW = (  0, 230, 255)
C_GREEN  = ( 80, 220,  80)
C_RED    = ( 60,  60, 220)
C_ORANGE = ( 30, 165, 255)
C_WHITE  = (240, 240, 240)
C_GRAY   = (140, 140, 140)
C_DARK   = ( 18,  18,  18)
C_ACCENT = ( 10, 200, 120)

# =========================================================
# MEDIAPIPE
# =========================================================
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_poses=1,
    min_pose_detection_confidence=0.55,
    min_pose_presence_confidence=0.55,
    min_tracking_confidence=0.55,
)
detector = vision.PoseLandmarker.create_from_options(options)

# =========================================================
# VIDEO
# =========================================================
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise IOError(f"Cannot open: {VIDEO_PATH}")

fps         = cap.get(cv2.CAP_PROP_FPS) or 30.0
delay       = max(1, int(1000 / fps))
frame_index = 0

# =========================================================
# LAST-GOOD LANDMARK CACHE
# =========================================================
last_good = {}

def update_cache(raw_landmarks):
    for i, lm in enumerate(raw_landmarks):
        if lm.visibility >= VISIBILITY_THRESHOLD:
            last_good[i] = {
                "x": lm.x, "y": lm.y, "z": lm.z,
                "v": lm.visibility
            }

def get_lm(i):
    return last_good.get(i)

def is_good(i):
    return i in last_good

# =========================================================
# HISTORY
# =========================================================
HISTORY_LEN = 120
history = {
    "hip_rot":    deque([0.0] * HISTORY_LEN, maxlen=HISTORY_LEN),
    "hip_sep":    deque([0.0] * HISTORY_LEN, maxlen=HISTORY_LEN),
    "back_elbow": deque([0.0] * HISTORY_LEN, maxlen=HISTORY_LEN),
    "stride":     deque([0.0] * HISTORY_LEN, maxlen=HISTORY_LEN),
}

# =========================================================
# SWING PHASE DETECTOR
# =========================================================
PHASE_COLORS = {
    "STANCE":  C_GRAY,
    "LOAD":    C_YELLOW,
    "STRIDE":  C_ORANGE,
    "CONTACT": C_RED,
    "FOLLOW":  C_GREEN,
}

class SwingPhaseDetector:
    def __init__(self):
        self.phase       = "STANCE"
        self.phase_frame = 0
        self.frame       = 0
        self._vel_buf    = deque([0.0] * 8, maxlen=8)
        self._wy_buf     = deque([0.5] * 8, maxlen=8)

    def update(self, hip_delta, wrist_y_norm):
        self.frame += 1
        self._vel_buf.append(abs(hip_delta))
        self._wy_buf.append(wrist_y_norm)
        vel  = np.mean(self._vel_buf)
        wy   = np.mean(self._wy_buf)
        age  = self.frame - self.phase_frame
        prev = self.phase
        if   self.phase == "STANCE"  and (vel > 0.8 or wy < 0.45): self.phase = "LOAD"
        elif self.phase == "LOAD"    and vel > 2.0 and age > 4:     self.phase = "STRIDE"
        elif self.phase == "STRIDE"  and vel > 5.0:                 self.phase = "CONTACT"
        elif self.phase == "CONTACT" and vel < 3.0 and age > 3:     self.phase = "FOLLOW"
        elif self.phase == "FOLLOW"  and age > 80:
            self.phase = "STANCE"
            self._vel_buf = deque([0.0] * 8, maxlen=8)
        if self.phase != prev:
            self.phase_frame = self.frame
        return self.phase

phase_detector = SwingPhaseDetector()

# =========================================================
# HELPERS
# =========================================================
def get_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b; bc = c - b
    cos = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    return np.degrees(np.arccos(np.clip(cos, -1.0, 1.0)))

def score_metric(value, ideal_min, ideal_max):
    if ideal_min <= value <= ideal_max:    return "GOOD", C_GREEN
    lo = ideal_min * 0.75; hi = ideal_max * 1.25
    if lo <= value <= hi:                  return "OK",   C_YELLOW
    return "FIX", C_RED

def z_of(i):
    """MediaPipe Z: negative = closer to camera. Normalize to 0..1 (0=far,1=close)."""
    lm = get_lm(i)
    if lm is None: return 0.5
    # typical range roughly -0.5 to +0.5; clamp and flip
    return float(np.clip(0.5 - lm["z"], 0.0, 1.0))

# =========================================================
# 3D-AWARE SKELETON DRAWING
# =========================================================
# Connection groups: each tuple is (idx_a, idx_b, base_color, layer)
# layer 0 = draw first (back), layer 1 = middle, layer 2 = front
# For chest-facing left-handed batter:
#   back arm  = right arm  (further from camera during stance)
#   front arm = left arm
#   torso/legs drawn in middle layer

SKEL_CONNECTIONS = [
    # --- back arm (right for LHB) --- layer 0
    (BACK_SHOULDER,  BACK_ELBOW,  (100, 100, 220), 0),
    (BACK_ELBOW,     BACK_WRIST,  (100, 100, 220), 0),

    # --- spine / torso core --- layer 1
    (L_SHOULDER, R_SHOULDER,     (160, 160, 160), 1),
    (L_SHOULDER, L_HIP,          (160, 160, 160), 1),
    (R_SHOULDER, R_HIP,          (160, 160, 160), 1),
    (L_HIP,      R_HIP,          (160, 160, 160), 1),

    # --- head --- layer 1
    (NOSE, L_SHOULDER,           (200, 200, 200), 1),
    (NOSE, R_SHOULDER,           (200, 200, 200), 1),

    # --- lead leg (toward pitcher) --- layer 1
    (LEAD_HIP,   LEAD_KNEE,      (80,  200, 120), 1),
    (LEAD_KNEE,  LEAD_ANKLE,     (80,  200, 120), 1),
    (LEAD_ANKLE, LEAD_HIP,       (80,  200, 120), 1),  # skip — placeholder

    # --- trail leg --- layer 1
    (TRAIL_HIP,   TRAIL_KNEE,    (60,  160,  90), 1),
    (TRAIL_KNEE,  TRAIL_ANKLE,   (60,  160,  90), 1),

    # --- front arm (left for LHB) --- layer 2
    (FRONT_SHOULDER, FRONT_ELBOW, (255, 200,  50), 2),
    (FRONT_ELBOW,    FRONT_WRIST, (255, 200,  50), 2),
]

# Remove the bogus leg connection added above
SKEL_CONNECTIONS = [c for c in SKEL_CONNECTIONS
                    if not (c[0] == LEAD_ANKLE and c[1] == LEAD_HIP)]

KEY_JOINTS = {NOSE, L_SHOULDER, R_SHOULDER, L_HIP, R_HIP,
              L_ELBOW, R_ELBOW, L_WRIST, R_WRIST, L_KNEE, R_KNEE}

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_skeleton_3d(frame, vw, vh):
    """
    Depth-aware skeleton:
    - Bones drawn in back→front order
    - Thickness scales with average depth of endpoints
    - Joint brightness scales with depth (closer = more saturated/bright)
    - Thin dark outline on each bone for contrast
    - Ground shadow projected below feet
    """
    def pt(i):
        lm = get_lm(i)
        if lm is None: return None
        return (int(lm["x"] * vw), int(lm["y"] * vh))

    def pt3(i):
        lm = get_lm(i)
        if lm is None: return None
        return np.array([lm["x"] * vw, lm["y"] * vh, lm["z"]])

    # --- ground shadow under feet ---
    foot_ids = [L_ANKLE, R_ANKLE, L_HEEL, R_HEEL, L_FOOT, R_FOOT]
    foot_pts = [pt(i) for i in foot_ids if pt(i) is not None]
    if foot_pts:
        max_y = max(fp[1] for fp in foot_pts)
        shadow_y = min(max_y + 6, vh - 4)
        xs = [fp[0] for fp in foot_pts]
        shadow_w = max(abs(max(xs) - min(xs)), 20)
        cx = (max(xs) + min(xs)) // 2
        overlay = frame.copy()
        cv2.ellipse(overlay, (cx, shadow_y),
                    (shadow_w // 2, 8), 0, 0, 360, (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.35, frame, 0.65, 0, frame)

    # Sort connections by layer so back limbs draw first
    for layer in [0, 1, 2]:
        for (a, b, base_color, lyr) in SKEL_CONNECTIONS:
            if lyr != layer: continue
            pa, pb = pt(a), pt(b)
            if pa is None or pb is None: continue

            # Average Z depth of this bone (0=far, 1=close)
            za = z_of(a); zb = z_of(b)
            z_avg = (za + zb) / 2.0

            # Thickness: 2–7 based on depth
            thickness = max(2, int(2 + z_avg * 5))

            # Color: blend base toward white as it gets closer
            bone_color = lerp_color((40, 40, 40), base_color, 0.4 + z_avg * 0.6)

            # Dark outline for 3D pop
            cv2.line(frame, pa, pb, (0, 0, 0), thickness + 3, cv2.LINE_AA)
            cv2.line(frame, pa, pb, bone_color, thickness, cv2.LINE_AA)

    # --- joints ---
    for i in range(33):
        p = pt(i)
        if p is None: continue

        z = z_of(i)
        is_key = i in KEY_JOINTS

        # Radius: 4–11 for key, 3–6 for minor
        if is_key:
            r = int(5 + z * 6)
        else:
            r = int(3 + z * 3)

        # Color by role + depth
        if i in {L_WRIST, R_WRIST}:
            base = (50, 200, 255)   # wrists = orange
        elif i in {L_ELBOW, R_ELBOW}:
            base = (80, 160, 255)   # elbows = blue-orange
        elif i in {L_SHOULDER, R_SHOULDER}:
            base = (200, 200, 200)  # shoulders = white-gray
        elif i in {L_HIP, R_HIP}:
            base = C_ACCENT
        elif i in {L_KNEE, R_KNEE}:
            base = (80, 200, 120)
        elif i == NOSE:
            base = (220, 220, 220)
        else:
            base = (100, 100, 100)

        joint_color = lerp_color((20, 20, 20), base, 0.3 + z * 0.7)

        # Outer dark ring
        cv2.circle(frame, p, r + 2, (0, 0, 0), -1, cv2.LINE_AA)
        # Main joint
        cv2.circle(frame, p, r, joint_color, -1, cv2.LINE_AA)
        # Specular highlight dot (top-left of joint) for 3D look
        if r >= 5:
            hx = p[0] - max(1, r // 3)
            hy = p[1] - max(1, r // 3)
            cv2.circle(frame, (hx, hy), max(1, r // 3),
                       lerp_color(joint_color, (255, 255, 255), 0.6),
                       -1, cv2.LINE_AA)

    # --- hip rotation arc indicator ---
    # Draw a curved arc between hips showing rotation
    if is_good(L_HIP) and is_good(R_HIP):
        lh_pt = pt(L_HIP); rh_pt = pt(R_HIP)
        if lh_pt and rh_pt:
            cx = (lh_pt[0] + rh_pt[0]) // 2
            cy = (lh_pt[1] + rh_pt[1]) // 2
            rad = max(8, abs(lh_pt[0] - rh_pt[0]) // 3)
            cv2.ellipse(frame, (cx, cy - 5), (rad, rad // 2),
                        0, 180, 360, C_ACCENT, 1, cv2.LINE_AA)

# =========================================================
# HUD PANEL
# =========================================================
def draw_sparkline(panel, x, y, w, h, data, color):
    cv2.rectangle(panel, (x, y), (x + w, y + h), (28, 28, 28), -1)
    pts = list(data)
    if len(pts) < 2: return
    mn, mx = min(pts), max(pts)
    rng = mx - mn if mx != mn else 1.0
    coords = [(x + int(i * w / len(pts)),
               y + h - int((v - mn) / rng * (h - 2)) - 1)
              for i, v in enumerate(pts)]
    for i in range(1, len(coords)):
        cv2.line(panel, coords[i-1], coords[i], color, 1, cv2.LINE_AA)

def build_hud_panel(metrics, phase, panel_h):
    panel = np.full((panel_h, HUD_W, 3), 18, dtype=np.uint8)

    gx = 10
    gw = HUD_W - 20
    gh = 22
    y  = 10

    cv2.putText(panel, "SWING ANALYZER", (gx, y + 18),
                cv2.FONT_HERSHEY_DUPLEX, 0.65, C_ACCENT, 1, cv2.LINE_AA)
    y += 26
    cv2.line(panel, (gx, y), (gx + gw, y), C_ACCENT, 1)
    y += 8

    pc = PHASE_COLORS.get(phase, C_GRAY)
    cv2.rectangle(panel, (gx, y), (gx + gw, y + 26), (35, 35, 35), -1)
    cv2.rectangle(panel, (gx, y), (gx + gw, y + 26), pc, 1)
    cv2.putText(panel, f"PHASE: {phase}", (gx + 8, y + 18),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, pc, 1, cv2.LINE_AA)
    y += 34

    # Handedness label
    hand_label = f"{'LEFT' if HANDEDNESS == 'LEFT' else 'RIGHT'}-HANDED  |  CHEST CAM"
    cv2.putText(panel, hand_label, (gx, y + 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.38, C_GRAY, 1, cv2.LINE_AA)
    y += 18

    def section(title):
        nonlocal y
        cv2.putText(panel, title, (gx, y + 13),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, C_GRAY, 1, cv2.LINE_AA)
        cv2.line(panel, (gx, y + 16), (gx + gw, y + 16), (55, 55, 55), 1)
        y += 22

    def row(label, val, unit, rating, color):
        nonlocal y
        cv2.putText(panel, f"{label}: {int(val)}{unit}", (gx, y + 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.47, C_WHITE, 1, cv2.LINE_AA)
        bw = 46
        cv2.rectangle(panel, (gx + gw - bw, y + 2), (gx + gw, y + gh - 2), color, -1)
        cv2.putText(panel, rating, (gx + gw - bw + 6, y + 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, C_DARK, 1, cv2.LINE_AA)
        y += gh + 4

    def bar(label, val, vmin, vmax, unit="°", color=C_ACCENT):
        nonlocal y
        cv2.rectangle(panel, (gx, y), (gx + gw, y + gh), (35, 35, 35), -1)
        cv2.rectangle(panel, (gx, y), (gx + gw, y + gh), (60, 60, 60), 1)
        pct = np.clip((val - vmin) / (vmax - vmin + 1e-6), 0, 1)
        fw = int(gw * pct)
        if fw > 2:
            cv2.rectangle(panel, (gx, y + 2), (gx + fw, y + gh - 2), color, -1)
        cv2.putText(panel, f"{label}: {int(val)}{unit}", (gx + 4, y + gh - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, C_WHITE, 1, cv2.LINE_AA)
        y += gh + 4

    def spark(data, color):
        nonlocal y
        draw_sparkline(panel, gx, y, gw, 28, data, color)
        y += 32

    section("HIP")
    bar("Hip Open Angle", metrics["hip_angle"], 0, 180)
    r, c = score_metric(metrics["hip_sep"], 15, 55)
    row("Hip-Shldr Sep", metrics["hip_sep"], "°", r, c)
    spark(history["hip_rot"], C_ACCENT)

    section("SHOULDER")
    r, c = score_metric(metrics["shoulder_tilt"], 0, 25)
    row("Tilt", metrics["shoulder_tilt"], "px", r, c)
    r, c = score_metric(metrics["shoulder_rot"], 10, 60)
    row("Rotation", metrics["shoulder_rot"], "°", r, c)

    section("ELBOW")
    r, c = score_metric(metrics["back_elbow"], 50, 110)
    row("Back Elbow", metrics["back_elbow"], "°", r, c)
    r, c = score_metric(metrics["front_elbow"], 70, 160)
    row("Front Elbow", metrics["front_elbow"], "°", r, c)
    spark(history["back_elbow"], C_ORANGE)

    section("HEAD & STRIDE")
    hs = metrics["head_status"]
    hc = C_GREEN if hs == "STABLE" else C_RED
    cv2.putText(panel, f"Head: {hs}", (gx, y + 14),
                cv2.FONT_HERSHEY_SIMPLEX, 0.47, hc, 1, cv2.LINE_AA)
    y += gh + 4
    r, c = score_metric(metrics["stride_pct"], 50, 100)
    row("Stride", metrics["stride_pct"], "%", r, c)
    spark(history["stride"], C_YELLOW)

    cv2.putText(panel, "S=anchor  SPACE=pause  Q=quit",
                (gx, panel_h - 14),
                cv2.FONT_HERSHEY_SIMPLEX, 0.37, C_GRAY, 1, cv2.LINE_AA)

    cv2.line(panel, (0, 0), (0, panel_h), C_ACCENT, 2)
    return panel

# =========================================================
# STATE
# =========================================================
head_anchor    = None
paused         = False
prev_hip_angle = None
current_frame  = None

# =========================================================
# MAIN LOOP
# =========================================================
while True:
    if not paused:
        ret, frame = cap.read()
        if not ret:
            print("Video ended.")
            break
        current_frame = frame.copy()

        vh, vw, _ = frame.shape
        rgb     = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_img  = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        results = detector.detect_for_video(mp_img, frame_index)
        frame_index += 1

        if results.pose_landmarks:
            update_cache(results.pose_landmarks[0])
    else:
        frame = current_frame.copy()
        vh, vw, _ = frame.shape

    def p(i):
        lm = get_lm(i)
        if lm is None: return None
        return np.array([lm["x"] * vw, lm["y"] * vh, lm["z"]])

    # =====================================================
    # METRICS
    # =====================================================
    metrics = {
        "hip_angle":     0.0,
        "hip_sep":       0.0,
        "shoulder_tilt": 0.0,
        "shoulder_rot":  0.0,
        "back_elbow":    90.0,
        "front_elbow":   90.0,
        "head_status":   "NO POSE",
        "stride_pct":    0.0,
    }

    phase = phase_detector.phase

    if all(is_good(i) for i in [L_SHOULDER, R_SHOULDER, L_HIP, R_HIP]):
        ls = p(L_SHOULDER); rs = p(R_SHOULDER)
        lh = p(L_HIP);      rh = p(R_HIP)

        hip_angle = get_angle(ls[:2], lh[:2], rh[:2])
        metrics["hip_angle"] = hip_angle

        shldr_vec = rs[:2] - ls[:2]
        hip_vec   = rh[:2] - lh[:2]
        shldr_ang = np.degrees(np.arctan2(shldr_vec[1], shldr_vec[0]))
        hip_ang   = np.degrees(np.arctan2(hip_vec[1],   hip_vec[0]))
        sep = abs(shldr_ang - hip_ang)
        if sep > 180: sep = 360 - sep
        metrics["hip_sep"]       = sep
        metrics["shoulder_tilt"] = abs(ls[1] - rs[1])
        metrics["shoulder_rot"]  = sep

        hip_delta = (hip_angle - prev_hip_angle) if prev_hip_angle is not None else 0.0
        prev_hip_angle = hip_angle

        wrist_y = 0.5
        if is_good(L_WRIST) and is_good(R_WRIST):
            lw = p(L_WRIST); rw = p(R_WRIST)
            wrist_y = ((lw[1] + rw[1]) / 2) / vh

        phase = phase_detector.update(hip_delta, wrist_y)
        history["hip_rot"].append(hip_delta)
        history["hip_sep"].append(sep)

    # Back elbow = right for LHB
    if all(is_good(i) for i in [BACK_SHOULDER, BACK_ELBOW, BACK_WRIST]):
        bs = p(BACK_SHOULDER); be = p(BACK_ELBOW); bw = p(BACK_WRIST)
        metrics["back_elbow"] = get_angle(bs[:2], be[:2], bw[:2])
        history["back_elbow"].append(metrics["back_elbow"])

    if all(is_good(i) for i in [FRONT_SHOULDER, FRONT_ELBOW, FRONT_WRIST]):
        fs = p(FRONT_SHOULDER); fe = p(FRONT_ELBOW); fw = p(FRONT_WRIST)
        metrics["front_elbow"] = get_angle(fs[:2], fe[:2], fw[:2])

    if is_good(NOSE):
        nose = p(NOSE)
        if head_anchor is None:
            metrics["head_status"] = "SET ANCHOR (S)"
        else:
            dy = nose[1] - head_anchor[1]
            dx = nose[0] - head_anchor[0]
            if   abs(dy) < 18 and abs(dx) < 22: metrics["head_status"] = "STABLE"
            elif dy > 18:                        metrics["head_status"] = "DROPPED"
            elif dy < -18:                       metrics["head_status"] = "RAISED"
            else:                                metrics["head_status"] = "DRIFTING"

    if all(is_good(i) for i in [LEAD_ANKLE, TRAIL_ANKLE, L_HIP, R_HIP]):
        la = p(LEAD_ANKLE); ta = p(TRAIL_ANKLE)
        lh2 = p(L_HIP);     rh2 = p(R_HIP)
        stride_px  = abs(la[0] - ta[0])
        hip_width  = abs(lh2[0] - rh2[0]) + 1e-6
        stride_pct = min((stride_px / hip_width) * 50, 150)
        metrics["stride_pct"] = stride_pct
        history["stride"].append(stride_pct)

    # =====================================================
    # DRAW
    # =====================================================
    draw_skeleton_3d(frame, vw, vh)

    if head_anchor is not None:
        cx, cy = int(head_anchor[0]), int(head_anchor[1])
        cv2.drawMarker(frame, (cx, cy), C_ACCENT,
                       cv2.MARKER_CROSS, 18, 2, cv2.LINE_AA)

    cv2.rectangle(frame, (0, 0), (vw, 32), (0, 0, 0), -1)
    cv2.putText(frame, "AI Baseball Swing Analyzer",
                (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, C_ACCENT, 1, cv2.LINE_AA)

    if paused:
        cv2.putText(frame, "PAUSED", (8, vh - 14),
                    cv2.FONT_HERSHEY_DUPLEX, 1.1, C_YELLOW, 2, cv2.LINE_AA)

    hud = build_hud_panel(metrics, phase, vh)
    composite = np.hstack([frame, hud])

    cv2.imshow("AI Swing Analyzer", composite)

    key = cv2.waitKey(delay) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s') and is_good(NOSE):
        nose = p(NOSE)
        head_anchor = nose[:2].copy()
    elif key == ord(' '):
        paused = not paused

cap.release()
cv2.destroyAllWindows()