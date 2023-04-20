;section .data                           ;Data segment
;   userMsg db 'Please enter a number: ' ;Ask the user to enter a number
;   lenUserMsg equ $-userMsg             ;The length of the message
;   dispMsg db 'You have entered: '
;   lenDispMsg equ $-dispMsg
;
;section .bss           ;Uninitialized data
;   num resb 5
;
;section .text
;    global _start
;
;_start:
;    mov rax, 0x2000004
;    mov rdi, 1
;    lea rsi, [rel userMsg]
;    mov rdx, lenUserMsg
;    syscall
;
;    ; Read and store the user input
;    mov rax, 0x2000003
;    mov rdi, 0
;    lea rsi, [rel num]
;    mov rdx, 5
;    syscall
;
;    mov rax, 0x2000004
;    mov rdi, 1
;    lea rsi, [rel dispMsg]
;    mov rdx, lenDispMsg
;    syscall
;
;    ;Output the number entered
;    mov rax, 0x2000004
;    mov rdi, 1
;    lea rsi, [rel num]
;    mov rdx, 5
;    syscall
;
;    ; Exit the program
;    mov rax, 0x2000001     ; sys_exit
;    xor rdi, rdi           ; exit code 0
;    syscall

section .data
   msg db 'Displaying 9 stars', 0xa
   len equ $ - msg
   s2 times 10 db '*'

section .text
    global _start

_start:
    ; Displaying 9 stars
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel msg]
    mov rdx, len
    syscall

    ; chainging 10 stars to 9 stars with a new line
    lea rbx, [rel s2]
    add rbx, 9
    mov byte [rbx], 0xa

    ; print 9 stars
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel s2]
    mov rdx, 10
    syscall

    ; Exit the program
    mov rax, 0x2000001     ; sys_exit
    xor rdi, rdi           ; exit code 0
    syscall