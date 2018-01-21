	  COPY   START  1000
      FIRST  STL    RETADR
      CLOOP  JSUB   RDREC
        -     LDA    LENGTH
        -    COMP   ZERO
        -     JEQ    ENDFIL
        -     JSUB   WRREC
        -     J      CLOOP
      ENDFIL LDA    EOF
        -     STA    BUFFER
        -     LDA    THREE
        -     STA    LENGTH
        -     JSUB   WRREC
        -     LDL    RETADR
        -     RSUB
      EOF    BYTE   C'EOF'
      THREE  WORD   3
      ZERO   WORD   0
      RETADR RESW   1
      LENGTH RESW   1
      BUFFER RESB   4096
      .
      .      SUBROUTINE TO READ RECORD INTO BUFFER
      .
      RDREC  LDX    ZERO
        -    LDA    ZERO
      RLOOP  TD     INPUT
        -    JEQ    RLOOP
        -     RD     INPUT
        -    COMP   ZERO
        -     JEQ    EXIT
        -     TIX    MAXLEN
        -     JLT    RLOOP
      EXIT   STX    LENGTH
      INPUT  BYTE   X'F1'
      MAXLEN WORD   4096
      .
      .      SUBROUTINE TO WRITE RECORD FROM BUFFER
      .
      WRREC  LDX    ZERO
      WLOOP  TD     OUTPUT
        -    JEQ    WLOOP
        -     WD     OUTPUT
        -     TIX    LENGTH
        -     JLT    WLOOP
      OUTPUT BYTE   X'06'
        -     END    FIRST