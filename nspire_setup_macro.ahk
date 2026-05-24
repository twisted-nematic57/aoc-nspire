; =========================================================================
; TI-Nspire Python AoC Solution Template with Auto-Inserted Inputs Setup-er
; =========================================================================

; Run this macro from the same directory where your generated Python files are.
; By default this is temp_workspace/py/

; Before running, create a brand new doc in TI-Nspire software and save it.
; Then on the first open tab, close the menu so that the "Press menu" text is
; only thing visible on the tab. When you click back into the Nspire software
; window, the menu will reappear if you click inside the tab content page.

; Do not move your mouse while the macro is running as that can mess up menu
; selection. (Submenus open instantly on hover on the Nspire platform, unlike
; Windows and Mac where there is a slight delay/manual click-in needed to expand
; submenus.)

; Press the ESC key at any time to insta-kill the macro execution in case of failure.


; PROBLEM-SPECIFIC NOTES:
; - You're going to have to paste Day 7 of 2016 manually in chunks. It is too large to be pasted all at once (software-enforced limit by Nspire Software). This macro automatically skips Day 7 of 2016.
; - Day 8 of 2015 and Day 9 of 2017 and may contain a sequence of three quotes in the input (literally: """) so you may need to escape those manually using \ OR change the surrounding quotes to literally '''.

#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; ---- CONFIGURATION (all range endpoint values are INCLUSIVE)
TargetYear  := 2015    ; Change this to the year you want to process
StartDay    := 1       ; Starting day (change this if resuming from an error)
EndDay      := 25      ; Upper limit day (e.g., 25 for 2015-2024, 12 for 2025)

; ---- TIMING DELAYS (adjust in milliseconds if the TI-Nspire software lags)
KeyDelay    := 500     ; Pause between structural menu navigation steps
PasteDelay  := 1000    ; Pause to allow large text blocks to paste into the editor
PageDelay   := 500     ; Pause to allow a new document tab to load
; =========================================================================

MsgBox, 4, AoC Auto-Setup-er, Ensure TI-Nspire Software is open to a blank document.`n`nPress YES to begin. You will have 3 seconds to manually Alt-Tab into the TI Software window.
IfMsgBox, No
    ExitApp

Sleep, 3000 ; 3 seconds buffer time to alt-tab into software

Loop, % (EndDay - StartDay + 1)
{
    CurrentDay := StartDay + A_Index - 1

    ; HARDCODED EXCEPTION: Skip Day 7 of 2016 due to gargantuan input size
    if (TargetYear = 2016 and CurrentDay = 7)
    {
        continue
    }

    ; Zero-pad the day number to make the Python editor "Open" menu look more organized
    if (CurrentDay < 10)
        PadDay := "0" . CurrentDay
    else
        PadDay := CurrentDay

    FileName := "y" . TargetYear . "d" . PadDay . ".py"
    ScriptName := "y" . TargetYear . "d" . PadDay

    ; Verify file exists before changing clipboard or firing keys
    if !FileExist(FileName)
    {
        MsgBox, 16, Error, File not found: %FileName%`nStopping automation loop.
        ExitApp
    }

    ; Read Python script directly into Windows Clipboard
    FileRead, FileContents, %FileName%
    Clipboard := FileContents
    ClipWait, 2 ; Ensure clipboard successfully holds data

    ; --- START REPEATING KEYBOARD SEQUENCE ---

    ; 1. Open Menu options (User Keys: A, 1)
    Send, a
    Sleep, %KeyDelay%
    Send, 1
    Sleep, %KeyDelay%

    ; 2. Type Script Name & Hit Enter
    SendRaw, %ScriptName%
    Sleep, %KeyDelay%
    Send, {Enter}
    Sleep, %PageDelay% ; Wait for new Python editor window to settle

    ; 3. Paste Clipboard Code (User Key: Ctrl+V)
    Send, ^v
    Sleep, %PasteDelay%

    ; 4. Check Syntax & Save (User Keys: Ctrl+Shift+M, 2, 2)
    Send, ^+m
    Sleep, %KeyDelay%
    Send, 2
    Sleep, %KeyDelay%
    Send, 2
    Sleep, %KeyDelay%

    ; 5. Open New Tab for the Next Loop (User Key: Ctrl+I)
    ; Only generate a new page if we haven't reached the end limit
    if (CurrentDay < EndDay)
    {
        Send, ^i
        Sleep, %PageDelay%
    }
}

MsgBox, 64, Success, Templates with inputs insertion finished successfully!
ExitApp

; =========================================================================
; EMERGENCY PANIC BUTTON
; =========================================================================
; Press the ESCAPE key at any time to instantly kill the macro execution.
Esc::
ExitApp
