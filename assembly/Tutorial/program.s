section .text
    global _start

section .bss
    num resb 1

_start:
    mov rcx,10
    mov rax, '1'

    l1:
        mov [rel num], rax
        mov rax, 0x2000004
        mov rdi, 1
        push rcx

        lea rsi, [rel num]
        mov rdx, 1
        syscall

        mov rax, [rel num]
        sub rax, '0'
        inc rax
        add rax, '0'
        pop rcx
        loop l1

exit:
    mov rax, 0x2000001
    xor rdi, rdi
    syscall