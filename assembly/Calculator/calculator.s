    %macro writeString 2
        mov rax, 0x2000004
        mov rdi, 1
        mov rsi, %1
        mov rdx, %2
        syscall
    %endmacro

    %macro readString 2
        mov rax, 0x2000003
        mov rdi, 0
        lea rsi, %1
        mov rdx, %2
        syscall
    %endmacro

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
    writeString msg1, len1
    readString [rel num1], 2

    writeString msg2, len2
    readString [rel num2], 2

    writeString msg3, len3

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

    writeString sum, 1
    writeString newline, 1

exit:
    mov rax, 0x2000001
    xor rdi, rdi
    syscall