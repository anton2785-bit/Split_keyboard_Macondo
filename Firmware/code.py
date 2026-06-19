# code.py — Macondo Split Keyboard
# Firmware: KMK (CircuitPython)
# MCU: Seeed XIAO nRF52840
#
# Matrix per half: 4 rows × 5 cols = 19 keys
# Row 4 has no key at col 3 (gap between thumb keys)
#
# Flash instructions:
#   1. Install CircuitPython on your XIAO nRF52840
#   2. Copy the KMK folder to CIRCUITPY/
#      (download from https://github.com/KMKfw/kmk_firmware)
#   3. Save this file as code.py on CIRCUITPY/
#
# ─────────────────────────────────────────────────────────────────

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# ── Modules ───────────────────────────────────────────────────────
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())

# ── Pin mapping (from schematic) ──────────────────────────────────
# Rows:    R1=P0.28 R2=P0.04 R3=P0.05 R4=P1.11
# Cols:    C1=P0.02 C2=P0.03 C3=P0.29 C4=P0.04_SDA C5=P1.15_MOSI
#
# Update board.XXX names to match your actual CircuitPython board pins.
# Run `import board; print(dir(board))` on your XIAO to list available pins.

keyboard.col_pins = (
    board.D0,   # C1 — P0.02
    board.D1,   # C2 — P0.03
    board.D2,   # C3 — P0.28 (A2)
    board.D3,   # C4 — P0.29 (A3)
    board.D4,   # C5 — P0.04 (SDA)
)

keyboard.row_pins = (
    board.D5,   # R1 — P0.05 (SCL)
    board.D6,   # R2 — P1.11 (TX)
    board.D7,   # R3 — P1.12 (RX)
    board.D8,   # R4 — P1.13 (SCK)
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ── Split config (if wired via UART) ─────────────────────────────
# Uncomment and configure if using a TRRS cable between halves.
# For fully wireless (each half independent), leave commented out.
#
# from kmk.modules.split import Split, SplitType, SplitSide
# split = Split(
#     split_type=SplitType.UART,
#     split_side=SplitSide.LEFT,   # change to RIGHT for the right half
#     data_pin=board.TX,
#     data_pin2=board.RX,
#     use_pio=True,
# )
# keyboard.modules.append(split)

# ── Layer indices ─────────────────────────────────────────────────
BASE = 0
NUMS = 1
FN   = 2

# ── Convenience aliases ───────────────────────────────────────────
# HoldTap: hold_key(hold, tap)
# LT = Layer-Tap, MT = Mod-Tap

def LT(layer, tap):
    return KC.LT(layer, tap)

def MT(mod, tap):
    return KC.MT(tap, mod)

LT_NUMS  = LT(NUMS, KC.SPC)             # Tap=Space,     Hold=NUMS layer
LT_FN    = LT(FN,   KC.ENT)             # Tap=Enter,     Hold=FN layer
MT_LSFT  = MT(KC.LSFT, KC.BSPC)        # Tap=Backspace, Hold=Shift
MT_LCTL  = MT(KC.LCTL, KC.ESC)         # Tap=Escape,    Hold=Ctrl

# ── Keymap ────────────────────────────────────────────────────────
# Layout: 4 rows × 5 cols per half, read left-to-right, top-to-bottom.
# Row 4 col 3 is skipped (no switch) — use KC.TRNS as placeholder.
#
# Left half then right half, mirrored.

keyboard.keymap = [

    # ──────────────────────────────────────────────────────────────
    # LAYER 0 — BASE (QWERTY)
    #
    # Left                              Right
    # ┌─────┬─────┬─────┬─────┬─────┐  ┌─────┬─────┬─────┬─────┬─────┐
    # │  Q  │  W  │  E  │  R  │  T  │  │  Y  │  U  │  I  │  O  │  P  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │  A  │  S  │  D  │  F  │  G  │  │  H  │  J  │  K  │  L  │  '  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │  Z  │  X  │  C  │  V  │  B  │  │  N  │  M  │  ,  │  .  │  /  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │CTL/ │  -  │  =  │xxxxx│ TAB │  │BSPC │xxxxx│  ;  │  \  │ GUI │
    # │ ESC │     │     │     │(FN) │  │(SFT)│     │     │     │     │
    # └─────┴─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┴─────┘
    #                          └── SPC(NUMS) / ENT(FN) centre thumbs ──┘
    # ──────────────────────────────────────────────────────────────
    [
        # Left half
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        MT_LCTL, KC.MINS, KC.EQL,  KC.TRNS, LT_FN,

        # Right half
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.QUOT,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
        MT_LSFT, KC.TRNS, KC.SCLN, KC.BSLS, KC.LGUI,
    ],

    # ──────────────────────────────────────────────────────────────
    # LAYER 1 — NUMS (Numbers & Symbols)
    #
    # Left                              Right
    # ┌─────┬─────┬─────┬─────┬─────┐  ┌─────┬─────┬─────┬─────┬─────┐
    # │  1  │  2  │  3  │  4  │  5  │  │  6  │  7  │  8  │  9  │  0  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │  !  │  @  │  #  │  $  │  %  │  │  ^  │  &  │  *  │  (  │  )  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │  `  │  ~  │  _  │  +  │  =  │  │  -  │  [  │  ]  │  {  │  }  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │     │     │     │xxxxx│     │  │▓▓▓▓▓│xxxxx│     │     │     │
    # └─────┴─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┴─────┘
    # ──────────────────────────────────────────────────────────────
    [
        # Left half
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,
        KC.GRV,  KC.TILD, KC.UNDS, KC.PLUS, KC.EQL,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # Right half
        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.MINS, KC.LBRC, KC.RBRC, KC.LCBR, KC.RCBR,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],

    # ──────────────────────────────────────────────────────────────
    # LAYER 2 — FN (Function Keys, Navigation & Media)
    #
    # Left                              Right
    # ┌─────┬─────┬─────┬─────┬─────┐  ┌─────┬─────┬─────┬─────┬─────┐
    # │ F1  │ F2  │ F3  │ F4  │ F5  │  │ F6  │ F7  │ F8  │ F9  │ F10 │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │ F11 │ F12 │PSCR │SCRL │PAUS │  │  ←  │  ↓  │  ↑  │  →  │  "  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │CAPS │     │MUTE │VOL- │VOL+ │  │HOME │PGDN │PGUP │ END │  |  │
    # ├─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┤
    # │▓▓▓▓▓│     │     │xxxxx│     │  │ DEL │xxxxx│ INS │     │     │
    # └─────┴─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┴─────┘
    # ──────────────────────────────────────────────────────────────
    [
        # Left half
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,
        KC.F11,  KC.F12,  KC.PSCR, KC.SCRL, KC.PAUS,
        KC.CAPS, KC.TRNS, KC.MUTE, KC.VOLD, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # Right half
        KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,
        KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.DQUO,
        KC.HOME, KC.PGDN, KC.PGUP, KC.END,  KC.PIPE,
        KC.DEL,  KC.TRNS, KC.INS,  KC.TRNS, KC.TRNS,
    ],
]

# ── Start! ────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
