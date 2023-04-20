section .data
    msg1 db "Enter a digit: "
    len1 equ $- msg1 

    msg2 db "Please enter a second digit: "
    len2 equ $- msg2 

    msg3 db "The sum is: "
    len3 equ $- msg3

    newline db 0xa

segment .bss
    num1 resb 2
    num2 resb 2
    sum resb 3

section .text
    global _start

_start:
    ; msg 1
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel msg1]
    mov rdx, len1
    syscall

    ; Read 1
    mov rax, 0x2000003
    mov rdi, 0
    lea rsi, [rel num1]
    mov rdx, 2
    syscall

    ; msg 2
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel msg2]
    mov rdx, len2
    syscall

    ; Read 2
    mov rax, 0x2000003
    mov rdi, 0
    lea rsi, [rel num2]
    mov rdx, 2
    syscall

    ; msg 3
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel msg3]
    mov rdx, len3
    syscall

    ; store num1 and num2 in rax and rbx then convert to desimal by sub '0'
    mov rax, [rel num1]
    mov rbx, [rel num2]

    sub rax, '0'
    sub rbx, '0'

    ; add the two numbers and convert back to ascii
    add rax, rbx
    add rax, '0'

    ; store sum in sum
    mov [rel sum], rax

    ; print the sum
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel sum]
    mov rdx, 1
    syscall

    ; newline
    mov rax, 0x2000004
    mov rdi, 1
    lea rsi, [rel newline]
    mov rdx, 1
    syscall

exit:
    mov rax, 0x2000001
    xor rdi, rdi
    syscall