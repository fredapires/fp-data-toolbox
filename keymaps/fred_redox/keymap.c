// -----------------------------------
// Todunk's Redox Keymap - 1.0
// -----------------------------------

#include QMK_KEYBOARD_H

// Each layer gets a name for readability, which is then used in the keymap matrix below.
// The underscores don't mean anything - you can have a layer called STUFF or any other name.
// Layer names don't all need to be of the same length, obviously, and you can also skip them
// entirely and just use numbers.

// -----------------------------------
// Layer Definitions
// -----------------------------------
#define _BASE 0     // Base layer
#define _ADJS 1     // Adjustment layer ; TODO: rename this layer to something better
#define _MOUS 2     // Mouse layer
#define _FPSG 3     // FPS gaming layer
#define _LMCR 4     // Left Macro layer
#define _RMCR 5     // Right Macro layer
#define _LNUM 6     // Left hand mod layer for numbers and arithmetic
#define _RNAV 7     // Right hand mod layer for navigation



// -----------------------------------
// Layer switch keycodes
// -----------------------------------
#define TO_BASE TO(_BASE)
#define MO_LNUM MO(_LNUM)
#define MO_RNAV MO(_RNAV)
#define MO_LMCR MO(_LMCR)
#define MO_RMCR MO(_RMCR)
#define MO_ADJS MO(_ADJS)
#define MO_MOUS MO(_MOUS)
#define TO_FPSG TO(_FPSG)





// -----------------------------------
// Custom Keycodes
// -----------------------------------
// System
#define KC_ALF4 LALT(KC_F4)   // Alt + F4
#define KC_CADE LCTL(LALT(KC_DEL)) // Ctrl + Alt + Del ; 
#define KC_WNME LGUI(KC_X)             // GUI + X ; Windows menu
#define KC_GTAB LGUI(KC_TAB)           // GUI + Tab

#define KC_CTLW LCTL(KC_W)             // Ctrl + W ; close tab in various applications
#define KC_CTF4 LCTL(KC_F4)             // Ctrl + F4 ; close tab in various applications

#define KC_SSHK MEH(KC_F12)            // Ctrl + Shift + Alt + F12 ; WHAT IS THIS?
#define KC_MEHT MEH(KC_TAB)            // Ctrl + Shift + Alt + Tab ; WHAT IS THIS?


// Navigation
#define KC_LSGU SWIN(KC_LEFT)          // GUI + Shift + Left ; desktop left
#define KC_RSGU SWIN(KC_RGHT)          // GUI + Shift + Right ; desktop right
#define KC_LCGU LCTL(LGUI(KC_LEFT))    // GUI + Ctrl + Left ;
#define KC_RCGU LCTL(LGUI(KC_RGHT))    // GUI + Ctrl + Right ;


#define KC_ALTT LALT(KC_TAB)           // Alt + Tab ; Alt tab right
#define KC_ALTL LALT(LSFT(KC_TAB))     // Alt + Shift + Tab ; Alt tab left

#define KC_ESCT LALT(KC_ESC)           // Alt + Esc ; Esc tab right
#define KC_ESCL LALT(LSFT(KC_ESC))     // Alt + Shift + Esc ; Esc tab left

#define KC_CTAB LCTL(KC_TAB)           // Ctrl + Tab ; next tab in various applications
#define KC_CSTA LCTL(LSFT(KC_TAB))     // Ctrl + Shift + Tab ; previous tab in various applications

#define KC_CPGD LCTL(KC_PGDN)          // Ctrl + PgDn ; next tab in various applications
#define KC_CPGU LCTL(KC_PGUP)          // Ctrl + PgUp ; previous tab in various applications


#define KC_STAB LSFT(KC_TAB)           // Shift + Tab ; 

// Shift Layer (OLD)
#define KC_SFTA LSFT(KC_A)
#define KC_SFTQ LSFT(KC_Q)
#define KC_SFTW LSFT(KC_W)
#define KC_SFTE LSFT(KC_E)
#define KC_SFTR LSFT(KC_R)
#define KC_SFTT LSFT(KC_T)
#define KC_SFTG LSFT(KC_G)
#define KC_SFTZ LSFT(KC_Z)
#define KC_SFTX LSFT(KC_X)
#define KC_SFTV LSFT(KC_V)
#define KC_SFTB LSFT(KC_B)

// Arithmetic
#define KC_UNDR LSFT(KC_MINS)   // Minus
#define KC_PLUS LSFT(KC_EQL)    // Plus
#define KC_GRTN LSFT(KC_DOT)    // Greater than
#define KC_LSTN LSFT(KC_COMM)   // Less than
#define KC_MULT LSFT(KC_8)      // Multiply

// Coding
#define KC_CSPC LCTL(KC_SPC)        // Ctrl + Space ; Intellisense / Auto Suggest
#define KC_CSLS LCTL(KC_SLSH)       // Ctrl + Slash ; comment / uncomment
#define KC_CENT LCTL(KC_ENT)        // Ctrl + Enter ; execute code
#define KC_CANT LALT(LCTL(KC_ENT))  // Ctrl + Alt + Enter ; Replace all
#define KC_CENT LCTL(KC_ENT)        // Ctrl + Enter ; execute code

#define KC_VSCP LCTL(LSFT(KC_P))    // Ctrl + Shift + P ; VS Code Command pallete
#define KC_ALTQ LALT(KC_Q)          // Alt + Q ; VS Code Command pallete ; various office search
#define KC_ASFZ LALT(LSFT(KC_0))    // Alt + Shift + 0 ; VS Code pivot view

#define KC_SF12 LSFT(KC_F12)        // Shift + F12 ; VS Code peek definition
#define KC_AS12 LALT(LSFT(KC_F12))  // Alt + Shift + F12 ; VS Code go to definition


#define KC_LPAR LSFT(KC_9)          // Open parenthesis
#define KC_RPAR LSFT(KC_0)          // Close parenthesis

#define KC_LCBR LSFT(KC_LBRC)       // Open curly brackets
#define KC_RCBR LSFT(KC_RBRC)       // Close curly brackets


// Excel
#define KC_LCA9 LCA(KC_F9) // Ctrl + Alt + F9 ; Excel recalc all sheets
#define KC_SF11 LSFT(KC_F11) // Shft + F11 ; Excel new sheet // SOMEDAY 22-03-27: adapt excel convention to conform with other applications; aka change this to Ctrl + T or something



// Homerow tap-Hold definitions
#define KC_LCKA LCTL_T(KC_A)    // LCtl over A
#define KC_LGKS LGUI_T(KC_S)    // LGui over S
#define KC_LAKD LALT_T(KC_D)    // LAlt over D
#define KC_LSKF LSFT_T(KC_F)    // LSft over F
   // 
#define KC_RSKJ RSFT_T(KC_J)    // RSft over J
#define KC_RAKK RALT_T(KC_K)    // RAlt over K
#define KC_RGKL RGUI_T(KC_L)    // RGui over L
#define KC_RCKS RCTL_T(KC_SCLN) // RCtl over Semicolon

// ------------------------------------

enum custom_keycodes {

   // System Combos
   M_WINSLP,

   // MS Excel Alt Combos
   M_ALTHOI,  // Adjust width column
   M_ALTHAC,  // middle fit text
   M_ALTHH,   // cell color picker
   M_ALTHN,   // data format

   M_ALTHBO,  // cell outline under   
   M_ALTHBP,  // cell outline over
   M_ALTHBR,  // cell outline right
   M_ALTHBL,  // cell outline left

   M_ALTMP,   // trace precedents
   M_ALTMD,   // trace dependents
   M_ALTMA,   // remove arrows


   M_ALTARA,  // refresh all data
   M_ALTWF,   // freeze frame
   M_ALTFAO,  // save as browse

   M_ALTESV,  // paste values
   M_ALTESF,  // paste formulas
   M_ALTEST,  // paste formatting

   M_ALTNV,   // create pivot table
   M_ALTPIV   // pivot table auto formatting


   // VS Code Ctrl Combos


   // Text editing


   //

};



// -----------------------------------
// Macro Definitions
// -----------------------------------
bool process_record_user(uint16_t keycode, keyrecord_t *record) {
   switch (keycode) {
	/*
    // Example Macro
      case M_MACRO_NM:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING();
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
	// --------------------------------------------------------------
    // System
	/*
      // Windows shutdown / sleep menu
      case M_WINSLP:
         if (record->event.pressed) {
         // when keycode is pressed
         tap_code_delay(KC_T,10);
         // tap_code_delay(LGUI(KC_T),10);
         //tap_code_delay(LALT(KC_F4),10);
         } else {
         // when keycode is released
         }
        return false; // Skip all further processing of this key
	*/
   // --------------------------------------------------------------
    // Excel
	/*
      case M_ALTHOI:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"hoi");
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTNV:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"nv");
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
   */
   /*
      case M_ALTESV:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"esv");tap_code(KC_ENT);
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTEST:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"est");tap_code(KC_ENT);
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTESF:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"esf");tap_code(KC_ENT);
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTARA:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"ara");
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTFAO:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"fao");
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTWF:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"wf");
         } else {
         }
         return false; // Skip all further processing of this key
	*/
   /*
      case M_ALTNV:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING(SS_TAP(X_LALT)"nv");
         } else {
         }
         return false; // Skip all further processing of this key
	*/
   /*
	   case M_ALTPIV:
         if (record->event.pressed) {
         // when keycode is pressed
         tap_code_delay(KC_LALT,80);tap_code_delay(KC_J,15);tap_code_delay(KC_Y,15);tap_code_delay(KC_P,15);tap_code_delay(KC_T,15);tap_code_delay(KC_ESC,15)
         tap_code_delay(KC_LALT,80);tap_code_delay(KC_J,15);tap_code_delay(KC_Y,15);tap_code_delay(KC_P,15);tap_code_delay(KC_R,15);tap_code_delay(KC_ESC,15)
         tap_code_delay(KC_LALT,80);tap_code_delay(KC_J,15);tap_code_delay(KC_Y,15);tap_code_delay(KC_G,15);tap_code_delay(KC_F,15);tap_code_delay(KC_ESC,15)
         tap_code_delay(KC_LALT,80);tap_code_delay(KC_J,15);tap_code_delay(KC_Y,15);tap_code_delay(KC_T,15);tap_code_delay(KC_D,15);tap_code_delay(KC_ESC,15)
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/


   // --------------------------------------------------------------
   // Coding
	/*
      case M_MACRO_NAME:
         if (record->event.pressed) {
         // when keycode is pressed
         SEND_STRING();
         } else {
         // when keycode is released
         }
         return false; // Skip all further processing of this key
	*/
   default:
        return true; // Process all other keycodes normally
   }
return true;
};







// --------------------------------------------------------------
// Layer Keymaps
// --------------------------------------------------------------

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [_BASE] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       KC_ESC  ,KC_1    ,KC_2    ,KC_3    ,KC_4    ,KC_5    ,                                            KC_6    ,KC_7    ,KC_8    ,KC_9    ,KC_0    ,KC_CTF4 ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       KC_TAB  ,KC_Q    ,KC_W    ,KC_E    ,KC_R    ,KC_T    ,_______ ,                          _______ ,KC_Y    ,KC_U    ,KC_I    ,KC_O    ,KC_P    ,KC_BSLS ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       KC_LCTL ,KC_A    ,KC_S    ,KC_D    ,KC_F    ,KC_G    ,_______ ,                          _______ ,KC_H    ,KC_J    ,KC_K    ,KC_L    ,KC_SCLN ,KC_ENT  ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       KC_LSFT ,KC_Z    ,KC_X    ,KC_C    ,KC_V    ,KC_B    ,MO_LMCR ,KC_DEL  ,        KC_DEL  ,MO_RMCR ,KC_N    ,KC_M    ,KC_COMM ,KC_DOT  ,KC_SLSH ,KC_RSFT ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       KC_ALTQ ,KC_LGUI ,KC_MEH  ,KC_LALT ,     MO_LNUM ,    KC_SPC  ,KC_UNDR ,        KC_ENT  ,KC_BSPC ,    MO_RNAV ,     KC_RALT ,KC_MEH  ,KC_QUOT ,KC_APP   
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_LNUM] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       KC_GRV  ,KC_F1   ,KC_F2   ,KC_F3   ,KC_F4   ,KC_F5   ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,KC_MULT ,KC_7    ,KC_8    ,KC_9    ,KC_PLUS ,KC_F11  ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,KC_EQL  ,KC_4    ,KC_5    ,KC_6    ,_______ ,_______ ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,KC_1    ,KC_2    ,KC_3    ,KC_MINS ,_______ ,_______ ,        _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,KC_0    ,KC_DOT  ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______ 
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_RNAV] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                                            KC_F6   ,KC_F7   ,KC_F8   ,KC_F9   ,KC_F10  ,KC_ALF4 ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          KC_F12  ,KC_ESCL ,KC_PGUP ,KC_UP   ,KC_PGDN ,KC_ESCT ,KC_SLSH ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          MO_ADJS ,KC_HOME ,KC_LEFT ,KC_DOWN ,KC_RGHT ,KC_END  ,KC_RCTL ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,        _______ ,MO_MOUS ,KC_LCGU ,KC_CPGU ,KC_GTAB ,KC_CPGD ,KC_RCGU ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,KC_RGUI ,_______ 
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_LMCR] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       _______ ,_______ ,_______ ,KC_LSTN ,KC_GRTN ,_______ ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,KC_LBRC ,KC_RBRC ,KC_SF11 ,_______ ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,KC_LPAR ,KC_RPAR ,_______ ,_______ ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,KC_LCBR ,KC_RCBR ,_______ ,_______ ,_______ ,        _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_RMCR] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,KC_CADE ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          _______ ,KC_AS12 ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          _______ ,KC_SF12 ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,        _______ ,_______ ,KC_ASFZ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_ADJS] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       M_WINSLP,TO_BASE ,TO_FPSG ,_______ ,_______ ,_______ ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,RESET   ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,BL_TOGG ,BL_STEP ,_______ ,_______ ,_______ ,_______ ,                          _______ ,_______ ,KC_MUTE ,KC_VOLU ,KC_MPLY ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       KC_CAPS ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          _______ ,_______ ,KC_MPRV ,KC_VOLD ,KC_MNXT ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,        _______ ,KC_INS  ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_MOUS] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          _______ ,KC_WH_U ,KC_BTN1 ,KC_MS_U ,KC_BTN2 ,KC_WH_D ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                          _______ ,KC_WH_L ,KC_MS_L ,KC_MS_D ,KC_MS_R ,KC_WH_R ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,        _______ ,_______ ,_______ ,KC_WBAK ,_______ ,KC_WFWD ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,_______ ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______ 
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    ),


    [_FPSG] = LAYOUT(
    //┌────────┬────────┬────────┬────────┬────────┬────────┐                                           ┌────────┬────────┬────────┬────────┬────────┬────────┐
       _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,                                            _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┐                         ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,KC_TAB  ,KC_Q    ,KC_W    ,KC_E    ,KC_R    ,KC_T    ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┤                         ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,KC_LCTL ,KC_A    ,KC_S    ,KC_D    ,KC_F    ,KC_G    ,                          _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┐       ┌────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
       _______ ,KC_LSFT ,KC_Z    ,KC_X    ,KC_C    ,KC_V    ,KC_B    ,_______ ,        _______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,_______ ,
    //├────────┼────────┼────────┼────────┼────┬───┴────┬───┼────────┼────────┤       ├────────┼────────┼───┬────┴───┬────┼────────┼────────┼────────┼────────┤
       _______ ,_______ ,_______ ,_______ ,     _______ ,    _______ ,KC_LCTL ,        _______ ,_______ ,    _______ ,     _______ ,_______ ,_______ ,_______
    //└────────┴────────┴────────┴────────┘    └────────┘   └────────┴────────┘       └────────┴────────┘   └────────┘    └────────┴────────┴────────┴────────┘
    )

};





// --------------------------------------------------------------
// Receiver LED color for each layer state
// --------------------------------------------------------------
layer_state_t layer_state_set_user(layer_state_t state) {
    switch (get_highest_layer(state)) {
        case _BASE:
            set_led_off;
            break;
        case _LNUM:
            set_led_green;
            break;
        case _RNAV:
            set_led_blue;
            break;
        case _ADJS:
            set_led_red;
            break;
        case _MOUS:
            set_led_blue;
            break;
        case _FPSG:
            set_led_red;
            break;
        default:
            break;
    }
return state;
};
