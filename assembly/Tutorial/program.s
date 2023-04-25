    %macro writeString 2
        mov rax, 0x2000004
        mov rdi, 1
        mov rsi, %1
        mov rdx, %2
        syscall
    %endmacro

section .data
    msg1 db 'Hello world!', 0xa
    len1 equ $ - msg1

    msg2 db 'This is a string!', 0xa
    len2 equ $ - msg2

    msg3 db 'Goodbye!', 0xa
    len3 equ $ - msg3

section .text
    global _start

_start:
    writeString msg1, len1
    writeString msg2, len2
    writeString msg3, len3

exit:
    mov rax, 0x2000001
    xor rdi, rdi
    syscall