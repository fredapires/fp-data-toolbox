/* Copyright 2017 Wunder
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "xd75.h"
#include QMK_KEYBOARD_H
#include "action_layer.h"
#include "version.h"
#include "eeconfig.h"
#include "eeprom.h"

extern keymap_config_t keymap_config;

enum ergodox_layers {
   BASE
  ,LNUM
  ,LNUP
  ,RNAV
  ,BOTH
};

enum custom_keycodes {
  PLACEHOLDER = SAFE_RANGE, // can always be here
  EPRM,
  VRSN,
  RGB_SLD
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

/* BASE
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * | ESC    | 1      | 2      | 3      | 4      | 5      |        |        |        | 6      | 7      | 8      | 9      | 0      | PgUp   |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+-----------------|
 * | TAB    | Q      | W      | E      | R      | T      | Home   |        | End    | Y      | U      | I      | O      | P      | PgDn   |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+-----------------+--------|
 * | LCTRL  | A      | S      | D      | F      | G      | +      |        | *      | H      | J      | K      | L      | ;      |CTL(ENT)|
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------------------------+--------|
 * | LSHIFT | Z      | X      | C      | V      | B      | -      |        | /      | N      | M      | ,      | .      | UP     |SFT(')  |
 * |--------+--------+--------+--------+--------+-----------------+--------+--------+--------+--------+-----------------+--------+--------|
 * |        | LGUI   | \      | APP    | LALT   | LNUM   | SPACE  |        | BSPACE | RNAV   | DEL    | RALT   | LEFT   | DOWN   | RIGHT  |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */

 [BASE] = { /* BASE */
  { KC_ESC,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    	KC_TRNS,		KC_GRV,  	KC_TRNS,  	KC_6,    	KC_7,    KC_8,    KC_9,    KC_0,   	KC_PGUP  		},
  { KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    	KC_HOME,		KC_TRNS, 	KC_END, 	KC_Y,    	KC_U,    KC_I,    KC_O,    KC_P,   	KC_PGDN  		},
  { KC_LCTL, KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    	LSFT(KC_EQL),	KC_TRNS,  	KC_PAST, 	KC_H,    	KC_J,    KC_K,    KC_L,    KC_SCLN,	RCTL_T(KC_ENT)  },
  { KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    	KC_MINS, 		KC_TRNS, 	KC_SLSH, 	KC_N,    	KC_M,    KC_COMM, KC_DOT,  KC_UP, 	RSFT_T(KC_QUOT) },
  { KC_TRNS, KC_LGUI, KC_BSLS, KC_APP,	KC_LALT, MO(LNUM),	KC_SPC,			KC_TRNS, 	KC_BSPC, 	MO(RNAV),	KC_DEL,  KC_RALT, KC_LEFT, KC_DOWN, KC_RGHT  		},
 },

/* LNUM
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * |        | F1     | F2     | F3     | F4     | F5     | F11    |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | ClcAll | 7      | 8      | 9      | ClcSht |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | (      | 4      | 5      | 6      | )      |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | [      | 1      | 2      | 3      | ]      |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * | RESET  |        | 0      | .      | =      |        |        |        |        | BOTH   |        |        |        |        | LNUP   |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */
 
[LNUM] = { /* LNUM */
  { KC_TRNS, KC_F1,   			KC_F2, KC_F3,  KC_F4,  KC_F5,   	KC_F11,  KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, LCTL(LALT(KC_F9)), KC_7,  KC_8,   KC_9,   LSFT(KC_F9), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, LSFT(KC_9), 		KC_4,  KC_5,   KC_6,   LSFT(KC_0),  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_LBRC, 			KC_1,  KC_2,   KC_3,   KC_RBRC, 	KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { RESET,   KC_TRNS, 			KC_0,  KC_DOT, KC_EQL, KC_TRNS, 	KC_TRNS, KC_TRNS, KC_TRNS, MO(BOTH), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, MO(LNUP) },
 }
};
 
/* LNUP
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * |        | F1     | F2     | F3     | F4     | F5     | F11    |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | ClcAll | P7     | P8     | P9     | ClcSht |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | (      | P4     | P5     | P6     | )      |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | [      | P1     | P2     | P3     | ]      |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | NumLck | P0     | .      | =      |        |        |        |        | BOTH   |        |        |        |        |        |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */
 
[LNUP] = { /* LNUP */
  { KC_TRNS, KC_F1,   			KC_F2, KC_F3,  KC_F4,  KC_F5,   	KC_F11,  KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, LCTL(LALT(KC_F9)), KC_P7, KC_P8,  KC_P9,  LSFT(KC_F9), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, LSFT(KC_9), 		KC_P4, KC_P5,  KC_P6,  LSFT(KC_0),  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_LBRC, 			KC_P1, KC_P2,  KC_P3,  KC_RBRC, 	KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_NLCK, 			KC_P0, KC_DOT, KC_EQL, KC_TRNS, 	KC_TRNS, KC_TRNS, KC_TRNS, MO(BOTH), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
 }
};

/* RNAV
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * |        |        |        |        |        |        |        |        | F12    | F6     | F7     | F8     | F9     | F10    |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        |        |        |        |        |        |        |        |        |        | Pg Up  | Up     | Pg Dn  |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        |        |        |        |        |        |        |        |        | Home   | Left   | Down   | Right  | End    |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        |        |        |        |        | BOTH   |        |        |        |        |        |        |        |        |        |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */
 
[RNAV] = { /* RNAV */
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_F12,  KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_TRNS  },
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_PGUP, KC_UP,   KC_PGDN, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_HOME, KC_LEFT, KC_DOWN, KC_RGHT, KC_END,  KC_TRNS  },
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, MO(BOTH), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
 }
};

/* BOTH
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * |        | F1     | F2     | F3     | F4     | F5     | F11    |        | F12    | F6     | F7     | F8     | F9     | F10    |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | ClcAll | 7      | 8      | 9      | ClcSht |        |        |        |        | Pg Up  | Up     | Pg Dn  |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | (      | 4      | 5      | 6      | )      |        |        |        | Home   | Left   | Down   | Right  | End    |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | [      | 1      | 2      | 3      | ]      |        |        |        |        |        |        |        |        |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        |        | 0      | .      | =      |        |        |        |        |        |        |        |        |        |        |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */
 
[BOTH] = { /* BOTH */
  { KC_TRNS, KC_F1,   			KC_F2, KC_F3,  KC_F4,  KC_F5,   	KC_F11,  KC_TRNS, KC_F12,  KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_TRNS  },
  { KC_TRNS, LCTL(LALT(KC_F9)), KC_7,  KC_8,   KC_9,   LSFT(KC_F9), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_PGUP, KC_UP,   KC_PGDN, KC_TRNS, KC_TRNS  },
  { KC_TRNS, LSFT(KC_9), 		KC_4,  KC_5,   KC_6,   LSFT(KC_0),  KC_TRNS, KC_TRNS, KC_TRNS, KC_HOME, KC_LEFT, KC_DOWN, KC_RGHT, KC_END,  KC_TRNS  },
  { KC_TRNS, KC_LBRC, 			KC_1,  KC_2,   KC_3,   KC_RBRC, 	KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, KC_TRNS, 			KC_0,  KC_DOT, KC_EQL, KC_TRNS, 	KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
 }
}; 

const uint16_t PROGMEM fn_actions[] = {

};

const macro_t *action_get_macro(keyrecord_t *record, uint8_t id, uint8_t opt)  
{
  // MACRODOWN only works in this function
      switch(id) {
        case 0:
          if (record->event.pressed) {
            register_code(KC_RSFT);
            #ifdef BACKLIGHT_ENABLE
              backlight_step();
            #endif
          } else {
            unregister_code(KC_RSFT);
          }
        break;
      }
    return MACRO_NONE;
};
