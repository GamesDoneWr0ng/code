section .data
    hello db 'Hello, World!', 0x0A
    len equ $ - hello

section .text
    global _start

_start:
    ; Write 'Hello, World!' to stdout
    mov rax, 0x2000004     ; sys_write
    mov rdi, 1             ; file descriptor for stdout
    lea rsi, [rel hello]   ; address of the hello string
    mov rdx, len           ; length of the hello string
    syscall

    ; Exit the program
    mov rax, 0x2000001     ; sys_exit
    xor rdi, rdi           ; exit code 0
    syscall