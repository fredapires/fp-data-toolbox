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
 * | ESC    | 1      | 2      | 3      | 4      | 5      |  DEL   |        | DEL    | 6      | 7      | 8      | 9      | 0      |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+-----------------|
 * | TAB    | Q      | W      | E      | R      | T      |   (    |        | )      | Y      | U      | I      | O      | P      | S(Tab) |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+-----------------+--------|
 * | LCTRL  | A      | S      | D      | F      | G      |        |        |        | H      | J      | K      | L      | ;      | Enter  |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------------------------+--------|
 * | LSHIFT | Z      | X      | C      | V      | B      |   [    |        | ]      | N      | M      | ,      | .      | /      | RSFT   |
 * |--------+--------+--------+--------+--------+-----------------+--------+--------+--------+--------+-----------------+--------+--------|
 * |   W(X) | Win    | Ins    | APP    | LALT   | LNUM   | SPACE  |   _    | BSPACE | RNAV   | RAlt   | CpsLk  |        | '      |        |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */

 [BASE] = { /* BASE */
  { KC_GESC, 	KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    	KC_DEL,	 	KC_TRNS,  		KC_DEL,  	KC_6,    	KC_7,    KC_8,    KC_9,    KC_0,   	KC_TRNS },
  { KC_TAB,  	KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    	LSFT(KC_9),	KC_TRNS, 		LSFT(KC_0), KC_Y,    	KC_U,    KC_I,    KC_O,    KC_P,   	KC_TRNS },
  { KC_LCTL, 	KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    	KC_TRNS,	KC_TRNS,  		KC_TRNS, 	KC_H,    	KC_J,    KC_K,    KC_L,    KC_SCLN,	KC_ENT	},
  { KC_LSFT, 	KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    	KC_LBRC,	KC_TRNS, 		KC_RBRC, 	KC_N,    	KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT	},
  { LGUI(KC_X), KC_LGUI, KC_INS,  KC_APP,  KC_LALT, MO(LNUM),	KC_SPC,		LSFT(KC_MINS), 	KC_BSPC, 	MO(RNAV),	KC_RALT, KC_TRNS, KC_TRNS, KC_QUOT, KC_TRNS },
 },

/* LNUM & RNAV
 * .--------------------------------------------------------------------------------------------------------------------------------------.
 * |        | F1     | F2     | F3     | F4     | F5     | S(F11) |        | F12    | F6     | F7     | F8     | F9     | F10    |  A+F4  |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * | Win(T) | *      | 7      | 8      | 9      | +      |   `    |        | \      | VirL   | Pg Up  | Up     | Pg Dn  | VirL   |  WTab  |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | <      | 4      | 5      | 6      | >      |        |        |        | Home   | Left   | Down   | Right  | End    |  RCtl  |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * |        | /      | 1      | 2      | 3      | -      |        |        |        | WinL   | CTab   |        | CSTb   | WinR   |        |
 * |--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------|
 * | S(F11) | CA(F9) | 0      | .      | =      | BOTH   |        |        |        | BOTH   |        |        |        |        |        |
 * '--------------------------------------------------------------------------------------------------------------------------------------'
 */
 
[LNUM] = { /* LNUM */
  { KC_TRNS, 		KC_F1,   		KC_F2, KC_F3,  KC_F4,  KC_F5,   	 KC_F11,  	KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { LGUI(KC_T), 	KC_PAST, 		KC_7,  KC_8,   KC_9,   LSFT(KC_EQL), KC_GRV,	KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, 		LSFT(KC_COMM),  KC_4,  KC_5,   KC_6,   LSFT(KC_DOT), KC_TRNS,	KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { KC_TRNS, 		KC_SLSH, 		KC_1,  KC_2,   KC_3,   KC_MINS, 	 KC_TRNS,	KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
  { LSFT(KC_F11), 	LCA(KC_F9), 	KC_0,  KC_DOT, KC_EQL, KC_TRNS, 	 KC_TRNS,	KC_TRNS, KC_TRNS, MO(BOTH), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS  },
 },

[RNAV] = { /* RNAV */
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_F12,  KC_F6,   				KC_F7,   			KC_F8,   KC_F9,   		KC_F10,  		LALT(KC_F4)   	},
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_BSLS, LCTL(LGUI(KC_LEFT)), 	KC_PGUP, 			KC_UP,   KC_PGDN, 		KC_TRNS, 		LGUI(KC_TAB)	},
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, KC_HOME, 				KC_LEFT, 			KC_DOWN, KC_RGHT, 		KC_END,  		KC_RCTL  		},
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_TRNS, KC_TRNS, KC_TRNS, SWIN(KC_LEFT), 		LCTL(LSFT(KC_TAB)), KC_TRNS, LCTL(KC_TAB), 	SWIN(KC_RGHT), 	KC_TRNS  		},
  { KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, MO(BOTH), KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, 				KC_TRNS, 			KC_TRNS, KC_TRNS, 		KC_TRNS, 		KC_TRNS  		},
 },
 
[BOTH] = { /* BOTH */
  { KC_TRNS, 		KC_F1,   		KC_F2, KC_F3,  KC_F4,  KC_F5,   	 KC_F11,  	KC_TRNS, KC_F12,  KC_F6,   				KC_F7,   			KC_F8,   KC_F9,   		KC_F10,  		LALT(KC_F4)   	},
  { LGUI(KC_T), 	KC_PAST, 		KC_7,  KC_8,   KC_9,   LSFT(KC_EQL), KC_GRV, 	KC_TRNS, KC_BSLS, LCTL(LGUI(KC_LEFT)), 	KC_PGUP, 			KC_UP,   KC_PGDN, 		KC_TRNS, 		LGUI(KC_TAB)	},
  { KC_TRNS, 		LSFT(KC_COMM),  KC_4,  KC_5,   KC_6,   LSFT(KC_DOT), KC_TRNS, 	RESET,   KC_TRNS, KC_HOME, 				KC_LEFT, 			KC_DOWN, KC_RGHT, 		KC_END,  		KC_RCTL  		},
  { KC_TRNS, 		KC_SLSH, 		KC_1,  KC_2,   KC_3,   KC_MINS, 	 KC_TRNS, 	KC_TRNS, KC_TRNS, SWIN(KC_LEFT), 		LCTL(LSFT(KC_TAB)), KC_TRNS, LCTL(KC_TAB), 	SWIN(KC_RGHT), 	KC_TRNS  		},
  { LSFT(KC_F11), 	LCA(KC_F9), 	KC_0,  KC_DOT, KC_EQL, KC_TRNS, 	 KC_TRNS, 	KC_TRNS, KC_TRNS, KC_TRNS, 				KC_TRNS, 			KC_TRNS, KC_TRNS, 		KC_TRNS, 		KC_TRNS  		},
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
